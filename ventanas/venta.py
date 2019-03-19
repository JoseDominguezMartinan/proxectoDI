import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from baseDatos import metodosBase
from ventanas import Coches

class Venta():

    def __init__(self, matricula):
        builder=Gtk.Builder()
        builder.add_from_file("ventana.glade")



        '''''''# para poder aplicar estilos , recurro al css , que se implementa en el archivo de la siguiente forma'''
        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_path('estilos.css')
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider,
                                             Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        self.fiestra=builder.get_object("FiestraPrincipal")

        self.entryMatricula=builder.get_object("entryMatricula")
        self.entryMatricula.set_text(matricula)
        self.entryDni = builder.get_object("entryDni")
        self.entryFecha = builder.get_object("entryFecha")

        self.calendario=builder.get_object("calendario")
        self.botonVender = builder.get_object("botonVender")
        self.botonLimpiar = builder.get_object("botonLimpiar")
        self.botonSalir = builder.get_object("botonSalir")

        sinais={
            "on_calendario_day_selected_double_click":self.on_calendario_day_selected_double_click,
            "on_botonVender_clicked":self.on_botonVender_clicked,
            "on_botonLimpiar_clicked":self.on_botonLimpiar_clicked,
            "on_botonSalir_clicked":self.on_botonSalir_clicked
        }

        builder.connect_signals(sinais)
        self.fiestra.show_all()

    def on_calendario_day_selected_double_click(self, evt):
        year, month, day=self.calendario.get_date()
        self.entryFecha.set_text(str(day)+"/"+str(month)+"/"+str(year))

    def on_botonVender_clicked(self,evt):

        matricula=self.entryMatricula.get_text()
        dni=self.entryDni.get_text()
        fecha=self.entryFecha.get_text()
        if not(matricula == "" and dni == "" and fecha == ""):
            self.on_botonLimpiar_clicked("")
            metodosBase.metodosBase.insertar_datos_ventas(self,matricula,dni,fecha)
            metodosBase.metodosBase.modificar_datoventa_coches(self,matricula,True)

            selection = Coches.Coches.vista.get_selection()
            model, paths = selection.get_selected_rows()

            for path in paths:
                iterador = Coches.Coches.modelos.get_iter(path)
                Coches.Coches.modelos.remove(iterador)






    def on_botonLimpiar_clicked(self,evt):
        self.entryMatricula.set_text("")
        self.entryDni.set_text("")
        self.entryFecha.set_text("")

    def on_botonSalir_clicked(self,evt):
        self.fiestra.destroy()



