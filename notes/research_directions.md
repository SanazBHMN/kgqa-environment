# Research Direction and Decision Log

This document records the reasoning behind the project's direction, technical investigations, and scope decisions.

It distinguishes verified progress from proposals and open questions. New entries should be dated. Earlier reasoning should be preserved, even if a later decision changes the direction.

## 24.11.2026 - Investigating lake observations as a research domain

### 1. Research context

The initial direction was to investigate question answering over a knowledge graph using a locally hosted LLM agent in LM Studio Bionic.

Possible research interests included:

- NL-to-SPARQL accuracy.
- Answer grounding in retrieved graph evidence.
- Whether graph grounding reduce unsupported answers compared with a suitable baseline.

The final research question, domain, architecture, and evaluation design have not yet been agreed.

Following the progress presentation, Antti supported the overall direction and considered Design Science Research suitable.

Antti suggested investigating Finnish lake conditions, particularly:

- Ice observations.
- Cyanobacterial observations.

He supplied Järvi-meriwiki examples, including the Haapanantien ranta observation site at Torankijärvi.

### 2. Why the original Python scripts were built

The existing scripts establish a controlled execution path between Bionic and a structured data source.

Verified path:
Bionic -> shell -> Python runner -> Wikidata client -> public Wikidata

The purpose was to establish that queries could be executed and results or errors returned before evaluating the agent's query generation.

This separation matters because a failed answer could arise from:

- Incorrect entity or property selection.
- An incorrect query.
- A network or endpoint failure.
- Incorrect interpretation of retrieved results.

The scripts are supporting research infrastructure. Building a connector alone is not the intended research contribution.

Current limitations:

- Most queries were supplied or corrected manually.
- Independent NL-to-SPARQL performance has not been evaluated.
- The current source is public Wikidata, not a private Wikibase.
- Retrieved facts have not been independently validated.

### 3. Why investigate Järvi-meriwiki?

Whe immediate purpose is to determine whether Antti's suggested domain provides accessible, understandable data suitable for abounded QA study.

This is a feasibility investigation, not a commitment to a final architecture or thesis topic.

The question guiding this phase is:

"Can we obtain and correctly interpret a small set of lake observations that could support evidence-grounded question answering?"

Järvi-meriwiki and Wikidata must be treated as separate sources. Finding observations in Järvi-meriwiki does not establish that those observations are available through Wikidata.

### 4. What has been observed so far

Observation site:

- Name: Haapanantien ranta
- Lake: Torankijärivi (74.031.1.023)
- Site ID. 169565

The ice-season chart offers a CSV download containing:

- Winter season
- Observation type
- Value
- Value type or unit
- Additional information
- Photograph
- Observer status

The CSV contains freeze-up dates, ice-free dates, and some ice-season duration. Not all seasons have every observation type.

Browser network inspection also revealed structured responses with:

- Site details
- An ice observation
- Archived algal observations
- A temperature observation

One ice record explicitly labels its event:
"Beginning of ice over period", dated 13 November 2026

The record also contains:
{ "cat": "2", "val": 1, "unit": "cm" }

The meaning of these numeric fields has not been established.
Do not interpret this record as a verified 1 cm thickness measurement.

Ice-season observations must not be treated as evidence that ice is safe travel.

### 5. Captured browser request

Endpoint: https://www.jarviwiki.fi/w/api.php

Method: POST

Payload:

- action: ask
- format: json
- query:
  [[Havainto::+]][[Seuranta::!Testiseuranta]][[Koordinaatit::+]][[Päivämäärä::>2026-11-13]][[SiteID::169565]][[obsCode::ice||snow||temp||alg]]|?ObsCode|?Päivämäärä|?SiteID|?Koordinaatit|?DataJSON|?Display_fi|?Display_sv|?Display_en|?Ylläpito|sort=Päivämäärä|order=desc|limit=2000

This is an action=ask request, not a SPARQL query.

Important limitations:

- The query includes several observation codes, not only ice.
- It has a date filter and a result limit.
- It does not establish access to the complete historical dataset.
- Exact date-boundary behaviour needs checking.

Evidence file: Jääpeitekauden kesto_SiteID-169565_Downloaded-2026-11-23.csv

### 6. Proposed decision: test retrieval separately

Next proposed action:
Reproduce one captured POST request in a standalone Python script.

Reason:
Determine whether a program we control can retrieve the same structured observation as the browser.

Keep this separate from the working Wikidata client because it:

- Preserves the existing prototype
- Separates data-access problems from LLM behaviour
- Avoids premature integration

### 7. Tentative research destination

"Design and evaluate a local LLM-based QA system that answers a limited set of questions about lake observations using traceable structured evidence."

This is a working direction, not an approved research question.

Possible answer requirements:

- Identify the observation site
- State the observation date or season
- Report the relevant event or measurement
- Preserve source information
- Distinguish missing evidence from a negative observation
- Avoid unsupported conclusions

### 8. Architecture decisions still open

Option 1: Query the observation source directly.
The agent would use a retrieval tool, potentially alongside a separate Wikidata tool for lake information

Option 2: Import selected observations into a small knowledge graph.
The system would answer questions over that graph.

No decision has been made to build a private Wikibase.

The architecture must follow the research contribution:

- If the focus remains NL-to-SPARQL, direct ask-API retrieval alone does not evaluate that capability.
- If the focus becomes evidence-grounded QA across structured sources, direct retrieval may serve a different role.

A graph-versus-vector comparison is also not yet committed.
