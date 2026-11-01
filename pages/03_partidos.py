import streamlit as st, plotly.express as px
from models.sqlite_model import players,matches
from models.api_model import teams,simulator
from common.ui import report_controls
st.title("Análisis de partidos")
m=matches(); p=players(); t,source=teams(); sim=simulator()
season=st.selectbox("Temporada",["Todas"]+sorted(m.season.unique().tolist()))
f=m if season=="Todas" else m[m.season==season]
st.caption(f"SQLite: {len(m)} partidos · {source} · simulador JSON: {len(sim)} registros")
st.dataframe(f,use_container_width=True,hide_index=True)
a,b=st.columns(2)
with a: st.plotly_chart(px.bar(f,x="opponent",y=["goals_for","goals_against"],barmode="group",title="Goles a favor y en contra"),use_container_width=True)
with b: st.plotly_chart(px.line(f,x="match_date",y="goals_for",markers=True,title="Goles a favor por fecha"),use_container_width=True)
st.subheader("Equipos consultados"); st.dataframe(t,use_container_width=True,hide_index=True)
st.subheader("Simulador JSON"); st.dataframe(sim,use_container_width=True,hide_index=True)
report_controls("Partidos",f)
