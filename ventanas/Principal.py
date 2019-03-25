import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from ventanas import Coches
from ventanas import Clientes

class Principal(Gtk.Window):
    def __init__(self):
        '''
        ventana principal, dispondra de dous botons para acceder as duas ventanas de xestión , e un tercer botón para cerrar a aplicación.
        No caso de pulsar este último , pedirase confimación a traves dunha ventá emerxente.
        '''

        # ventana do menú, con tamaño por defecto e non se pode redimensionar
        Gtk.Window.__init__(self, title="CompraVenta")
        self.set_default_size(400, 200)
        self.set_resizable(False)

        self.coches=None

        #caixa onde almacenaremos os tres botons
        caixa = Gtk.Box(spacing=0, orientation=Gtk.Orientation.VERTICAL)


        #para cambiar de cor a caixa , e despois de importar gdk

        caixa.override_background_color(0, Gdk.RGBA(0.937, 0.914, 0.898, 0.5))

        #engadimos a caixa a ventá
        self.add(caixa)

        # para poder aplicar estilos , recurro al css , que se implementa en el archivo de la siguiente forma
        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_path('estilos.css')
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider,
                                             Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


        #creamos os tres botons e os engadimos a caixa
        self.botonCoches = Gtk.Button(label="COCHES", margin_top=30, margin_left=50, margin_right=50)
        self.botonClientes = Gtk.Button(label="CLIENTES", margin_top=30, margin_left=50, margin_right=50)
        self.botonSalir = Gtk.Button(label="Salir", margin_top=60, margin_left=70, margin_right=70, margin_bottom=20)

        caixa.add(self.botonCoches)
        caixa.add(self.botonClientes)
        caixa.add(self.botonSalir)

        #chamadas aos metodos correspondentes de cada boton ao facer click neles
        self.botonCoches.connect("clicked", self.on_open_clicked)
        self.botonClientes.connect("clicked",self.on_open_clientes_clicked)
        self.botonSalir.connect("clicked", self.on_salir_clicked)

        #evento para cerrar a ventá
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


    def on_open_clicked(self,button):
        '''
        metodo para abrir a ventá de xestión de coches, saltará ao dar o primeiro dos botons
        :param button: evento que ocorre ao pulsar o boton
        :return: non devolve nada, abre a ventá coches
        '''

        self.coches =Coches.Coches()

    def on_open_clientes_clicked(self,button):
        '''
        metodo para abrir a ventá de xestión de clientes ao pulsar o segundo botón
        :param button: evento que ocurre ao pulsar o segundo boton
        :return: abre a ventá clientes
        '''

        self.clientes =Clientes.Clientes()

    def on_salir_clicked(self, evt):
        '''
        metodo que salta ao pulsar o metodo de sair
        :param evt: evento ao pulsar o boton correspondente
        :return: mostra un cadro emerxente para confirmar , en caso de confirmación cerra a aplicación.
        '''
        messageDialog = Gtk.MessageDialog(parent=self,
                                          flags=Gtk.DialogFlags.MODAL,
                                          type=Gtk.MessageType.WARNING,
                                          buttons=Gtk.ButtonsType.OK_CANCEL,
                                          message_format="SEGURO QUE DESEA SALIR?")
        response = messageDialog.run()
        if (response == Gtk.ResponseType.OK):
            messageDialog.destroy()
            Principal.destroy(self)
        elif (response==Gtk.ResponseType.CANCEL):
            messageDialog.destroy()


