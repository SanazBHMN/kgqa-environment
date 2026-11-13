# Project instructions

This project is a Master's thesis prototype for graph-grounded question answering over Wikidate using LM Studio Bionic.

## Important rule

For questions about entities, facts, or relationships that can be answered from Wikidata, DO NOT search the web.

Instead, use the local Wikidata SPARQL client in:

tools/wikidata_client.py

The function to use is:

run_query(query)

It sends a SPARQL query to the Wikidata Query Service and returns a list of dictionaries.

## Required workflow

For every knowledge-graph question:

1. Identify the entities andWikidata properties needed.
2. Verify entity IDs before using them in SPARQL.
3. Generate a SPARQL query.
4. Call run_query(query)
5. Inspect the returned rows.
6. If the query fails, diagnose the error and repair it once.
7. If the result is empty, state that no matching data was found.
8. Produce a final answer using only the query results.
9. Show the SPARQL query and the supporting evidence.

## Output format

Always run:

### Answer

[answer]

### SPARQL query

```
sparql
[generated query]
```

### Evidence

- [Wikidata entity and relevant value]
- [Wikidata entity and relevant value]

### Execution status

- Query executed: yes/no
- Number of result rows: [number]
- Errors: [none or error message]

## Constraints

- Do not use web search for Wikidata-answerable questions.
- Do not invent QIDs or property IDs.
- Do not claim an answer is correct if the SPARQL query did not execute.
- Use LIMIT 20 while exploring.
