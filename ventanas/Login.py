import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from ventanas import Principal
from baseDatos import metodosBase


class Login (Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="CompraVenta")
        self.set_default_size(600,400)
        self.set_resizable(False)


        metodosBase.metodosBase.conectar(self)
        metodosBase.metodosBase.crear_tablas(self)
        metodosBase.metodosBase.insertar_datos_usuarios(self, "1", "abc123.")




        '''''''# para poder aplicar estilos , recurro al css , que se implementa en el archivo de la siguiente forma'''
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

        self.lblPass=Gtk.Label(label="CONTRASINAL:", margin_top=40, margin_bottom=20)

        self.txtPass=Gtk.Entry(margin_bottom=40, margin_left=30, margin_right=30)
        self.txtPass.set_visibility(False)

        caixa2.pack_start(self.lblPass, True, True, 0)
        caixa2.pack_start(self.txtPass, True, True, 0)

        caixa.pack_start(caixa2, True, True, 0)

        self.boton = Gtk.Button(label="CONECTAR", margin_bottom=80, margin_left=300, margin_right=50)
        self.boton.connect("clicked", self.on_open_clicked)




        caixa2.pack_end(self.boton, True, True, 10)



        self.connect("destroy", Gtk.main_quit)
        self.show_all()


        '''sinal para ao facer click na contrasinal facer o mesmo que no boton '''
        self.txtPass.connect("activate", self.on_open_clicked)

        self.txtNome.connect("activate", self.on_txt_clicked)


    def on_open_clicked(self, button):

        logueado = metodosBase.metodosBase.compobrar_usuarios(self,self.txtNome.get_text(), self.txtPass.get_text())
        if(logueado==True):
            principal = Principal.Principal()
            self.set_visible(False)
        else:
            self.txtNome.set_text("")
            self.txtPass.set_text("")
            messageDialog = Gtk.MessageDialog(parent=self,
                                              flags=Gtk.DialogFlags.MODAL,
                                              type=Gtk.MessageType.WARNING,
                                              buttons=Gtk.ButtonsType.OK,
                                              message_format="USUARIO O CONTRASEÑA INCORRECTOS")
            response=messageDialog.run()
            if(response==Gtk.ResponseType.OK):
                messageDialog.destroy()

    def on_txt_clicked(self,button):
        self.txtPass.grab_focus()


if __name__ == "__main__":
    Login()
    Gtk.main()



