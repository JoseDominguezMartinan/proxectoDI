from reportlab.platypus import (SimpleDocTemplate, PageBreak,

                                Spacer, Table, TableStyle, Paragraph, Image)


from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.pagesizes import A4

from reportlab.lib import colors
from reportlab.lib.units import inch

from baseDatos import metodosBase

from PyPDF2 import PdfFileMerger,PdfFileReader
class informeAlbaran():

    def crear_factura(self,numVenta,matricula,dni,fecha):

        try:
            coche=metodosBase.metodosBase.listar_coches_matricula(self,matricula)
            marca=coche[0][1]
            modelo=coche[0][2]
            kilometraje=coche[0][3]
            ano=coche[0][4]
            precio=coche[0][5]
            clase=coche[0][6]
            automatico=coche[0][7]
            motor=coche[0][8]
            caballos=coche[0][9]


            cliente=metodosBase.metodosBase.listar_clientes_dni(self,dni)
            nome=cliente[0][1]
            fechaNac=cliente[0][2]
            telefono=cliente[0][3]
            direccion=cliente[0][4]
            codPostal=cliente[0][5]




            detalleFactura = []
            detalleCoche=[]
            facturas = []
            coches=[]
            follaEstilo=getSampleStyleSheet()
            imagen = Image('/home/hansen/PycharmProjects/projectCompraVenta/platy/logo.png', 1 * inch, 1 * inch)

            detalleFactura.append(['Factura:', numVenta, '', ''])
            detalleFactura.append(['DNI:',  dni, '', ''])
            detalleFactura.append(['Nombre:', nome, 'Nacido:', fechaNac])
            detalleFactura.append(['Telefono:', telefono, 'Direccion:', direccion])
            detalleFactura.append(['Fecha:',  fecha,'Cod.postal:', codPostal])

            detalleCoche.append(['Matricula:',  matricula, 'Marca', marca])
            detalleCoche.append(['Modelo:', modelo, 'Km', kilometraje])
            detalleCoche.append(['Año:', ano, 'Precio', precio])
            detalleCoche.append(['Clase:', clase, 'Automatico', automatico])
            detalleCoche.append(['Motor:', motor, 'Caballos', caballos])

            facturas.append(list(detalleFactura))
            coches.append(list(detalleCoche))

            detalleFactura.clear()
            nombreFactura= "factura %d .pdf" % ( numVenta)

            doc = SimpleDocTemplate(nombreFactura, pagesize=A4)

            guion = []


            for factura in facturas:

                taboa = Table(factura, colWidths=120, rowHeights=30)

                taboa.setStyle(TableStyle([

                    ('BOX', (0, 0), (-1, -1), 0, colors.black),
                    ('FONTSIZE', (0, 0), (-1, -1), 8),

                ]))

                for coche in coches:
                    taboa2 = Table(coche, colWidths=120, rowHeights=30)

                    taboa2.setStyle(TableStyle([

                        ('BOX', (0, 0), (-1, -1), 1, colors.black),
                        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.grey),
                        ('BACKGROUND', (0, 0), (-1, -1), colors.lightcyan),


                    ]))


            cabeceira = follaEstilo['Heading4']  # formato por defecto
            cabeceira2 = follaEstilo['Normal']  # formato por defecto
            cabeceira.pageBreakBefore = 0  # con un uno a primeira folla queda en branco
            cabeceira.keepWitNext = 0  # para que non nos deixe a primeira paxina en branco
            cabeceira.backColor = colors.lightcyan
            parrafo = Paragraph("Recibo de venta simplificado", cabeceira)
            parrafo2 = Paragraph("  COCHESJOSE.SL CARRETERA INFINITA S/N "+
                                "  VIGO", cabeceira2)
            parrafo3=Paragraph("    GRACIAS, HASTA LA PROXIMA , TELEFONO:986505050", cabeceira2)
            guion.append(parrafo)
            guion.append(Spacer(0, 40))

            guion.append(imagen)
            guion.append(Spacer(0, 10))
            guion.append(parrafo2)
            guion.append(taboa)


            guion.append(Spacer(0, 40))
            guion.append(taboa2)

            guion.append(Spacer(0, 40))
            guion.append(parrafo3)
            guion.append(Spacer(0, 40))
            guion.append(PageBreak())

            doc.build(guion)


            merger = PdfFileMerger()
            merger.append(PdfFileReader(open(nombreFactura, 'rb')))


            return True

        except:
            return False
