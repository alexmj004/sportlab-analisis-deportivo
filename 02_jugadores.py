import streamlit as st, plotly.express as px
from models.sqlite_model import players,matches
from models.api_model import teams
from common.ui import report_controls
st.title("Explorador de jugadores")
p=players(); m=matches(); t,source=teams()
team=st.selectbox("Equipo",["Todos"]+sorted(p.team.unique().tolist()))
minimum=st.slider("Puntos mínimos",int(p.points.min()),int(p.points.max()),int(p.points.min()))
f=p if team=="Todos" else p[p.team==team]; f=f[f.points>=minimum]
st.caption(f"SQLite + {source}; partidos consultados: {len(m)}")
st.dataframe(f,use_container_width=True,hide_index=True)
a,b=st.columns(2)
with a: st.plotly_chart(px.scatter(f,x="minutes",y="points",color="team",size="assists",hover_name="player",title="Minutos y puntos"),use_container_width=True)
with b: st.plotly_chart(px.bar(f,x="player",y="top_speed_kmh",color="team",title="Velocidad punta"),use_container_width=True)
st.subheader("Equipos de referencia"); st.dataframe(t,use_container_width=True,hide_index=True)
report_controls("Jugadores",f)
