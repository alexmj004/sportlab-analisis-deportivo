import os, streamlit as st
def login_form():
    st.subheader("Acceso a SportLab")
    with st.form("login"):
        u=st.text_input("Usuario"); p=st.text_input("Contraseña",type="password")
        ok=st.form_submit_button("Entrar",type="primary")
    if ok:
        if u==os.getenv("APP_USER","admin") and p==os.getenv("APP_PASSWORD","admin"):
            st.session_state["authenticated"]=True; st.session_state["username"]=u; st.rerun()
        else: st.error("Usuario o contraseña incorrectos.")
    st.info("Credenciales académicas: usuario **admin**, contraseña **admin**")
