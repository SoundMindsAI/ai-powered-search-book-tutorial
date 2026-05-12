# 5. Putting It All Together: Smarter Search

Let's recap the journey. Five short paragraphs, one per section.

In Section 1 we said a knowledge graph is dots connected by lines, with real-world things and real-world relationships. We saw three ways to build one — by hand, by plugging in an existing one, or by autogenerating from your own content — and we said the rest of the chapter would be about that third option.

In Section 2 we said you don't need a separate graph database to build a graph. Every search engine already maintains two indexes: the inverted index (term → documents) and the forward index (document → terms). Composing those two lookups gives you a two-step graph traversal for free.

In Section 3 we looked at two ways to *extract* facts from text into an explicit knowledge graph. The grammar-based approach reads sentences and pulls out subject-predicate-object triples. The pattern-based approach (Hearst patterns) catches a specific kind of relationship — *is-a* — with high accuracy. Both work; both have trade-offs; both produce explicit graphs that live next to your content.

In Section 4 we saw a different idea: don't extract the facts in advance. Leave them in the text and let the engine *discover* relationships on the fly by comparing two distributions — the foreground (documents that match a query) and the background (the whole corpus). Words that are over-represented in the foreground are conceptually related to the query. The advil example: type *advil*, get back *motrin, aleve, ibuprofen*, no curation required.

And in this section, we'll pull all of that together into one picture and talk about what it lets you build.

## The whole chapter, on one page

[FIGURE: fig11_pipeline]

Start at the left. You have content — documents, posts, descriptions, whatever. You index it into a search engine that maintains both the inverted and forward indexes. That gives you a semantic knowledge graph for free, traversable at query time. With the graph in hand, you can rewrite queries to be smarter — expanding them with semantically related terms — and the resulting search results are dramatically better than what plain keyword matching would have produced.

Five boxes, four arrows. Each arrow is something this chapter walked you through.

The picture is intentionally simple. Real systems add steps — there's usually a query parser, a re-ranker, possibly a machine-learned scoring model, possibly a personalization layer. But you can hold the whole shape of Chapter 5 in your head without those.

## What this lets you do that you couldn't before

Three concrete capabilities.

**Find documents that don't contain the words people typed.** Plain keyword search can't find a document about *motrin* when someone types *advil*, no matter how relevant it is. A semantic-knowledge-graph-expanded search can. This is the most visible improvement and the easiest to demonstrate. It's also the one most directly tied to user satisfaction — people don't know your exact vocabulary, and they shouldn't have to.

**Build "more like this" recommendations from text alone.** No need to wait for users to click on things, no need to train an embedding model, no need to stand up a recommender service. The same indexes that power search also power recommendations, using the same primitives.

**Ask the corpus structured questions.** Beyond simple "related to" queries, you can use intermediate nodes — like the *in love with* example — to discover typed relationships that you never had to explicitly model. This is the most powerful and most under-used capability.

## What the book covers next

This chapter introduced the engine — both the semantic-knowledge-graph idea and the extraction techniques that complement it. The next chapters of *AI-Powered Search* build on that engine.

Chapter 6 talks about *learning domain-specific language* from user signals — what queries do people actually type, what do they correct themselves to, what alternate spellings show up, what phrases are people treating as units? Some of those answers come from analyzing the same indexes you've been seeing here, just from a different angle.

Chapter 7 puts the pieces together into a full query interpretation pipeline. A user types a query; the system parses it, expands it with related terms (using the semantic knowledge graph from this chapter), rewrites it into a form the engine can run, and returns results that are notably better than what raw keyword matching would have produced.

Chapters 8 through 12 cover *reflected intelligence* — using user signals (clicks, dwell time, search reformulations) to keep improving the ranking over time. The semantic knowledge graph plays a supporting role there too.

But the foundational trick — turn your search engine into a knowledge graph by exploiting its two indexes — is what you came for, and you have it.

## Three things to take with you

1. **Use what you have.** The search engine you may already have can do far more than match keywords. It's already a graph. Treat it as one.

2. **The corpus is the source of truth.** Semantically related terms don't have to come from a curated synonyms file. They come from how your content uses language. If you ever feel tempted to hand-build a synonyms list, ask first whether the corpus could just tell you.

3. **Relatedness is just statistics.** Don't be intimidated by the math. The whole trick is a comparison: how often does this word appear in the foreground compared to how often it appears in the background? That's it. Surprise is the signal.

You now have a complete mental model of Chapter 5. The next time someone says "we should add a knowledge graph to our search," you'll know what they mean — and you'll know whether you already have one.
