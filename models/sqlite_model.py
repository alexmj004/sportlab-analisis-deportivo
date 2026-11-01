from pathlib import Path
import pandas as pd, sqlite3, streamlit as st
DB=Path(__file__).resolve().parents[1]/"data"/"sports.db"
@st.cache_resource
def conn(): return sqlite3.connect(DB,check_same_thread=False)
@st.cache_data(ttl=300)
def players(): return pd.read_sql_query("SELECT * FROM players ORDER BY points DESC",conn())
@st.cache_data(ttl=300)
def matches(): return pd.read_sql_query("SELECT * FROM matches ORDER BY match_date DESC",conn())
