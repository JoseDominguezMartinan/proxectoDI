from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.legends import Legend
from baseDatos import metodosBase
import random
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.widgets.markers import makeMarker

class informeVentas():

    def crear_informe(self):
        guion = []
        d = Drawing(300, 200)

        tarta = Pie()
        tarta.x = 65
        tarta.y = 15
        tarta.width = 170
        tarta.height = 170

        tarta.data = []
        tarta.labels = []
        cores = []
        follaEstilo = getSampleStyleSheet()
        _HEX = list('0123456789ABCDEF')
        j=False
        ventasMarca=metodosBase.metodosBase.listar_ventas_marca(self)

        for ventaMarca in ventasMarca:
            tarta.data.append(ventaMarca[0])
            tarta.labels.append(ventaMarca[1])

            color = '#' + ''.join(_HEX[random.randint(0, len(_HEX)-1)] for _ in range(6))
            cores.append(colors.HexColor(color))
            if ((tarta.data[0] is not None) and j==False):
                mayor = tarta.data[0]
                indice=0
                j=True
            else:
                if(ventaMarca[0]>=mayor):
                    mayor=ventaMarca[0]




        tarta.slices.strokeWidth = 0.2  # anchura das liñas
        tarta.sideLabels = 1
        tarta.slices[tarta.data.index(mayor)].popout = 10  # destacase o gajo que pomos entre corchetes, o que ten maior valor de todos
        tarta.slices[tarta.data.index(mayor)].strokeWidth = 2  # a este gajo en concreto cambiamos o tamaño da liña
        tarta.slices[tarta.data.index(mayor)].labelRadius = 1.20  # radio da etiqueta , cambiamolo para este elemento
        tarta.slices[tarta.data.index(mayor)].fontColor = colors.red

        lenda = Legend()
        lenda.x = 370
        lenda.y = 0
        lenda.dx = 8
        lenda.dy = 8
        lenda.fontName = 'Helvetica'
        lenda.fontSize = 7
        lenda.boxAnchor = 'n'
        lenda.columnMaximum = 10
        lenda.strokeColor = colors.black
        lenda.strokeWidth = 1
        lenda.deltax = 75
        lenda.deltay = 10
        lenda.autoXPadding = 5
        lenda.yGap = 0
        lenda.dxTextSpace = 5
        lenda.alignment = 'right'
        lenda.dividerLines = 1 | 2 | 4
        lenda.dividerOffsY = 4.5
        lenda.subCols.rpad = 30

        for i, color in enumerate(cores):
            tarta.slices[i].fillColor = color
        lenda.colorNamePairs = [(tarta.slices[i].fillColor, (tarta.labels[i][0:20], '%0.2f' % tarta.data[i])
                                 ) for i in range(len(tarta.data))]
        '''parrafo 1 : cabeceira primeira grafica'''
        cabeceira = follaEstilo['Heading4']  # formato por defecto

        cabeceira.pageBreakBefore = 0  # con un uno a primeira folla queda en branco
        cabeceira.keepWitNext = 0  # para que non nos deixe a primeira paxina en branco
        cabeceira.backColor = colors.lightcyan
        parrafo = Paragraph("Informe de ventas por marcas", cabeceira)

        guion.append(parrafo)
        guion.append(Spacer(0, 40))

        d.add(lenda)
        d.add(tarta)
        guion.append(d)
        guion.append(Spacer(0, 60))
        '''parrafo 2:cabeceira segunda grafica'''
        cabeceira2 = follaEstilo['Heading4']  # formato por defecto

        cabeceira2.pageBreakBefore = 0  # con un uno a primeira folla queda en branco
        cabeceira2.keepWitNext = 0  # para que non nos deixe a primeira paxina en branco
        cabeceira2.backColor = colors.lightcyan
        parrafo2 = Paragraph("Informe de ventas por año de matriculación", cabeceira)

        guion.append(parrafo2)
        guion.append(Spacer(0, 40))

        d2 = Drawing(400, 200)
        lc = HorizontalLineChart()
        lc.x = 30
        lc.y = 50
        lc.height = 125
        lc.width = 350
        lc.data = []
        lista=[]
        lc.categoryAxis.categoryNames = []

        ventasAno = metodosBase.metodosBase.listar_ventas_anoMatricula(self)

        for ventaAno in ventasAno:
            lista.append(ventaAno[0])
            lc.categoryAxis.categoryNames.append(str(ventaAno[1]))
        lc.data.append(lista)

        lc.categoryAxis.labels.boxAnchor = 'n'
        lc.valueAxis.valueMin = 0
        lc.valueAxis.valueMax = 12
        lc.valueAxis.valueStep = 2
        lc.lines[0].strokeWidth = 2
        lc.lines[0].symbol = makeMarker('FilledCircle')  # círculos rellenos
        lc.lines[1].strokeWidth = 1.5
        d2.add(lc)
        guion.append(d2)
        guion.append(Spacer(0, 20))

        cabeceira3 = follaEstilo['Normal']  # formato por defecto
        parrafo3 = Paragraph(" COCHESJOSE S.L. CARRETERA INFINITA S/N  , TELEFONO:986505050", cabeceira3)
        cabeceira3.keepWitNext = 0  # para que non nos deixe a primeira paxina en branco
        guion.append(parrafo3)
        guion.append(Spacer(0, 20))

        doc = SimpleDocTemplate("informeVentas.pdf", pagesize=A4)

        doc.build(guion)