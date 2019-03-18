import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from ventanas import Coches

class Principal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="CompraVenta")
        self.set_default_size(400, 200)
        self.set_resizable(False)



        caixa = Gtk.Box(spacing=0, orientation=Gtk.Orientation.VERTICAL)


        '''para cambiar de cor a caixa , e despois de importar gdk'''

        caixa.override_background_color(0, Gdk.RGBA(0.937, 0.914, 0.898, 0.5))

        self.add(caixa)

        '''''''# para poder aplicar estilos , recurro al css , que se implementa en el archivo de la siguiente forma'''
        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_path('estilos.css')
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider,
                                             Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


        self.botonCoches = Gtk.Button(label="COCHES", margin_top=30, margin_left=50, margin_right=50)
        self.botonClientes = Gtk.Button(label="CLIENTES", margin_top=30, margin_left=50, margin_right=50)
        self.botonTaller = Gtk.Button(label="TALLER", margin_top=30, margin_left=50, margin_right=50)

        caixa.add(self.botonCoches)
        caixa.add(self.botonClientes)
        caixa.add(self.botonTaller)

        self.botonCoches.connect("clicked", self.on_open_clicked)


        self.connect("destroy", Gtk.main_quit)
        self.show_all()


    def on_open_clicked(self,button):
        coches =Coches.Coches()





