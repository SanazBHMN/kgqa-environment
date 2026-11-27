import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


query = (
    "[[Havainto::+]]"
    "[[Seuranta::!Testiseuranta]]"
    "[[Koordinaatit::+]]"
    "[[Päivämäärä::>2026-11-13]]"
    "[[SiteID::169565]]"
    "[[obsCode::ice||snow||temp||alg]]"
    "|?ObsCode|?Päivämäärä|?SiteID|?Koordinaatit"
    "|?DataJSON|?Display_fi|?Display_sv|?Display_en|?Ylläpito"
    "|sort=Päivämäärä|order=desc|limit=2000"
)

body = urlencode({
    "action": "ask",
    "query": query,
    "format": "json",
}).encode("utf-8")

request = Request("https://www.jarviwiki.fi/w/api.php",
                  data=body,
                  headers={
                      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                      "User-Agent": "LakeObservationResearchPrototype/0.1"
                  },
                  method="POST"
                  )

with urlopen(request, timeout=60) as response:
    result = json.load(response)


out = Path("notes/evidence")
out.mkdir(parents=True, exist_ok=True)
(out / "jarviwiki_ask_response_2026_11_27.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2)
)

print(json.dumps(result, ensure_ascii=False, indent=2))
