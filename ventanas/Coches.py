import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from baseDatos import metodosBase

class Coches(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Gestión de coches")

        self.set_resizable(False)
        self.set_border_width(5)

        vbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox.override_background_color(0, Gdk.RGBA(0.937, 0.914, 0.898, 0.5))
        self.add(vbox)

        vbox2=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)

        gridCompra=Gtk.Grid()
        boxVenta=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        labelTitulo = Gtk.Label(label="COMPRA DE COCHES", margin_bottom=20)
        self.botonOk = Gtk.Button(label="COMPRAR", margin_top=20, margin_bottom=20, margin_left=80, margin_right=80)

        vbox2.add(labelTitulo)
        vbox2.add(gridCompra)
        vbox2.add(self.botonOk)

        stack=Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)


        stack.add_titled(vbox2, "compra","Compra")
        stack.add_titled(boxVenta,"venta","Venta")

        self.labelMatricula=Gtk.Label()
        self.labelMarca = Gtk.Label()
        self.labelModelo = Gtk.Label()
        self.labelKm = Gtk.Label()
        self.labelAno = Gtk.Label()
        self.labelPrecio = Gtk.Label()
        self.labelClase = Gtk.Label()
        self.labelMatricula.set_markup("Matricula ")
        self.labelMarca.set_markup("  Marca  ")
        self.labelModelo.set_markup("Modelo")
        self.labelAno.set_markup("Año")
        self.labelKm.set_markup("  Kilometros ")
        self.labelPrecio.set_markup("  Precio  ")
        self.labelClase.set_markup("  Clase  ")

        self.entryMatricula=Gtk.Entry()
        self.entryMarca = Gtk.Entry()
        self.entryModelo = Gtk.Entry()
        self.entryKm = Gtk.Entry()
        self.entryPrecio = Gtk.Entry()
        self.entryAno=Gtk.Entry()

        lista_clases =Gtk.ListStore(int,str)
        lista_clases.append([0,""])
        lista_clases.append([1,"A"])
        lista_clases.append([2,"B"])
        lista_clases.append([3,"C"])
        lista_clases.append([4,"D"])
        lista_clases.append([5,"E"])
        lista_clases.append([6,"MUSCLE"])
        lista_clases.append([7,"CROSSOVER"])
        lista_clases.append([8,"FAMILIAR"])
        lista_clases.append([9,"DEPORTIVO"])

        self.comboClases = Gtk.ComboBox.new_with_model_and_entry(lista_clases)
        self.comboClases.set_entry_text_column(1)


        self.botonOk.connect("clicked", self.on_open_clicked)

        gridCompra.add(self.labelMatricula)
        gridCompra.attach(self.entryMatricula,1,0,2,1)
        gridCompra.attach(self.labelMarca,3,0,1,1)
        gridCompra.attach(self.entryMarca,4,0,2,1)
        gridCompra.attach(self.labelModelo, 0, 1, 1, 1)
        gridCompra.attach(self.entryModelo, 1, 1, 2, 1)
        gridCompra.attach(self.labelPrecio, 3, 1, 1, 1)
        gridCompra.attach(self.entryPrecio, 4, 1, 2, 1)
        gridCompra.attach(self.labelKm, 0, 2, 1, 1)
        gridCompra.attach(self.entryKm, 1, 2, 2, 1)
        gridCompra.attach(self.labelClase, 3, 2, 1, 1)
        gridCompra.attach(self.comboClases, 4, 2, 2, 1)
        gridCompra.attach(self.labelAno, 0, 3, 1, 1)
        gridCompra.attach(self.entryAno, 1, 3, 2, 1)

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher,True,True,0)
        vbox.pack_start(stack,True,True,0)

        self.show_all()

    def on_open_clicked(self,button):

        metodosBase.metodosBase.insertar_datos_coches(self,self.entryMatricula.get_text(),self.entryMarca.get_text(),
                                                      self.entryModelo.get_text(),
                                                      self.entryKm.get_text(),self.entryAno.get_text(),
                                                      self.entryPrecio.get_text()
                                                      ,self.comboClases.get_active())
        self.entryMatricula.set_text("")
        self.entryModelo.set_text("")
        self.entryMarca.set_text("")
        self.entryKm.set_text("")
        self.entryAno.set_text("")
        self.entryPrecio.set_text("")
        self.comboClases.set_active(0)

