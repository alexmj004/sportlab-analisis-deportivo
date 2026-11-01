import requests, pandas as pd, streamlit as st
@st.cache_data(ttl=900,show_spinner=False)
def teams():
    try:
        r=requests.get("https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?l=English%20Premier%20League",timeout=5); r.raise_for_status()
        ts=r.json().get("teams") or []
        rows=[{"equipo":x.get("strTeam",""),"deporte":x.get("strSport",""),"estadio":x.get("strStadium") or "No disponible","país":x.get("strCountry") or "No disponible"} for x in ts[:30]]
        if rows: return pd.DataFrame(rows),"API externa TheSportsDB"
    except (requests.RequestException,ValueError,TypeError): pass
    return pd.DataFrame([{"equipo":"Arsenal","deporte":"Soccer","estadio":"Emirates Stadium","país":"England"},{"equipo":"Liverpool","deporte":"Soccer","estadio":"Anfield","país":"England"},{"equipo":"Manchester City","deporte":"Soccer","estadio":"Etihad Stadium","país":"England"}]),"respaldo local (API no disponible)"
@st.cache_data(ttl=300)
def simulator():
    import json
    from pathlib import Path
    return pd.DataFrame(json.loads((Path(__file__).resolve().parents[1]/"data"/"api_simulator.json").read_text(encoding="utf-8")))
