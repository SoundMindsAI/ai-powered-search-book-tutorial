# Glossary

The terms we introduced, in one place, in plain English.

**Background.** In a relatedness query, the wider reference set — usually every document in your corpus. The yardstick we measure the foreground against.

**Distributional hypothesis.** The idea, going back to the 1950s, that words with similar meanings tend to appear in similar contexts. The intellectual foundation of the semantic knowledge graph.

**Edge.** A line in a graph. Connects two nodes. Usually has a label that describes the relationship. *(Lucy, is friends with, Charlie Brown)* uses *is friends with* as the edge.

**Foreground.** In a relatedness query, the smaller, query-specific set — the documents that match the starting query. We're interested in what's over-represented in the foreground compared to the background.

**Forward index.** A data structure inside a search engine that maps each document to the list of terms it contains. Sometimes called the *uninverted index* or *doc values*. Used here to walk from documents back to terms.

**Hearst pattern.** A linguistic template that reliably signals an *is-a* relationship in English text. Named after Marti Hearst, who described them in 1992. Examples: *"X such as Y and Z"*, *"X including Y and Z"*, *"Y and other X"*.

**Hypernym.** The more general thing in an *is-a* relationship. *Tool* is the hypernym of *hammer*.

**Hyponym.** The more specific thing in an *is-a* relationship. *Hammer* is a hyponym of *tool*.

**Inverted index.** A data structure inside a search engine that maps each unique term to the list of documents containing it. The reason keyword search is fast.

**Knowledge graph.** A graph whose nodes are real-world things and whose edges are meaningful relationships. Used to answer questions keyword search can't.

**Node.** A dot in a graph. Stands for *a thing*. Also called a *vertex*.

**Ontology.** A formal description of which kinds of nodes and edges are allowed in a domain. Think *schema* for knowledge.

**Query expansion.** Taking a user's query and adding semantically related terms to it before searching. The most common use of a semantic knowledge graph.

**RDF triple.** A fact written as *(subject, predicate, object)*. The plumbing of most explicit knowledge-graph formats. RDF stands for *Resource Description Framework*.

**Relatedness score.** A number that measures how over-represented a term is in the foreground compared to the background. High score: the term is conceptually related to the query. Near-zero: it's not.

**Semantic knowledge graph (SKG).** A way of traversing a search engine's indexes — at query time, with no precomputed graph — to discover related terms. The central trick of Chapter 5.

**Taxonomy.** A tree-shaped knowledge structure, usually built from *is-a* relationships. A simple but useful kind of knowledge graph.

**Triple.** Short for RDF triple. A three-part fact: *(subject, predicate, object)*.

**Vertex.** Same as node. Mathematicians use *vertex*; everyone else says *node*.


# Cheat sheet

If you remember nothing else from this chapter.

**A graph is dots and lines.** Nodes are things, edges are relationships. That's the whole vocabulary.

**A search engine is secretly a graph.** Its inverted index gives you term → documents. Its forward index gives you document → terms. Compose them and you can walk through your content as if it were a graph.

**You can extract facts from text two ways.** Grammar-based extraction (sentence → triple) is flexible but noisy. Hearst patterns (looking for "X such as Y") are accurate but only catch is-a relationships.

**You can also discover relationships on the fly.** Compare two distributions — foreground (docs matching a query) versus background (the whole corpus). Words over-represented in the foreground are semantically related. This is the semantic knowledge graph.

**Three things to do with related terms.** Expand queries to find documents that don't contain the exact words. Build content-based "more like this" recommendations. Use intermediate nodes to discover typed relationships you never modeled.

**Surprise is the signal.** Relatedness is a statistical measure of how surprised the engine should be to see a word in the foreground. Stopwords are unsurprising and get scored near zero. Real semantic siblings are surprising and get high scores. No synonym file required.
