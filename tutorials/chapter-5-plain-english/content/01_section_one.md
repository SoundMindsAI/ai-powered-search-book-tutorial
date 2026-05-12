# 1. Knowledge Graphs: Connecting the Dots

If you've ever drawn a family tree, you've made a knowledge graph.

You drew little circles or boxes for each person. You drew lines between them to show how they're related — *is the parent of*, *is married to*, *is the sibling of*. You probably didn't think of yourself as building a graph database. But that's what you were doing. A graph is just dots connected by lines. A knowledge graph is the same idea, but the dots stand for real things in the world and the lines stand for real relationships between them.

You've seen these graphs in action many times even if you haven't named them.

When you search for a movie on Google and a panel appears on the right with the director, the cast, the year, the budget, the box office, the studio — that's coming from a knowledge graph. Each fact is a line between two dots.

When Netflix suggests "because you watched *X*, you might like *Y*," there's a graph in the background mapping movies to other movies, to actors, to themes, to viewers. A traversal through that graph is what produced the recommendation.

When LinkedIn says "people you may know," it's not magic. It's a graph of who knows whom, walked one or two steps out from your name.

The trick this chapter is about is a particular kind of knowledge graph: one that a search engine builds for itself, automatically, from the documents you already have. By the end of the chapter you'll see why that's a much bigger deal than it sounds.

But first, let's nail down what a graph actually is.

## The two pieces of every graph

Every graph in the world is made of just two things.

**Nodes.** Sometimes called *vertices* (because mathematicians like to give simple things long names). A node is *a thing*. A person, a place, a movie, a word, a concept, a product, a paper, a recipe, a date — it doesn't matter what. If you can name it, it can be a node.

**Edges.** An edge is *a relationship between two things*. It connects two nodes and usually has a label that says how they're related. *is the parent of*, *contains*, *was directed by*, *was published in*.

That's all the vocabulary you need to start. Here's a small graph drawn with just those two pieces.

[FIGURE: fig01_sample_kg]

Read it like a sentence. Star Wars features Luke. Star Wars features Leia. Luke lives on Tatooine. Mark Hamill plays Luke. Luke is a sibling of Leia.

Five facts, five edges, five nodes. You could keep going forever. Add Han Solo, the Millennium Falcon, the Death Star, every movie in the franchise, every actor in every movie, the years they came out, the directors, the cinematographers. The graph just gets bigger. It doesn't get more complicated. It's still nodes and edges.

> **Tip.** When you read about a knowledge graph that has "a billion edges" or "100 million nodes," don't be intimidated. It's the same Luke-and-Leia idea, scaled up. The hard problem isn't drawing the graph — it's deciding which nodes and edges should exist in the first place.

## When a graph becomes a knowledge graph

Not every graph is a knowledge graph.

A road map is a graph. The intersections are the nodes, the streets are the edges. But we wouldn't usually call a road map a "knowledge graph" — its job is to help you navigate, not to capture facts about how the world fits together.

The wiring diagram of a microwave is a graph. The components are the nodes, the wires are the edges. Again, useful, but not a knowledge graph.

The shift is fuzzy, but in practice a graph becomes a *knowledge* graph when:

1. The nodes stand for real-world things people can name — people, products, ideas, places.
2. The edges describe meaningful relationships — *is a*, *wrote*, *married to*, *located in*, *contains*.
3. You can use the graph to answer questions you couldn't easily answer otherwise.

That third part is the punchline. The reason anyone bothers building one of these is to answer questions that flat-text search can't. Questions like:

*Show me drugs that work the same way as advil.*

*What other movies are in the Marvel Cinematic Universe?*

*Who else in our company has worked with this client?*

A keyword search engine, by default, doesn't know that advil and motrin are related — they're just two different sequences of characters. A knowledge graph does know, because someone (or some automated process) drew a line between them.

## Three ways to build a knowledge graph

If you want a knowledge graph for your own product, there are three main paths.

[FIGURE: fig02_three_ways]

**Option 1: By hand.** You sit down with someone who knows the domain — a doctor, a lawyer, a librarian, an experienced product manager — and you type in every node and every edge. This is slow. It's expensive. It produces beautiful, precise graphs that nobody can argue with, and they're outdated the moment you stop maintaining them. Specialized industries that need very high accuracy (medical coding, legal taxonomies, drug interaction databases) do exactly this. It's the right tool when the cost of a wrong edge is high and the world doesn't change too fast.

**Option 2: Plug in an existing one.** Several large knowledge graphs already exist, built by other people. Wikipedia has a structured-fact cousin called Wikidata. There's ConceptNet, full of common-sense connections between everyday concepts. And, increasingly, large language models themselves act like implicit knowledge graphs — you can ask them, in plain English, what's related to what. The advantage is speed: you get a huge graph for free. The catch is that these graphs don't know about *your* domain. They won't know your product names, your customer segments, your internal jargon, the words your users actually type into your search bar.

**Option 3: Have the search engine build one for you.** Feed your own documents to a search engine and let it work out the relationships from the text itself. This is the option this chapter is about. The advantage: it knows about *your* terminology, it updates itself as new documents arrive, and it's free in the sense that you already have the documents and the search engine. The catch: it depends on having enough content. A graph built from three documents won't be very useful. A graph built from three million might be excellent.

> **Remember.** These three options aren't mutually exclusive. The most powerful real-world systems combine all three — autogenerate the bulk of the graph from content, plug in a public graph for common-sense facts, and sprinkle in hand-curated edges where accuracy really matters.

## Where this chapter is heading

The rest of the chapter is about Option 3. Each section adds one piece:

- Section 2 shows that you don't actually need a separate graph database. The search engine you may already have is, in a real sense, a graph database in disguise.
- Section 3 shows two techniques for pulling structured facts out of plain text — useful if you want a clean, explicit knowledge graph as a side effect of your indexing.
- Section 4 shows a different, more powerful idea: leave the facts in the text and let the engine discover relationships on the fly, every time someone searches.
- Section 5 ties it together — how the pieces fit, and what they let you build that you couldn't before.

By the end you'll have a clear mental model of one of the most useful tricks in modern search.
