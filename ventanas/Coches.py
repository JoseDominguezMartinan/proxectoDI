import distutils

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from baseDatos import metodosBase
from ventanas import venta
from ventanas import Principal
from platy import informeVentas


class Coches(Gtk.Window):


    def __init__(self):

        #ventá para a xestión dos coches
        Gtk.Window.__init__(self,title="Gestión de coches")
        self.set_default_size(600, 400)
        self.set_resizable(False)
        self.set_border_width(5)

        # para poder aplicar estilos , recurro al css , que se implementa en el archivo de la siguiente forma
        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_path('estilos.css')
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider,
                                             Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        #contedores que precisamos para as ventás:

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6, homogeneous=False)
        vbox.override_background_color(0, Gdk.RGBA(0.937, 0.914, 0.898, 0.5))
        self.add(vbox)

        boxCompra = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50, homogeneous=False)
        gridCompra = Gtk.Grid(margin_left=150)

        self.boxVenta = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6, homogeneous=False)

        self.boxBotonesVentas = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.botonesBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=10)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher, True, True, 0)
        vbox.pack_start(stack, True, True, 0)

        self.modelos = Gtk.ListStore(str, str, str, int, int, str, str, bool, str, int)

        self.filtro_categoria = self.modelos.filter_new()

        self.vista = Gtk.TreeView(model=self.filtro_categoria)

        self.parametro_filtro_categoria = None

        #variables que precisamos:q
        #almacenaremos aqui las coordenadas para modificaciones posteriormente
        self.x=0
        self.y=2
        #para controlar que seu pueda modificar o no el togled del treeview
        self.modificable=False

        #engadimos ao stack os titulos das duas ventás que vai a ter
        stack.add_titled(boxCompra, "compra", "Compra")
        stack.add_titled(self.boxVenta, "venta", "Venta")


        #necesario para a opcion de filtrar
        self.filtro_categoria.set_visible_func(self.categoria_filtro)

        #labels
        labelTitulo = Gtk.Label(label="COMPRA DE COCHES", margin_bottom=20)
        labelTituloVenta=Gtk.Label(label="VENTA DE COCHES", margin_bottom=20)
        self.boxVenta.add(labelTituloVenta)
        self.labelMatricula = Gtk.Label()
        self.labelMarca = Gtk.Label()
        self.labelModelo = Gtk.Label()
        self.labelKm = Gtk.Label()
        self.labelAno = Gtk.Label()
        self.labelPrecio = Gtk.Label()
        self.labelClase = Gtk.Label()
        self.labelAutomatico = Gtk.Label()
        self.labelMotor = Gtk.Label()
        self.labelCaballos = Gtk.Label()

        self.labelMatricula.set_markup("Matricula ")
        self.labelMarca.set_markup("  Marca  ")
        self.labelModelo.set_markup("Modelo")
        self.labelAno.set_markup("Año")
        self.labelKm.set_markup("  Kilometros ")
        self.labelPrecio.set_markup("  Precio  ")
        self.labelAutomatico.set_markup("  Auto.  ")
        self.labelMotor.set_markup("  Motor  ")
        self.labelCaballos.set_markup("  Caballos  ")
        self.labelClase.set_markup("  Clase  ")

        #botons e entrys
        self.botonOk = Gtk.Button(label="COMPRAR", margin_top=20, margin_left=80, margin_right=80)
        self.botonVender = Gtk.Button(label="Vender")
        self.botonModificar = Gtk.Button(label="Modificar")
        self.botonModificar.connect("clicked", self.modificar_clicked)
        self.botonSalir = Gtk.Button(label="Salir", margin_left=625)
        self.botonSalir2 = Gtk.Button(label="Salir", margin_left=25)
        self.botonLimpar = Gtk.Button(label="Limpiar", margin_left=600)
        self.botonInforme=Gtk.Button(label="Informe")

        self.entryMatricula = Gtk.Entry()
        self.entryMarca = Gtk.Entry()
        self.entryModelo = Gtk.Entry()
        self.entryKm = Gtk.Entry()
        self.entryPrecio = Gtk.Entry()
        self.entryAno = Gtk.Entry()
        self.entryMotor = Gtk.Entry()
        self.entryCaballos = Gtk.Entry()

        self.checkAutomatico = Gtk.CheckButton()

        #eventos
        self.botonSalir.connect("clicked", self.on_close_clicked)
        self.botonSalir2.connect("clicked", self.on_close_clicked)
        self.botonLimpar.connect("clicked",self.limpar_clicked)
        self.botonVender.connect("clicked", self.vender_clicked)
        self.botonInforme.connect("clicked",self.crear_informe)
        self.botonOk.connect("clicked", self.on_open_clicked)

        #engadimos as caixas correspondentes
        self.boxBotonesVentas.add(self.botonLimpar)
        self.boxBotonesVentas.add(self.botonSalir2)

        #engadimos as caixas correspondentes
        boxCompra.add(labelTitulo)
        boxCompra.add(gridCompra)
        boxCompra.add(self.botonOk)
        boxCompra.add(self.boxBotonesVentas)

        #list store para o combo box
        self.lista_clases =Gtk.ListStore(int,str)
        self.lista_clases.append([0,""])
        self.lista_clases.append([1,"A"])
        self.lista_clases.append([2,"B"])
        self.lista_clases.append([3,"C"])
        self.lista_clases.append([4,"D"])
        self.lista_clases.append([5,"E"])
        self.lista_clases.append([6,"MUSCLE"])
        self.lista_clases.append([7,"4x4"])
        self.lista_clases.append([8,"FAMILIAR"])
        self.lista_clases.append([9,"DEPORTIVO"])

        self.comboClases = Gtk.ComboBox.new_with_model_and_entry(self.lista_clases)
        self.comboClases.set_entry_text_column(1)

        #formateamos como van a aparecer os widgets dentro do grid que creamos para a venta de insercion de coches
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
        gridCompra.attach(self.labelMotor, 3, 3, 1, 1)
        gridCompra.attach(self.entryMotor, 4, 3, 2, 1)
        gridCompra.attach(self.labelCaballos, 0, 4, 1, 1)
        gridCompra.attach(self.entryCaballos, 1, 4, 2, 1)
        gridCompra.attach(self.labelAutomatico, 3, 4, 1, 1)
        gridCompra.attach(self.checkAutomatico, 4, 4, 2, 1)



        '''ventana 2: venta de coches'''

        #chamamos ao metodo da base de datos para listar os coches e asi amosalos na nosa taboa
        self.coches=metodosBase.metodosBase.listar_coches(self)

        #recorremos esta lista
        for coche in self.coches:
            self.modelos.append([coche[0],
                                 coche[1], coche[2], coche[3],
                                 coche[4], ("%.2f" % coche[5]),
                                 coche[6],
                                 coche[7], coche[8], coche[9]])

        #xeramos un scroll para meter dentro a taboa
        self.scrollTree = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        self.scrollTree.add_with_viewport(self.vista)

        #elementos para a estructura da taboa
        self.seleccion = self.vista.get_selection()
        self.celdaText = Gtk.CellRendererText()
        self.celdaText.connect("edited", self.on_celdaText_edited, self.modelos)

        self.celdaButton= Gtk.CellRendererToggle()
        self.celdaButton.connect("toggled", self.on_cell_toggled)
        self.celdaText.set_property("editable", False)

        self.vista.connect("button-press-event", self.on_pressed)

        # damos formato a taboa
        self.columnaMatricula = Gtk.TreeViewColumn('Matricula', self.celdaText, text=0)
        self.columnaMatricula.set_sort_column_id(0)
        self.columnaMatricula.colnr = 0
        self.vista.append_column(self.columnaMatricula)

        self.columnaMarca = Gtk.TreeViewColumn('Marca', self.celdaText, text=1)
        self.columnaMarca.set_sort_column_id(1)
        self.columnaMarca.colnr = 1
        self.vista.append_column(self.columnaMarca)

        self.columnaModelo = Gtk.TreeViewColumn('Modelo', self.celdaText, text=2)
        self.columnaModelo.set_sort_column_id(2)
        self.columnaModelo.colnr = 2
        self.vista.append_column(self.columnaModelo)

        self.columnaKm = Gtk.TreeViewColumn('Kilometros', self.celdaText, text=3)
        self.columnaKm.set_sort_column_id(3)
        self.columnaKm.colnr = 3
        self.vista.append_column(self.columnaKm)

        self.columnaAno = Gtk.TreeViewColumn('Año', self.celdaText, text=4)
        self.columnaAno.set_sort_column_id(4)
        self.columnaAno.colnr = 4
        self.vista.append_column(self.columnaAno)

        self.columnaPrecio = Gtk.TreeViewColumn('Precio', self.celdaText, text=5)
        self.columnaPrecio.set_sort_column_id(5)
        self.columnaPrecio.colnr = 5
        self.vista.append_column(self.columnaPrecio)

        self.columnaClase = Gtk.TreeViewColumn('Clase', self.celdaText, text=6)
        self.columnaClase.set_sort_column_id(6)
        self.columnaClase.colnr = 6
        self.vista.append_column(self.columnaClase)

        self.columnaAutomatico = Gtk.TreeViewColumn('Automatico', self.celdaButton, active=7)
        self.columnaAutomatico.set_sort_column_id(7)
        self.columnaAutomatico.colnr = 7
        self.vista.append_column(self.columnaAutomatico)

        self.columnaMotor = Gtk.TreeViewColumn('Motor', self.celdaText, text=8)
        self.columnaMotor.set_sort_column_id(8)
        self.columnaMotor.colnr = 8
        self.vista.append_column(self.columnaMotor)

        self.columnaCaballos = Gtk.TreeViewColumn('Caballos', self.celdaText, text=9)
        self.columnaCaballos.set_sort_column_id(9)
        self.columnaCaballos.colnr = 9
        self.vista.append_column(self.columnaCaballos)

        self.boxVenta.add(self.scrollTree)


        #para o filtrado:
        self.filtrarBox=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=20)
        self.entryFiltrar=Gtk.Entry()

        self.lista_filtrar = Gtk.ListStore(int, str)

        self.lista_filtrar.append([0, "Marca"])
        self.lista_filtrar.append([1, "Modelo"])
        self.lista_filtrar.append([2, "Automatico"])
        self.lista_filtrar.append([3, "Año"])
        self.lista_filtrar.append([4, "Precio"])
        self.lista_filtrar.append([5, "Clase"])

        self.comboFiltrar = Gtk.ComboBox.new_with_model_and_entry(self.lista_filtrar)
        self.comboFiltrar.set_entry_text_column(1)

        self.botonFiltrar = Gtk.Button(label="Filtrar")
        self.botonFiltrar.connect("clicked", self.on_btnFiltrar_clicked)

        self.filtrarBox.add(self.entryFiltrar)
        self.filtrarBox.add(self.comboFiltrar)
        self.filtrarBox.add(self.botonFiltrar)

        self.boxVenta.add(self.filtrarBox)


        #botons que aparecer na parte inferior da ventá para modificar , xenerar informe, vender e sair
        self.botonesBox.add(self.botonModificar)
        self.botonesBox.add(self.botonInforme)
        self.botonesBox.add(self.botonVender)
        self.botonesBox.add(self.botonSalir)

        self.boxVenta.add(self.botonesBox)

        self.categoria = self.lista_filtrar[self.comboFiltrar.get_active()][0]


        self.show_all()



    def on_open_clicked(self,button):
        '''
        metodo que he chamado dende o stack de comprar, para engadir coches a base de datos e a taboa
        :param button: evento que ocorre ao pulsar o boton
        :return: engade unha entrada cos datos que metimos, na base de datos e na taboo da ventá venta
        '''
        #error: devolvemos true no caso de que a operacion saise ven , false no caso de que saise mal
        error=metodosBase.metodosBase.insertar_datos_coches(self,self.entryMatricula.get_text(),self.entryMarca.get_text(),
                                                      self.entryModelo.get_text(),
                                                      self.entryKm.get_text(),self.entryAno.get_text(),
                                                      self.entryPrecio.get_text(),
                                                      self.lista_clases[self.comboClases.get_active()][1],
                                                      self.checkAutomatico.get_active(),
                                                      self.entryMotor.get_text(),
                                                      self.entryCaballos.get_text(),
                                                     False)
        #se non ocurriu erro ao intentar engadir os datos na base de datos os engadimps tamen na taboa
        if(error==True):

            self.modelos.append([self.entryMatricula.get_text(), self.entryMarca.get_text(),
                                                          self.entryModelo.get_text(),
                                                          int(self.entryKm.get_text()), int(self.entryAno.get_text()),
                                                          self.entryPrecio.get_text(),
                                                          self.lista_clases[self.comboClases.get_active()][1],
                                                          self.checkAutomatico.get_active(),
                                                          self.entryMotor.get_text(),
                                                          int(self.entryCaballos.get_text())]
                                                        )
            #limpamos os entry
            self.limpar_clicked(self)

        #no caso de error mostramos un mensaxe avisando
        else:
            messageDialog = Gtk.MessageDialog(parent=self,
                                              flags=Gtk.DialogFlags.MODAL,
                                              type=Gtk.MessageType.WARNING,
                                              buttons=Gtk.ButtonsType.OK,
                                              message_format="Inserte todos los datos y no introduzca matricula repetida")
            response = messageDialog.run()
            if (response == Gtk.ResponseType.OK):
                messageDialog.destroy()



    def on_btnFiltrar_clicked(self, control):
        '''
        metodo que e chamado ao pulsar o boton filtrar
        :param control: evento que salta ao pulsar o boton
        :return: cambia o contido da taboa para mostrar so a informacion pertinente coa nosa busqueda
        '''

        #recollemos o valor polo que queremos filtrar
        self.punteiro=self.entryFiltrar.get_text()
        #recollemos a categoria pola que queremos filtrar
        self.categoria = self.lista_filtrar[self.comboFiltrar.get_active()][1]
        #recollemos o obtido na busqueda
        self.parametro_filtro_categoria = self.entryFiltrar.get_text()
        if self.parametro_filtro_categoria=="True":
            self.parametro_filtro_categoria=True
        if self.parametro_filtro_categoria=="False":
            self.parametro_filtro_categoria=False
        if self.parametro_filtro_categoria=="":
            self.parametro_filtro_categoria=None

        #chamase a refilter
        self.filtro_categoria.refilter()
        self.entryFiltrar.set_text("")




    def categoria_filtro(self, modelo,  punteiro, datos):

        '''
        en caso de que o filtro obtuvera resultados, retorna true, en caso contrario retorna false.
        comparase o campo co nombre da categoria coa que filtramos e o contido
        :return true: en caso de que devolva coincidencia
        :return false: en caso de que non sea asi
        '''

        if self.parametro_filtro_categoria is None:
            return True
        else:
            if(self.categoria=="Marca"):
                if self.modelos[punteiro][1]==self.parametro_filtro_categoria:
                    return True
                else:
                    return False
            if (self.categoria == "Modelo"):
                if self.modelos[punteiro][2] == self.parametro_filtro_categoria:
                    return True
                else:
                    return False
            if (self.categoria == "Automatico"):


                if self.modelos[punteiro][7]  == self.parametro_filtro_categoria:
                    return True
                else:
                    return False
            if (self.categoria == "Año"):
                if self.modelos[punteiro][4] == int(self.parametro_filtro_categoria):
                    return True
                else:
                    return False
            if (self.categoria == "Precio"):
                if float(self.modelos[punteiro][5]) < float(self.parametro_filtro_categoria):
                    return True
                else:
                    return False
            if (self.categoria == "Clase"):
                if self.modelos[punteiro][6] == self.parametro_filtro_categoria:
                    return True
                else:
                    return False

    def on_close_clicked(self, control):
        '''
        metodo chamado ao pulsar no boton sair, cerra a ventá actual
        :param control: evento que ocorre ao pulsar o boton
        :return: cerra a ventá actual
        '''
        Coches.destroy(self)

    def limpar_clicked(self, control):
        '''
        limpa os cadros de texto da ventá
        :param control: evento que ocorre ao pulsar o botón
        :return: None
        '''

        self.entryMatricula.set_text("")
        self.entryModelo.set_text("")
        self.entryMarca.set_text("")
        self.entryKm.set_text("")
        self.entryAno.set_text("")
        self.entryPrecio.set_text("")
        self.comboClases.set_active(0)
        self.checkAutomatico.set_active(0)
        self.entryCaballos.set_text("")
        self.entryMotor.set_text("")

    def on_pressed(self, trview, event):
        '''
        evento que ocurre ao pulsar sobre un dos elementos do treview
        :param trview: treeview enteiro, taboa onde se amosan os datos
        :param event: evento que ocurre ao pulsar
        :return: None
        recolle as cordenadas do elemento clickado no treeview

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
        salta no momento de editar unha entrada do treeview
        :param control: evento
        :param punteiro: indica a fila do treeview afectada
        :param texto: nova entrada para o campo editado
        :param modelo: modelo do tree view que foi modificado
        :return:
        '''
        #recollemos a columna na que clicamos antes
        x=int(self.x)
        #cambiamos no modelo o texto polo que introducimos novo
        modelo[punteiro][x] = texto
        #modificamos os datos na base de datos
        metodosBase.metodosBase.modificar_datos_coches(self,self.modelos[punteiro][0],self.modelos[punteiro][1]
                                                       ,self.modelos[punteiro][2],self.modelos[punteiro][3],self.modelos[punteiro][4]
                                                       ,self.modelos[punteiro][5],self.modelos[punteiro][6],self.modelos[punteiro][7]
                                                       ,self.modelos[punteiro][8],self.modelos[punteiro][9],False)
        self.celdaText.set_property("editable", False)



    def modificar_clicked(self, control):
        '''
        salta no momento de pulsar o boton modificar, o que fai e habilitar o tree view para a sua edición
        :param control: evento
        :return: None
        '''
        self.celdaText.set_property("editable", True)
        self.modificable=True


    def on_cell_toggled(self, widget, punteiro):
        '''
        salta no momento de modificar o togled button do tree view
        :param widget: widget no cal pulsamos
        :param punteiro: columna modificada
        :return:
        '''
        if(self.modificable==True):
            self.modelos[punteiro][7] = not self.modelos[punteiro][7]

            metodosBase.metodosBase.modificar_datos_coches(self, self.modelos[punteiro][0], self.modelos[punteiro][1]
                                                        , self.modelos[punteiro][2], self.modelos[punteiro][3], self.modelos[punteiro][4]
                                                        , self.modelos[punteiro][5], self.modelos[punteiro][6], self.modelos[punteiro][7]
                                                         , self.modelos[punteiro][8], self.modelos[punteiro][9],False)

            self.modificable=False

    def vender_clicked(self, evt):
        '''
        funcion que salta no momentos no que pulsamos o boton vender
        :param evt: evento
        :return: None, abre unha ventana nova para a venda do coche, e borra a fila marcada do modelo
        '''

        try:

            ventas = venta.Venta(self.modelos[self.y][0])

            selection = self.vista.get_selection()
            model, paths = selection.get_selected_rows()
            for path in paths:
                iterador = self.modelos.get_iter(path)
                self.modelos.remove(iterador)

        except:
            print("error al abrir la ventana")


    def crear_informe(self,evt):
        '''
        ao pulsar o boton informe  , xerase o informe automaticamente, para isto chamamos ao metodo da clase adecuada e mandamos un mensaxe
        :param evt: evento
        :return:None
        '''
        informeVentas.informeVentas.crear_informe(self)
        messageDialog = Gtk.MessageDialog(parent=self,
                                          flags=Gtk.DialogFlags.MODAL,
                                          type=Gtk.MessageType.WARNING,
                                          buttons=Gtk.ButtonsType.OK,
                                          message_format="Informe generado con exito")
        response = messageDialog.run()
        if (response == Gtk.ResponseType.OK):
            messageDialog.destroy()