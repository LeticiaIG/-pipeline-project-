from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.platypus.tables import TableStyle


def CreateCanvas():
    w,h = A4
    c = canvas.Canvas('Security.pdf', pagesize= A4)

    #nombre
    text_i= c.beginText(500, h - 40)
    text_i.setFont("Helvetica", 9)
    text_i.textLine("Leticia Izquierdo") 
    c.drawText(text_i)

    # title
    text_title = c.beginText(45, h - 80)
    text_title.setFont("Helvetica", 12)
    text_title.textLine("Crime in public space -Madrid.") 
    c.drawText(text_title)

    # subtitle
    text_r= c.beginText(45, h - 100)
    text_r.setFont("Helvetica", 10)
    text_r.textLine("Reporte de errores.") 
    c.drawText(text_r)

    #images
    c.drawImage("IMG2.png", 45, h - 300, 1970/3.8 , 668/3.8)
    c.drawImage("IMG3.png", 45, h - 500, 1970/3.8 , 668/3.8)
    c.drawImage("IMG5.png", 45, h - 700, 1970/3.8 , 668/3.8)

    c.showPage()

#PAGE 2 _PDF_

    #nombre
    text_i= c.beginText(500, h - 40)
    text_i.setFont("Helvetica", 9)
    text_i.textLine("Leticia Izquierdo") 
    c.drawText(text_i)

    #images
    c.drawImage("tabla_typeOfCrime.png", 40, h - 300, 1994/3.8 , 630/3.8)

    c.save()
    print(c)

CreateCanvas()
