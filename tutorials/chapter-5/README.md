# Chapter 5 — Hands-on tutorials

A short series of notebooks that walk through the core ideas of Chapter 5
("Knowledge graph learning") of *AI-Powered Search*. Each tutorial is
self-contained, takes 20–30 minutes, and assumes you already have the
book's Docker environment running.

## Audience

You've worked with an inverted-index search engine (Solr, Elasticsearch,
OpenSearch). You know what an inverted index is, you've written a facet
query, and you have an intuition for BM25. You may or may not have read
all of Chapter 5 — each notebook re-derives the concepts it needs.

## Setup (one time)

If you haven't yet installed Docker, cloned the book's repo, or indexed
the chapter-5 datasets, **start with [`../SETUP.md`](../SETUP.md)** — it
walks through everything from scratch (Mac and Windows both supported)
and ends by pointing you at the verification notebook below.

If you think your environment is ready, jump straight to
[`../00_verify_setup.ipynb`](../00_verify_setup.ipynb). It runs seven
discrete checks and tells you the exact fix-it step for anything that's
broken.

Once that's green, you're ready to start Tutorial 1.

## Tutorials

| # | Notebook | Time | What you'll learn |
|---|----------|------|-------------------|
| 1 | [`01_advil_moment.ipynb`](01_advil_moment.ipynb) | 20 min | The core SKG primitive — turn `advil` into `motrin, aleve, ibuprofen` with one Solr request. |
| 2 | *(planned)* `02_query_expansion.ipynb` | 25 min | Use the SKG to rewrite a sparse query four different ways. Measure precision@5 changes. |
| 3 | *(planned)* `03_typed_relationships.ipynb` | 20 min | Traverse through a "relationship node" to find typed edges. Who's in love with Jean Grey? |
| 4 | *(planned)* `04_hearst_patterns.ipynb` | 30 min | Build an explicit `is_a` knowledge graph with Hearst patterns. Compare against the SKG. |

## Files in this folder

- `01_advil_moment.ipynb` — main notebook for Tutorial 1.
- `skg_viz.py` — reusable bar-chart + force-graph helpers. Imported by
  the notebook; designed to be reused across all four tutorials.
- `README.md` — this file.

## Mapping to Chapter 5 sections

| Tutorial | Sections covered |
|----------|------------------|
| 1 | §5.4.1, §5.4.2, §5.4.3, §5.4.4 |
| 2 | §5.4.5 |
| 3 | §5.4.7 |
| 4 | §5.3.1, §5.3.2, plus contrast with §5.4 |

## Conventions

Every tutorial follows the same arc, so a reader who does one knows what
to expect from the rest:

1. **The problem** — what keyword search alone gets wrong.
2. **The naive fix** — what you'd reach for first, and why it falls short.
3. **The chapter-5 fix** — derived from first principles.
4. **The wire format** — the raw Solr JSON, shown once and explained.
5. **The abstraction** — the same thing through `aips`.
6. **Visualize** — bar chart + graph view.
7. **Your turn** — a playground cell with knobs to twist.
8. **Discussion** — three or four "things worth pausing on".
9. **What's next** — pointer to the next tutorial.

If you find a place where the arc breaks down, that's a bug — file it.
