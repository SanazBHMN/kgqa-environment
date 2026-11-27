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

## Day 3 - Client validation complete

### Finnish lakes

- Query executed successfully
- Returned 10 rows
- Each row contained both `lake` and `lakeLabel`

### Baltic rivers

- Query executed successfully
- Returned 10 rows
- Confirmed that Q545 is the Baltic Sea
- Confirmed that P403 points from a river to the water body it drains into

### Finnish lakes without limit

- Query executed successfully
- Returned 17,878 rows
- No lables here - the query only selects `?lake`
- Demonstrated that result size can become large without specifying `LIMIT`

### Invalid query

- Client raised `SparqlQueryError`
- Wikidata returned HTTP 400
- Error indicated a malformed SPARQL query and a missing closing brace
- Test explicitly verified that the expected exception was raised

### Empty result

- Query executed successfully
- Returned zero rows
- Confirmed that an empty result is not an execution error

## Day 3 Entity Verification Lesson

Initial query used wdt:Q2123 for "Baltic Sea" which in fact refers to "Regina, Saskatchewan, Canade". Therefore, the empty result was expected and correct.

**Lesson**

Before generating SPARQL, the agent must verify the target entity's QID. An incorrect QID can produce a valid but semantically meaningless query.

**Corrected target**

Baltic Sea = Q545

**Corrected query**

```
SELECT ?river ?riverLabel
WHERE
{
    ?river wdt:P403 wd:Q545 .

    SERVICE wikibase:label { bd:serviceParam wikibase:languages "en". }
}
LIMIT 50
```

## Day 4 - Client validation complete

### Finnish lakes

- Query executed successfully
- Returned 10 rows
- Each row contained both `lake` and `lakeLabel`

### Baltic rivers

- Query executed successfully
- Returned 10 rows
- Confirmed that Q545 is the Baltic Sea
- Confirmed that P403 points from a river to the water body it drains into

### Finnish lakes without limit

- Query executed successfully
- Returned 17,878 rows
- No labels here - the query only selects `?lake`
- Demonstrated that result size can become large without specifying `LIMIT`

### Invalid query

- Client raised `SparqlQueryError`
- Wikidata returned HTTP 400
- Error indicated a malformed SPARQL query and a missing closing brace

### Empty result

- Query executed successfully
- Returned zero rows
- Confirmed that an empty result is not an execution error

### Day 3 status

The Wikidata client is ready for Bionic integration

## 2026-11-27 - Järvi-meriwiki ask API retrieval test

Purpose:

Check whether a standalone Python script can reproduce the browser's action=ask request for site 169565.

Script: tools/test_jarviwiki.py
Method: POST to https://jarviwiki.fi/w/api.php (action=ask, format=json)

Result:
Request succeeded. count = 1. Record: ObsCode "ice", SiteID 169565,
date 2026-11-13 9:00, Display_en "Beginning of ice cover period".
Matches the browser response captured on 2026-11-23.

Not established:

- Historical coverage (query filters by date)
- Meaning of DataJSON {"cat": "2", "val": 1, "unit": "cm"}
- Whether the maintainer's observations are reliable.

Evidence: notes/evidence/jarviwiki_ask_response_2026_11_27.json
