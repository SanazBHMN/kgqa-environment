## Day 3 - Entity verification lesson

Initial query used wd:Q2123 for "Baltic Sea" which in fact refers to "Regina, Saskatchewan, Canada". Therefore, the empty result was expected and correct.

**Lesson**

Before generating SPARQL, the agent must verify the target entity's QID. An incorrect QID can produce a valid but semantically meaningless query.

**Corrected target**

Baltic Sea = Q545

**Corrected Query**

```
SELECT ?river ?riverLabel
WHERE 
{
    ?river wdt:P403 wd:Q545 . 

    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
LIMIT 50
```