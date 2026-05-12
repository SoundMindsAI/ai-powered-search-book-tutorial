# 3. Teaching a Computer to Read Between the Lines

Sometimes you don't want to *infer* relationships from your text. You want to *extract* them, cleanly and explicitly, and store them in your knowledge graph as crisp little facts.

A fact, in this world, is a tiny three-part thing. It has a *subject*, a *predicate* (the relationship), and an *object*.

[FIGURE: fig06_sentence_triple]

"Lucy is friends with Charlie Brown" becomes the fact `(Lucy, "is friends with", Charlie Brown)`. Three parts. Two nodes and the edge between them. People in the knowledge-graph world call this a *triple* — three parts, hence the name. You'll also see it called an *RDF triple*, where RDF stands for "Resource Description Framework," which is the name of an old web standard for writing facts like this down. Don't be intimidated by the acronym. A triple is just *(thing, relationship, thing)*.

The question of this section is: how do you turn a sea of text into a pile of triples? Two main techniques, with very different trade-offs.

## Technique 1: Read the grammar

The first technique is to teach the computer to read like a third-grader doing sentence diagrams.

Every English sentence has parts of speech. There's usually a subject (who or what the sentence is about), a verb (what they're doing), and often an object (what they're doing it to). A natural-language processing library, like spaCy, can parse a sentence and identify these parts automatically. Once you know which word is the subject and which is the object, you have your triple.

Here's the rough flow:

1. Take a sentence.
2. Have an NLP library label every word with its part of speech.
3. Identify the subject, verb, and object.
4. Output `(subject, verb, object)`.

This works beautifully on simple sentences. *"Data scientists build machine learning models."* The subject is *data scientists*, the verb is *build*, the object is *machine learning models*. Triple: `(data scientists, build, machine learning models)`. Done.

It works less well on messy sentences. Pronouns get in the way (*"They also write code"* — they who?). Complex sentences with multiple clauses produce noisy triples. Verbs come in many forms: *build, building, built, builds, will build* — the same relationship, five different surface words. Synonyms are even worse: *build, create, develop, construct, make, write* might all mean the same thing in context, but the extraction process treats them as separate edge types.

> **Warning.** When you extract facts this way, the cleanliness of the result depends heavily on how much you cleaned up the text first. Pronouns need to be resolved (replace *they* with what *they* refers to). Verbs need to be normalized (treat *build*, *built*, and *building* as the same edge). Even with all that, you'll get noise. This is fine if the next step is some kind of aggregation or fuzzy match. It's painful if you need the output to be database-clean.

Grammar-based extraction is flexible — it can pull out any kind of relationship the text describes — but it's noisy. Modern systems often use larger language models to do this more accurately. The trade-off is the same: more flexibility, more noise.

## Technique 2: Look for specific patterns

The second technique sidesteps the noise problem by focusing on just one kind of relationship.

It turns out that one specific relationship is unusually well-behaved in English: the *is-a* relationship. Whenever you say one thing is a kind of another thing, English provides surprisingly few, surprisingly consistent ways to say it. A linguist named Marti Hearst noticed this in 1992 and wrote down the patterns.

[FIGURE: fig07_hearst_pattern]

Here are some of those patterns, in plain English:

*"Tools, such as hammers and screwdrivers, ..."* → hammer is_a tool, screwdriver is_a tool.

*"Vegetables including carrots, broccoli, and spinach"* → carrot is_a vegetable, etc.

*"Hammers and other tools"* → hammer is_a tool.

*"Carrots, broccoli, spinach, and other vegetables"* → carrot is_a vegetable, etc.

*"Phillips heads are a type of screwdriver"* → phillips head is_a screwdriver.

There are about fifty of these patterns in total. Together they catch most of the ways English speakers express *is-a* relationships in writing.

Run those patterns over enough text and you get back a clean, fairly accurate, *is-a* graph. Sometimes called a *taxonomy*. You can use it to answer "what kind of X is this?" or "what are all the X's mentioned in our documents?" — exactly the kinds of questions a category-based search needs.

> **Tip.** Hearst patterns work best on text where authors are actively trying to be informative — encyclopedias, forum posts, product descriptions. They work poorly on tweets, chat logs, and casual conversation, where people skip the explicit *is-a* phrasings ("I just got an iPhone" doesn't tell you an iPhone is a phone — but every product page on Apple's site does).

### Hyponym and hypernym — two words you'll see

Two words you'll see in this corner of the world:

A **hyponym** is the more specific thing. *Hammer* is a hyponym of *tool*. *Carrot* is a hyponym of *vegetable*. *Advil* is a hyponym of *medication*.

A **hypernym** is the more general thing. *Tool* is a hypernym of *hammer*. *Vegetable* is a hypernym of *carrot*. *Medication* is a hypernym of *advil*.

(There's a third word, *meronym*, for part-of relationships, like "wheel is a meronym of car." That one's less common, and we won't use it.)

Hearst patterns are essentially a hyponym-extractor. They specifically find pairs of words in an is-a relationship and produce a cleaned-up list of them.

## Two techniques, two trade-offs

Both techniques produce real facts. Both have their place.

The grammar-based technique gives you breadth: any kind of relationship you can name. The catch is noise — you'll spend real effort cleaning up the output before you can use it.

The pattern-based technique gives you cleanliness, but only for one relationship type. If you only ever needed is-a, you'd be perfectly happy. Most real systems need more.

Either way, both techniques have one big property in common: they *take the facts out of the text* and put them somewhere else, as discrete edges in a graph. That's useful, but it's lossy. You lose the surrounding context. You lose the nuance of *how* the document said something. And every fact in your graph is a fact you committed to in advance, whether or not anyone ever asked a question that needed it.

The next section shows a different, more flexible approach. Instead of extracting facts up front, we leave the facts in the text and let the search engine *discover* relationships on the fly, in response to whatever question someone asks. It turns out to be enormously powerful.

> **Remember.** Up-front extraction (this section) and on-the-fly discovery (next section) aren't competitors. They're complementary. Many real systems do both — extract the most important, stable facts as explicit edges, and let everything else fall out of relatedness scoring at query time.
