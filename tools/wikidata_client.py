import requests

WDQA_API_URL = "https://query.wikidata.org/sparql"

HEADERS = {
    "User-Agent": "LUT-KGQA-Demo/1.0 (sanaz.bahmani@lut.fi)",
    "Accept": "application/sparql-results+json",
}

class SparqlQueryError(Exception):
    """Custom exception for SPARQL query errors."""


def run_sparql_query(query: str, timeout: int = 60) -> dict:
    if not query or not query.strip():
        raise SparqlQueryError("SPARQL query is empty.")

    try:
        response = requests.get(
            WDQA_API_URL,
            params={
                "query": query.strip(),
                "format": "json",
            },
            headers=HEADERS,
            timeout=timeout,
        )
    except requests.exceptions.Timeout as error:
        raise SparqlQueryError(f"SPARQL query timed out after {timeout} seconds: {error}") from error
    except requests.exceptions.RequestException as error:
        raise SparqlQueryError(f"Could not connect to Wikidata SPARQL endpoint: {error}") from error
    
    if response.status_code == 429:
        raise SparqlQueryError("Rate limit exceeded. Wait before making more requests.")
    
    if response.status_code >= 400:
        raise SparqlQueryError(f"Wikidata returned HTTP {response.status_code}: {response.text[:500]}")
    
    try:
        return response.json()
    except ValueError as error:
        raise SparqlQueryError(f"Wikidata returned a response that cannot be parsed as JSON: {error}") from error

def format_results(data: dict) -> list[dict]:
    """
    Convert a Wikidata SPARQL JSON response into a list of dictionaries.
    
    Ex:
        [{"lake": "http://www.wikidata.org/entity/Q12345", "lakeLabel": "Lake Saimaa"}]
    """
    bindings = data.get("results", {}).get("bindings", [])
    
    rows = []
    for binding in bindings:
        row = {}
        for variable, value in binding.items():
            row[variable] = value.get("value")
        rows.append(row)
        
    return rows

def run_query(query: str, timeout: int = 60) -> list[dict]:
    """
    Execute a query and return formatted results.
    """
    data = run_sparql_query(query, timeout=timeout)
    return format_results(data)