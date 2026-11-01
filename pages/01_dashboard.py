import streamlit as st, plotly.express as px
from models.sqlite_model import players,matches
from models.api_model import teams
from common.ui import report_controls
st.title("Resumen de rendimiento")
p=players(); m=matches(); t,source=teams()
a,b,c,d=st.columns(4); a.metric("Jugadores",len(p)); b.metric("Partidos",len(m)); c.metric("Puntos medios",round(p.points.mean(),1)); d.metric("Velocidad media",f"{p.top_speed_kmh.mean():.1f} km/h")
st.plotly_chart(px.bar(p,x="player",y="points",color="team",title="Puntos por jugador"),use_container_width=True)
st.subheader("Partidos recientes"); st.dataframe(m,use_container_width=True,hide_index=True)
st.subheader("Equipos (fuente API)"); st.caption(source); st.dataframe(t,use_container_width=True,hide_index=True)
st.subheader("Jugadores"); st.dataframe(p,use_container_width=True,hide_index=True)
report_controls("Resumen",p)
