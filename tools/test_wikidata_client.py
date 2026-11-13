from wikidata_client import run_query, SparqlQueryError

QUERIES = {
    "finnish_lakes": """
        SELECT ?lake ?lakeLabel WHERE {
          ?lake wdt:P17 wd:Q33 .
          ?lake wdt:P31/wdt:P279* wd:Q23397 .
          SERVICE wikibase:label {
            bd:serviceParam wikibase:language "en".
          }
        }
        LIMIT 10
    """,
    "baltic_rivers_direct": """
        SELECT ?river ?riverLabel WHERE {
          ?river wdt:P403 wd:Q545 .
          SERVICE wikibase:label {
            bd:serviceParam wikibase:language "en".
          }
        }
        LIMIT 10
    """,
    "finnish_lakes_no_limit": 
        """
        SELECT ?lake WHERE {
          ?lake wdt:P17 wd:Q33 .
          ?lake wdt:P31/wdt:P279* wd:Q23397 .
          SERVICE wikibase:label {
            bd:serviceParam wikibase:language "en".
          }
        }
    """,
    "invalid_query": """
        SELECT ?lake WHERE {
          ?lake wdt:P17 wd:Q33 .
          ?lake wdt:P31/wdt:P279* wd:Q23397 .
        """,
}


def main():
    for name, query in QUERIES.items():
        print(f"\n=== {name} ===")

        try:
            rows = run_query(query)

            print(f"Returned {len(rows)} row(s).")

            for row in rows[:3]:
                print(row)

        except SparqlQueryError as error:
            print(f"Query failed: {error}")

def test_unit_filter_str_comparison():
    query = """
    SELECT ?lake ?area WHERE {
      ?lake wdt:P17 wd:Q33 .
      ?lake wdt:P31/wdt:P279* wd:Q23397 .
      ?lake p:P2046 ?areaStatement .
      ?areaStatement psv:P2046 ?areaValue .
      ?areaValue wikibase:quantityAmount ?area ;
                 wikibase:quantityUnit ?unit .
      FILTER(STR(?unit) = "http://www.wikidata.org/entity/Q712226")
      FILTER(?area > 100)
    }
    LIMIT 5
    """
    rows = run_query(query)
    assert len(rows) > 0

def test_empty_result():
    query = """
        SELECT ?item ?itemLabel WHERE {
          ?item wdt:P403 wd:Q2123 .
          SERVICE wikibase:label {
            bd:serviceParam wikibase:language "en".
          }
        }
        LIMIT 10
    """

    rows = run_query(query)
    print(f"\nEmpty-result test returned {len(rows)} row(s).")
    assert len(rows) == 0
    
def test_invalid_query():
    try:
        run_query(QUERIES["invalid_query"])
        raise AssertionError("Expected SparqlQueryError for malformed SPARQL, but no error was raised.")
    except SparqlQueryError as error:
        print(f"\nInvalid-query test passed. Caught expected error: {error}")


if __name__ == "__main__":
    main()
    test_empty_result()
    test_invalid_query()