import distutils

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from baseDatos import metodosBase
from ventanas import venta
from ventanas import Principal


class Clientes(Gtk.Window):


    def __init__(self):
        '''
        constructor
        se genera todos los boxes y widgets de la ventana
        '''
        Gtk.Window.__init__(self,title="Gestión de clientes")
        self.set_default_size(600, 400)
        self.set_resizable(False)
        self.set_border_width(5)

        self.modelos = Gtk.ListStore(str,str,str,str,str,str)

        self.filtro_categoria = self.modelos.filter_new()

        self.vista = Gtk.TreeView(model=self.filtro_categoria)



        self.parametro_filtro_categoria = None

        """almacenaremos aqui las coordenadas para modificaciones posteriormente"""
        self.x=0
        self.y=2
        """para controlar que seu pueda modificar o no el togled del treeview"""
        self.modificable=False



        '''ventana 1 : añadir clientes'''

        vbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6, homogeneous=False)
        vbox.override_background_color(0, Gdk.RGBA(0.937, 0.914, 0.898, 0.5))
        self.add(vbox)

        boxAnadir=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=50, homogeneous=False)

        gridAnadir=Gtk.Grid(margin_left=150)



        self.filtro_categoria.set_visible_func(self.categoria_filtro)

        self.boxVenta=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6, homogeneous=False)

        labelTitulo = Gtk.Label(label="AÑADIR CLIENTES", margin_bottom=20)
        self.botonOk = Gtk.Button(label="AÑADIR", margin_top=20, margin_left=80, margin_right=80)

        labelTituloGestion=Gtk.Label(label="GESTION DE CLIENTES", margin_bottom=20)
        self.boxVenta.add(labelTituloGestion)


        self.botonBorrar = Gtk.Button(label="Borrar")
        self.botonModificar = Gtk.Button(label="Modificar")
        self.botonModificar.connect("clicked", self.modificar_clicked)
        self.botonSalir = Gtk.Button(label="Salir", margin_left=625)
        self.botonSalir2 = Gtk.Button(label="Salir", margin_left=25)
        self.botonLimpar = Gtk.Button(label="Limpiar", margin_left=600)
        self.botonSalir.connect("clicked", self.on_close_clicked)
        self.botonSalir2.connect("clicked", self.on_close_clicked)
        self.botonLimpar.connect("clicked",self.limpar_clicked)
        self.botonBorrar.connect("clicked", self.borrar_clicked)

        self.boxBotonesVentas = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.boxBotonesVentas.add(self.botonLimpar)
        self.boxBotonesVentas.add(self.botonSalir2)

        '''''''# para poder aplicar estilos , recurro al css , que se implementa en el archivo de la siguiente forma'''
        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_path('estilos.css')
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider,
                                             Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        boxAnadir.add(labelTitulo)
        boxAnadir.add(gridAnadir)

        boxAnadir.add(self.botonOk)
        boxAnadir.add(self.boxBotonesVentas)

        stack=Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)


        stack.add_titled(boxAnadir, "añadir","Añadir")

        stack.add_titled(self.boxVenta,"gestion","Gestion")

        self.labelDni=Gtk.Label()
        self.labelNome = Gtk.Label()
        self.labelFecha = Gtk.Label()
        self.labelTelefono = Gtk.Label()
        self.labelDireccion = Gtk.Label()
        self.labelCodPostal = Gtk.Label()


        self.labelDni.set_markup("DNI ")
        self.labelNome.set_markup("  Nombre Completo  ")
        self.labelFecha.set_markup("Fecha")
        self.labelDireccion.set_markup("Direccion")
        self.labelTelefono.set_markup("  Telefono ")
        self.labelCodPostal.set_markup("  Cod.Postal  ")


        self.entryDni=Gtk.Entry()
        self.entryNome = Gtk.Entry()
        self.entryFecha = Gtk.Entry()
        self.entryTelefono = Gtk.Entry()
        self.entryCodPostal = Gtk.Entry()
        self.entryDireccion=Gtk.Entry()


        self.botonOk.connect("clicked", self.on_open_clicked)

        gridAnadir.add(self.labelDni)
        gridAnadir.attach(self.entryDni, 1, 0, 2, 1)
        gridAnadir.attach(self.labelNome, 3, 0, 1, 1)
        gridAnadir.attach(self.entryNome, 4, 0, 2, 1)
        gridAnadir.attach(self.labelFecha, 0, 1, 1, 1)
        gridAnadir.attach(self.entryFecha, 1, 1, 2, 1)
        gridAnadir.attach(self.labelCodPostal, 3, 1, 1, 1)
        gridAnadir.attach(self.entryCodPostal, 4, 1, 2, 1)
        gridAnadir.attach(self.labelTelefono, 0, 2, 1, 1)
        gridAnadir.attach(self.entryTelefono, 1, 2, 2, 1)
        gridAnadir.attach(self.labelDireccion, 3, 2, 1, 1)
        gridAnadir.attach(self.entryDireccion, 4, 2, 2, 1)


        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher,True,True,0)
        vbox.pack_start(stack,True,True,0)

        '''ventana 2: gestion de clientes'''

        self.clientes=metodosBase.metodosBase.listar_clientes(self)



        for cliente in self.clientes:
            self.modelos.append([cliente[0],
                                 cliente[1], cliente[2], cliente[3],
                                 cliente[4], cliente[5]])



        self.scrollTree = Gtk.ScrolledWindow(hexpand=True, vexpand=True)

        self.scrollTree.add_with_viewport(self.vista)

        self.seleccion = self.vista.get_selection()
        self.celdaText = Gtk.CellRendererText()
        self.celdaText.connect("edited", self.on_celdaText_edited, self.modelos)


        self.celdaText.set_property("editable", False)

        self.vista.connect("button-press-event", self.on_pressed)

        self.columnaDni = Gtk.TreeViewColumn('DNI', self.celdaText, text=0)
        self.columnaDni.set_sort_column_id(0)
        self.columnaDni.colnr = 0
        self.vista.append_column(self.columnaDni)

        self.columnaNome = Gtk.TreeViewColumn('Nombre completo', self.celdaText, text=1)
        self.columnaNome.set_sort_column_id(1)
        self.columnaNome.colnr = 1
        self.vista.append_column(self.columnaNome)

        self.columnaFecha = Gtk.TreeViewColumn('Fecha nacimiento', self.celdaText, text=2)
        self.columnaFecha.set_sort_column_id(2)
        self.columnaFecha.colnr = 2
        self.vista.append_column(self.columnaFecha)

        self.columnaTelefono = Gtk.TreeViewColumn('Telefono', self.celdaText, text=3)
        self.columnaTelefono.set_sort_column_id(3)
        self.columnaTelefono.colnr = 3
        self.vista.append_column(self.columnaTelefono)

        self.columnaDireccion = Gtk.TreeViewColumn('Direccion', self.celdaText, text=4)
        self.columnaDireccion.set_sort_column_id(4)
        self.columnaDireccion.colnr = 4
        self.vista.append_column(self.columnaDireccion)

        self.columnaCodPostal = Gtk.TreeViewColumn('Codigo Postal', self.celdaText, text=5)
        self.columnaCodPostal.set_sort_column_id(5)
        self.columnaCodPostal.colnr = 5
        self.vista.append_column(self.columnaCodPostal)


        self.boxVenta.add(self.scrollTree)



        self.filtrarBox=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=20)
        self.entryFiltrar=Gtk.Entry()

        self.lista_filtrar = Gtk.ListStore(int, str)

        self.lista_filtrar.append([0, "DNI"])
        self.lista_filtrar.append([1, "Nombre"])
        self.lista_filtrar.append([2, "FechaNacimiento"])
        self.lista_filtrar.append([3, "Telefono"])
        self.lista_filtrar.append([4, "Direccion"])
        self.lista_filtrar.append([5, "CodPostal"])

        self.comboFiltrar = Gtk.ComboBox.new_with_model_and_entry(self.lista_filtrar)
        self.comboFiltrar.set_entry_text_column(1)

        self.botonFiltrar = Gtk.Button(label="Filtrar")
        self.botonFiltrar.connect("clicked", self.on_btnFiltrar_clicked)

        self.filtrarBox.add(self.entryFiltrar)
        self.filtrarBox.add(self.comboFiltrar)
        self.filtrarBox.add(self.botonFiltrar)

        self.boxVenta.add(self.filtrarBox)


        self.botonesBox=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=10)
        self.botonesBox.add(self.botonModificar)
        self.botonesBox.add(self.botonBorrar)
        self.botonesBox.add(self.botonSalir)

        self.boxVenta.add(self.botonesBox)

        self.categoria = self.lista_filtrar[self.comboFiltrar.get_active()][0]


        self.show_all()



    def on_open_clicked(self,button):
        '''
        funcion para insertar clientes en la base de datos, se añade tambien a la vista del tree view
        :param button: evento
        :return: None
        '''

        error=metodosBase.metodosBase.insertar_datos_clientes(self, self.entryDni.get_text(), self.entryNome.get_text(),
                                                            self.entryFecha.get_text(),
                                                            self.entryTelefono.get_text(), self.entryDireccion.get_text(),
                                                            self.entryCodPostal.get_text(),
                                                            )
        if(error==True):

            self.modelos.append([self.entryDni.get_text(), self.entryNome.get_text(),
                                 self.entryFecha.get_text(),
                                 self.entryTelefono.get_text(), self.entryDireccion.get_text(),
                                 self.entryCodPostal.get_text(),
                                 ])

            self.limpar_clicked(self)

        else:
            messageDialog = Gtk.MessageDialog(parent=self,
                                              flags=Gtk.DialogFlags.MODAL,
                                              type=Gtk.MessageType.WARNING,
                                              buttons=Gtk.ButtonsType.OK,
                                              message_format="Inserte todos los datos y no introduzca dni repetido")
            response = messageDialog.run()
            if (response == Gtk.ResponseType.OK):
                messageDialog.destroy()



    def on_btnFiltrar_clicked(self, control):
        '''
        para filtrar por un parametro de busqueda
        :param control: evento
        :return:None
        '''

        self.punteiro=self.entryFiltrar.get_text()
        self.categoria = self.lista_filtrar[self.comboFiltrar.get_active()][1]

        self.parametro_filtro_categoria = self.entryFiltrar.get_text()
        if self.parametro_filtro_categoria=="True":
            self.parametro_filtro_categoria=True
        if self.parametro_filtro_categoria=="False":
            self.parametro_filtro_categoria=False
        if self.parametro_filtro_categoria=="":
            self.parametro_filtro_categoria=None



        self.filtro_categoria.refilter()
        self.entryFiltrar.set_text("")




    def categoria_filtro(self, modelo,  punteiro, datos):
        '''
        devuelve en caso de tener coincidencias las entradas que corresponden con la busqueda
        :param modelo: modelo del tree view donde se muestran los datos
        :param punteiro: fila afectada
        :param datos: datos de la fila
        :return: boolean, true si hay coincidencia , false en caso contrario
        '''


        if self.parametro_filtro_categoria is None:
            return True
        else:
            if(self.categoria=="DNI"):
                if self.modelos[punteiro][0]==self.parametro_filtro_categoria:
                    return True
                else:
                    return False
            if (self.categoria == "Nombre"):
                if self.modelos[punteiro][1] == self.parametro_filtro_categoria:
                    return True
                else:
                    return False
            if (self.categoria == "FechaNacimiento"):


                if self.modelos[punteiro][2]  == self.parametro_filtro_categoria:
                    return True
                else:
                    return False
            if (self.categoria == "Telefono"):
                if self.modelos[punteiro][3] == self.parametro_filtro_categoria:
                    return True
                else:
                    return False
            if (self.categoria == "Direccion"):
                if self.modelos[punteiro][4] == self.parametro_filtro_categoria:
                    return True
                else:
                    return False
            if (self.categoria == "CodPostal"):
                if self.modelos[punteiro][5] == self.parametro_filtro_categoria:
                    return True
                else:
                    return False

    def on_close_clicked(self, control):
        '''
        cierra la ventana actual
        :param control: evento
        :return: None
        '''
        Clientes.destroy(self)

    def limpar_clicked(self, control):
        '''
        limpia los entry text del formulario
        :param control: evento
        :return: None
        '''

        self.entryDni.set_text("")
        self.entryFecha.set_text("")
        self.entryNome.set_text("")
        self.entryTelefono.set_text("")
        self.entryDireccion.set_text("")
        self.entryCodPostal.set_text("")

    def on_pressed(self, trview, event):
        '''
        salta al dar click en una de las filas del treeview
        :param trview: tabla donde se muestra la información
        :param event: evento
        :return: None
        '''
        try:
            path, col, x, y = trview.get_path_at_pos(event.x, event.y)
            coordenada=(col.colnr, path.to_string())
            self.x=int(coordenada[0])
            self.y=int(coordenada[1])
        except:
            print("erro, ten que marcar algo")



    def on_celdaText_edited (self, control, punteiro, texto, modelo):
        '''
        ocurre cando se edita a celda seleccionada
        :param control: evento
        :param punteiro: fila marcada
        :param texto: texto que se modificou
        :param modelo: modelo do tree view que se esta mostrando por pantalla
        :return: None
        '''
        x=int(self.x)
        modelo[punteiro][x] = texto
        metodosBase.metodosBase.modificar_datos_clientes(self,self.modelos[punteiro][0],self.modelos[punteiro][1]
                                                       ,self.modelos[punteiro][2],self.modelos[punteiro][3],self.modelos[punteiro][4]
                                                       ,self.modelos[punteiro][5])
        self.celdaText.set_property("editable", False)



    def modificar_clicked(self, control):
        '''
        ao presionar o boton modificar , habilitamos a edicion do tree view
        :param control: evento
        :return: None
        '''
        self.celdaText.set_property("editable", True)
        self.modificable=True



    def borrar_clicked(self, evt):
        '''
        borra a fila marcada no tree view, lanza un cadro de confirmación para que non se borre nada por erro
        :param evt: evento
        :return: None 
        '''
        y = int(self.y)
        x= int(self.x)
        messageDialog = Gtk.MessageDialog(parent=self,
                                          flags=Gtk.DialogFlags.MODAL,
                                          type=Gtk.MessageType.WARNING,
                                          buttons=Gtk.ButtonsType.OK_CANCEL,
                                          message_format="¿Desea eliminar la fila seleccionada?")
        response = messageDialog.run()
        if (response == Gtk.ResponseType.CANCEL):
            messageDialog.destroy()
        elif (response == Gtk.ResponseType.OK):

            metodosBase.metodosBase.borrar_datos_clientes(self, self.modelos[y][0])
            selection = self.vista.get_selection()
            model, paths = selection.get_selected_rows()
            for path in paths:
                iterador = self.modelos.get_iter(path)
                self.modelos.remove(iterador)

            messageDialog.destroy()


