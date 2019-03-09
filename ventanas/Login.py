import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk


class Login (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="CompraVenta")
        self.set_default_size(600,400)
        self.set_resizable(False)

        # para poder aplicar estilos , recurro al css , que se implementa en el archivo de la siguiente forma
        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_path('estilos.css')
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider,
                                             Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        caixa2 = Gtk.Box(spacing=0,orientation=Gtk.Orientation.VERTICAL)
        caixa = Gtk.Box(spacing=0, orientation=Gtk.Orientation.HORIZONTAL)

        '''para cambiar de cor a caixa , e despois de importar gdk'''

        caixa.override_background_color(0, Gdk.RGBA(0.937, 0.914, 0.898, 0.5))


        self.add(caixa)

        self.imagen = Gtk.Image(margin_bottom=85)
        self.imagen.set_from_file("login.JPG")
        caixa.pack_start(self.imagen, True, True, 0)


        self.lblNome=Gtk.Label(label="USUARIO:", margin_top=55)


        self.txtNome=Gtk.Entry(margin_left=30, margin_right=30)
        caixa2.pack_start(self.lblNome, True, True, 0)
        caixa2.pack_start(self.txtNome, True, True, 0)

        self.lblPass=Gtk.Label(label="CONTRASEÑA:", margin_top=40, margin_bottom=20)

        self.txtPass=Gtk.Entry(margin_bottom=40, margin_left=30, margin_right=30)
        self.txtPass.set_visibility(False)

        caixa2.pack_start(self.lblPass, True, True, 0)
        caixa2.pack_start(self.txtPass, True, True, 0)

        caixa.pack_start(caixa2, True, True, 0)

        self.boton = Gtk.Button(label="CONECTAR", margin_bottom=80, margin_left=300, margin_right=50)



        caixa2.pack_end(self.boton, True, True, 10)

        # para poder aplicar estilos , recurro al css , que se implementa en el archivo de la siguiente forma
        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_path('estilos.css')
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider,
                                             Gtk.STYLE_PROVIDER_PRIORITY_USER)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Login()
    Gtk.main()



