from wikidata_client import run_query

#QUERY = """
#SELECT ?lake ?lakeLabel ?area ?unit ?unitLabel WHERE {
 # ?lake wdt:P17 wd:Q33 .
  #?lake wdt:P31/wdt:P279* wd:Q23397 .

  #?lake p:P2046 ?areaStatement .
  #?areaStatement psv:P2046 ?areaValue .
  #?areaValue wikibase:quantityAmount ?area ;
   #          wikibase:quantityUnit ?unit .

  #SERVICE wikibase:label {
   # bd:serviceParam wikibase:language "en".
  #}
#}
#LIMIT 10
#"""

QUERY = """
SELECT DISTINCT ?lake ?lakeLabel ?area ?unit ?unitLabel WHERE {
  ?lake wdt:P17 wd:Q33 .
  ?lake wdt:P31/wdt:P279* wd:Q23397 .

  ?lake p:P2046 ?areaStatement .
  ?areaStatement psv:P2046 ?areaValue .
  ?areaValue wikibase:quantityAmount ?area ;
             wikibase:quantityUnit ?unit .

  FILTER(?area > 100) .
  FILTER(STR(?unit) = "http://www.wikidata.org/entity/Q712226") .

  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en".
  }
}
ORDER BY DESC(?area)
LIMIT 10
"""

if __name__ == "__main__":
    try:
        rows = run_query(QUERY)
        print(f"query executed successfully")
        print(f"number of rows returned: {len(rows)}")
        
        print("\nfirst five rows:")
        for row in rows[:5]:
            print(row)
            
    except Exception as e:
        print(f"query failed with error: {e}")