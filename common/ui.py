from io import BytesIO
from datetime import datetime
import streamlit as st
import streamlit.components.v1 as components
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
def report_controls(title,df):
    a,b=st.columns(2)
    with a: components.html('<button onclick="window.parent.print()" style="padding:10px;background:#10243a;color:white;border:0;border-radius:8px">🖨️ Imprimir página</button>',height=45)
    buf=BytesIO(); doc=SimpleDocTemplate(buf,pagesize=A4,rightMargin=1*cm,leftMargin=1*cm)
    sty=getSampleStyleSheet(); story=[Paragraph("SportLab | "+title,sty["Title"]),Spacer(1,10),Paragraph("Informe generado "+datetime.now().strftime("%d/%m/%Y %H:%M"),sty["Normal"]),Spacer(1,10)]
    data=[list(map(str,df.columns))]+[list(map(str,r)) for r in df.astype(str).itertuples(index=False,name=None)]
    t=Table(data,repeatRows=1); t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#10243a")),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),.4,colors.grey),("FONTSIZE",(0,0),(-1,-1),7)])); story.append(t); doc.build(story)
    with b: st.download_button("📄 Exportar resultados a PDF",buf.getvalue(),file_name=title.lower()+".pdf",mime="application/pdf",use_container_width=True)
