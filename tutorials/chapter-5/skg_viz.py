"""
skg_viz.py
==========
Reusable visualization helpers for the Chapter 5 (Knowledge Graph Learning)
tutorial series from "AI-Powered Search" (Grainger, Turnbull, Irwin).

These helpers operate on the traversal dict returned by `skg.traverse(...)`
in the book's `aips` helper library.

Two main functions:
    plot_relatedness_bars(traversal, query)  -- horizontal bar chart of scores
    draw_graph(traversal, query)             -- force-directed ego-graph

Both render inline in Jupyter. They require only matplotlib and networkx,
which are already in the book's environment.
"""

from __future__ import annotations

from typing import Dict, Iterable

import matplotlib.pyplot as plt
import networkx as nx


# ---------------------------------------------------------------------------
# Traversal parsing
# ---------------------------------------------------------------------------

def extract_related_terms(traversal: dict, query: str) -> Dict[str, float]:
    """
    Pull the {term: relatedness} dict out of an SKG traversal result.

    The book's traversal response is shaped like:
        traversal["graph"][0]["values"][query]["traversals"][0]["values"]
            -> {"motrin": {"relatedness": 0.599}, "aleve": {...}, ...}

    Returns an ordered dict (insertion-ordered, descending by score) of the
    related terms and their relatedness scores.
    """
    try:
        raw = (
            traversal["graph"][0]["values"][query]["traversals"][0]["values"]
        )
    except (KeyError, IndexError, TypeError) as exc:
        raise ValueError(
            "Could not find related terms in the traversal. "
            "Expected traversal['graph'][0]['values'][<query>]"
            "['traversals'][0]['values']. "
            f"Got: {type(traversal).__name__}"
        ) from exc

    pairs = [(term, stats.get("relatedness", 0.0)) for term, stats in raw.items()]
    pairs.sort(key=lambda kv: kv[1], reverse=True)
    return dict(pairs)


# ---------------------------------------------------------------------------
# Bar chart
# ---------------------------------------------------------------------------

def plot_relatedness_bars(
    traversal: dict,
    query: str,
    *,
    figsize: tuple = (8, 5),
    highlight_color: str = "#d62728",
    bar_color: str = "#1f77b4",
) -> None:
    """
    Horizontal bar chart of relatedness scores. The bar for the original
    query term itself is highlighted so learners can immediately see "the
    query always relates most strongly to itself".
    """
    scores = extract_related_terms(traversal, query)
    terms = list(scores.keys())
    values = list(scores.values())

    # Reverse so the highest score is at the top of the chart
    terms_rev = terms[::-1]
    values_rev = values[::-1]
    colors = [highlight_color if t.lower() == query.lower() else bar_color
              for t in terms_rev]

    fig, ax = plt.subplots(figsize=figsize)
    bars = ax.barh(terms_rev, values_rev, color=colors)

    ax.set_xlabel("Relatedness score (sigmoid-normalized, -1.0 to 1.0)")
    ax.set_title(f"Terms most related to '{query}'")
    ax.set_xlim(0, max(1.0, max(values_rev) * 1.1))
    ax.grid(axis="x", linestyle="--", alpha=0.3)

    # Annotate each bar with the numeric score
    for bar, val in zip(bars, values_rev):
        ax.text(
            val + 0.01,
            bar.get_y() + bar.get_height() / 2,
            f"{val:.3f}",
            va="center",
            fontsize=9,
        )

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# Graph view
# ---------------------------------------------------------------------------

def draw_graph(
    traversal: dict,
    query: str,
    *,
    figsize: tuple = (8, 7),
    min_score: float = 0.0,
    center_color: str = "#d62728",
    leaf_color: str = "#1f77b4",
    edge_label_fmt: str = "{:.2f}",
    seed: int = 7,
) -> None:
    """
    Ego-graph: the query term in the center, related terms around it,
    edge thickness and label proportional to relatedness score.

    Use `min_score` to filter out weak/negative neighbors when the result
    list gets noisy.
    """
    scores = extract_related_terms(traversal, query)

    G = nx.Graph()
    G.add_node(query)
    for term, score in scores.items():
        if term.lower() == query.lower():
            continue  # the query-to-itself self-loop is implicit; skip it
        if score < min_score:
            continue
        G.add_node(term)
        G.add_edge(query, term, weight=score)

    if G.number_of_edges() == 0:
        print(f"No related terms above min_score={min_score}.")
        return

    pos = nx.spring_layout(G, seed=seed, k=1.6)

    fig, ax = plt.subplots(figsize=figsize)

    # Nodes
    node_colors = [center_color if n == query else leaf_color for n in G.nodes()]
    node_sizes = [2400 if n == query else 1600 for n in G.nodes()]
    nx.draw_networkx_nodes(
        G, pos, node_color=node_colors, node_size=node_sizes, ax=ax,
        edgecolors="white", linewidths=2,
    )

    # Edges: width proportional to relatedness
    weights = [G[u][v]["weight"] for u, v in G.edges()]
    edge_widths = [max(0.6, w * 4.0) for w in weights]
    nx.draw_networkx_edges(
        G, pos, width=edge_widths, edge_color="#888", alpha=0.7, ax=ax,
    )

    # Labels
    nx.draw_networkx_labels(
        G, pos, font_size=10, font_color="white", font_weight="bold", ax=ax,
    )

    # Edge labels (relatedness scores)
    edge_labels = {(u, v): edge_label_fmt.format(d["weight"])
                   for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, font_size=8, ax=ax,
    )

    ax.set_title(f"Semantic neighborhood of '{query}'")
    ax.axis("off")
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# Convenience: side-by-side both views
# ---------------------------------------------------------------------------

def show_both(traversal: dict, query: str, **kwargs) -> None:
    """Render bar chart and graph view back to back."""
    plot_relatedness_bars(traversal, query)
    draw_graph(traversal, query, **kwargs)
