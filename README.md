# SportLab — Análisis deportivo con Streamlit

## Funciones
- Login y sesión mediante `st.session_state` (práctica: admin/admin).
- Navegación lateral con Resumen, Jugadores y Partidos.
- SQLite como fuente SQL y API TheSportsDB como fuente externa, con fallback si falla Internet.
- Simulador JSON complementario, tablas, filtros, métricas y gráficos Plotly.
- Impresión desde navegador, exportación de tablas a PDF y caché Streamlit.

## Estructura
`.streamlit/`, `data/`, `models/`, `controllers/`, `common/`, `pages/`, `app.py`.

## Ejecutar
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
Abrir `http://localhost:8501`. Usuario `admin`, contraseña `admin`.

## Fuentes
`data/sports.db` contiene datos ficticios generados desde los CSV. La API externa es TheSportsDB; si no responde, la app presenta un conjunto de respaldo. El simulador JSON está en `data/api_simulator.json`. Los datos deportivos son demostrativos, no estadísticas oficiales.

## Publicación
Subir el proyecto a GitHub y crear una aplicación en Streamlit Community Cloud apuntando a `app.py`. Configurar `APP_USER` y `APP_PASSWORD` en Secrets. No se ha publicado desde aquí: el enlace público debe generarse desde una cuenta del usuario.

## Seguridad
El login simple cumple el enunciado académico, pero no es adecuado para producción. Para uso real se requiere autenticación robusta, contraseñas cifradas y gestión segura de secretos.
