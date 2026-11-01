import streamlit as st
from common.auth import login_form
st.set_page_config(page_title="SportLab",page_icon="⚽",layout="wide")
st.markdown("""<style>[data-testid="stSidebar"]{background:#10243a} [data-testid="stSidebar"] *{color:#fff} div[data-testid="stMetric"]{background:#f2f6fa;padding:12px;border-radius:10px}</style>""",unsafe_allow_html=True)
st.title("⚽ SportLab | Análisis deportivo")
st.caption("Dashboard interactivo de rendimiento")
if not st.session_state.get("authenticated",False):
    login_form(); st.stop()
p1=st.Page("pages/01_dashboard.py",title="Resumen",icon="📊",default=True)
p2=st.Page("pages/02_jugadores.py",title="Jugadores",icon="🏃")
p3=st.Page("pages/03_partidos.py",title="Partidos",icon="⚽")
pg=st.navigation([p1,p2,p3])
with st.sidebar:
    st.caption("Sesión: "+st.session_state.get("username","admin"))
    if st.button("Cerrar sesión"): st.session_state.clear(); st.rerun()
pg.run()
