# Chapter 5 — Plain English Edition

A friendly, five-notebook walk through Chapter 5 of *AI-Powered Search*
("Knowledge graph learning"), written in the spirit of the *For Dummies*
series — clear, conversational, analogy-first, with code in a supporting
role rather than the lead.

## Who this is for

- Product managers, designers, analysts, and other tech-curious folks
  who want to understand how knowledge graphs make search smarter,
  without becoming a search engineer first.
- Engineers from other disciplines (frontend, mobile, data) who want a
  gentle on-ramp before diving into the book's denser sections.
- Anyone who's tried to read Chapter 5 once and bounced off the math.

If you're already comfortable with inverted indexes, BM25, and JSON
faceting, you probably want the more technical track in
[`tutorials/chapter-5/`](../chapter-5/) instead. The two tracks cover
the same material at very different altitudes.

## How to read these

Each notebook is a self-contained explanation of one section of the
book's Chapter 5. You can read them in order or jump to whichever one
sounds most useful right now.

- The prose carries the explanation. Most cells are text.
- A small number of code cells produce a picture or a vivid demo. You
  click the ▶️ button, look at the output, move on. You don't have to
  understand the code.
- Every notebook ends with a one-paragraph **cheat sheet** and a
  **glossary**.

## What you'll need

- Notebooks 1, 2, and 3: just Python with `networkx`, `matplotlib`, and
  `spacy` available. Runnable on your laptop or in any Jupyter
  environment. No Docker.
- Notebooks 4 and 5: the full book Docker stack from
  [`../SETUP.md`](../SETUP.md). The shift happens because those
  notebooks need a real search engine with real data indexed in it.

We'll remind you of this at the top of each notebook.

## The five notebooks

| # | Section | Title | Needs Docker? |
|---|---------|-------|---------------|
| 1 | §5.1 | [Knowledge Graphs: Connecting the Dots](01_connecting_the_dots.ipynb) | No |
| 2 | §5.2 | *(planned)* Your Search Engine Already Knows More Than You Think | No |
| 3 | §5.3 | *(planned)* Teaching a Computer to Read Between the Lines | No |
| 4 | §5.4 | *(planned)* Finding Hidden Connections in Your Words | Yes |
| 5 | §5.5 | *(planned)* Putting It All Together: Smarter Search | Yes |

## Style conventions

Every notebook follows the same beats so the rhythm is predictable:

1. **In this notebook** — what you'll learn (4–6 bullets).
2. **An everyday analogy** — connect the topic to something familiar.
3. **The concept in plain English** — what's going on.
4. **A small visible demo** — usually a picture or a short table.
5. **🤓 Technical Stuff** — a skippable sidebar for the curious.
6. **Cheat sheet** — three things to remember.
7. **Glossary** — vocabulary you'll see again later.
8. **Up next** — a one-paragraph teaser for the next notebook.

Callout icons you'll see throughout:

- 💡 **Tip** — practical advice
- ⚠️ **Warning** — common pitfalls
- 🤓 **Technical Stuff** — skippable deep dives
- 🎯 **Remember** — one-line takeaways

## Relationship to the other track

If you're curious how this material gets applied at the engineering
level — exact API calls, JSON wire formats, performance trade-offs —
the parallel track in [`tutorials/chapter-5/`](../chapter-5/) walks
through the same concepts for a search engineer audience. You can read
both. The plain-English track gives you the *why*; the technical track
gives you the *how*.
