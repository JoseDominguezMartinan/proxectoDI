import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from baseDatos import metodosBase
from ventanas import Coches
from platy import informeAlbaran

class Venta():

    def __init__(self, matricula):
        '''
        constructor, aqui se xenera a caixa cos widgets desta ventá, recibe a matricula do coche a vender para asi autocompletar ese campo
        :param matricula: matricula do coche a vender
        '''
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
        '''
        metodo para completar o campo fecha tras facer doble click no widget calendario que dispon a ventá
        :param evt: evento
        :return: None
        '''
        year, month, day=self.calendario.get_date()
        self.entryFecha.set_text(str(day)+"/"+str(month)+"/"+str(year))

    def on_botonVender_clicked(self,evt):
        '''
        metodo que salta ao darlle o boton vender, modifica o coche na taboa coches para polo como vendido, inserta a entrada en ventas, e xenera unha factura
        :param evt:
        :return: None
        '''

        matricula=self.entryMatricula.get_text()
        dni=self.entryDni.get_text()
        fecha=self.entryFecha.get_text()

        if not(matricula == "" and dni == "" and fecha == ""):

                self.on_botonLimpiar_clicked("")
                numVenta=metodosBase.metodosBase.insertar_datos_ventas(self,matricula,dni,fecha)
                if(numVenta is not None):
                    num=numVenta[0][0]
                    metodosBase.metodosBase.modificar_datoventa_coches(self,matricula,True)
                    albaran=informeAlbaran.informeAlbaran.crear_factura(self,num,matricula,dni,fecha)
                    if(albaran==False):
                        messageDialog = Gtk.MessageDialog(parent=self,
                                                          flags=Gtk.DialogFlags.MODAL,
                                                          type=Gtk.MessageType.WARNING,
                                                          buttons=Gtk.ButtonsType.OK,
                                                          message_format="NO SE PUEDE HACER LA FACTURA, CLIENTE NO REGISTRADO")
                        response = messageDialog.run()
                        if (response == Gtk.ResponseType.OK):
                            messageDialog.destroy()
                else:
                    messageDialog2 = Gtk.MessageDialog(parent=None,
                                                     flags=Gtk.DialogFlags.MODAL,
                                                     type=Gtk.MessageType.WARNING,
                                                     buttons=Gtk.ButtonsType.OK,
                                                     message_format="ERROR, CLIENTE NO ENCONTRADO")
                    response2 = messageDialog2.run()
                    if (response2 == Gtk.ResponseType.OK):
                        messageDialog2.destroy()


    def on_botonLimpiar_clicked(self,evt):
        '''
        metodo para limpar os campos de entrada de texto do formulario
        :param evt:
        :return: None
        '''
        self.entryMatricula.set_text("")
        self.entryDni.set_text("")
        self.entryFecha.set_text("")

    def on_botonSalir_clicked(self,evt):
        '''
        metodo para cerrar a ventá actual
        :param evt:
        :return: None
        '''
        self.fiestra.destroy()