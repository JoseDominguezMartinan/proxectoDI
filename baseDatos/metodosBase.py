from sqlite3 import dbapi2
from sqlite3.dbapi2 import Connection, Cursor




class metodosBase:
    bbdd: Connection

    def conectar(self):
        '''
        xera a conexion coa base de datos
        :return: None
        '''

        metodosBase.bbdd = dbapi2.connect("gestionAplicacion.db")
        cursor = metodosBase.bbdd.cursor()
        # Este código de creación da base de datos. Executar só unha vez
        return cursor



    def cerrar(self):
        '''
        cerra a conexion coa base de datos
        :return:None
        '''
        try:
            metodosBase.bbdd.close()
        except dbapi2.DatabaseError as erroSQL:
            print("Erro ao cerrar a conecion: "+str(erroSQL))

    def crear_tablas(self):
        '''
        metodo para xerar as taboas da base de datos
        :return: None
        '''
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""create table if not exists clientes (dni varchar primary key,nomeCompleto varchar(100),
            fechaNac varchar, telefono varchar(12), direccion varchar(60),codPostal varchar(8) )""")

            cursor.execute("""create table if not exists coches (matricula varchar primary key,marca varchar(60),modelo varchar(60),
                            kilometraje float, ano int,precio float, clase varchar(20),
                             automatico boolean, motor varchar, caballos int, vendido boolean )""")

            cursor.execute("""create table if not exists ventas (numVenta integer primary key autoincrement, matricula varchar, dni varchar, fecha datetime 
                             , foreign key (matricula) references coches(matricula),
                              foreign key (dni) references clientes(dni))""")

            cursor.execute("""create table if not exists usuarios (id varchar primary key,contrasinal varchar(30) ) """)
            metodosBase.bbdd.commit()

            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroSQL:
            print("Erro na creación da base de datos: "+str(erroSQL))

        else:
            print("A base de datos creada correctamente")

    #metodos para insertar datos en cada una de las tablas

    def insertar_datos_clientes(self,dni, nome,fecha, telefono, direccion, codPostal):
        '''
        metodo para insertar datos na taboa clientes
        :param dni: dni do cliente
        :param nome: nome do cliente
        :param fecha: fecha de nacemento
        :param telefono: telefono do cliente
        :param direccion: direccion do cliente
        :param codPostal: codigo postal do clietne
        :return: None
        '''

        try:
            if(dni!="" and nome!="" and fecha!="" and telefono!="" and direccion!="" and codPostal!=""):
                cursor = metodosBase.conectar(self)
                cursor.execute("""insert into clientes (dni, nomeCompleto,fechaNac, telefono, direccion, codPostal) values (?,?,?,?,?,?)""", (dni, nome,fecha, telefono, direccion, codPostal))

                metodosBase.bbdd.commit()
                metodosBase.cerrar(self)
                return True
            else:
                return False
        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))
            return False


    def insertar_datos_coches(self,matricula, marca, modelo, km, ano, precio, clase, automatico, motor, caballos, vendido):
        '''
        metodo para insertar datos na taboa coches
        :param matricula: matricula do coche
        :param marca: marca do coche
        :param modelo: modelo do coche
        :param km: kilometrajo do coche no momento da compra
        :param ano: ano de matriculacion do coche
        :param precio: precio de venda do coche
        :param clase: categoria do coche , vai dende a (ultracompacto) ata todoterrenos
        :param automatico: booleano, si e true o coche ten transmision automatica, se e false non
        :param motor: cilindrada do coche
        :param caballos: caballaxe do coche
        :param vendido: os coches con este booleano a true non estan dispoñibles para a sua venda
        :return: True en caso de que se fixera todo ben , false en caso de ocorrer un erro
        '''
        try:
            if(matricula!="" and marca!="" and modelo!="" and km!="" and ano!=""
                    and precio!="" and clase!="" and automatico!=""
                    and motor!=""and caballos!="" and vendido!=""):
                cursor = metodosBase.conectar(self)
                cursor.execute("""insert into coches (matricula, marca, modelo, 
                kilometraje, ano, precio, clase, automatico, motor, caballos, vendido) values (?,?,?,?,?, ?, ?,?,?,?,?)""", (matricula, marca, modelo, km, ano, precio, clase, automatico, motor, caballos, vendido))

                metodosBase.bbdd.commit()
                metodosBase.cerrar(self)
                #para indicar que non hubo erros, devolvemos unha variable booleana
                return True
            else:
                return False

        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))
            # se hubo erro devolvemos false
            return False

    def insertar_datos_ventas(self,matricula, dni, fecha):
        '''
        metodo para insertar datos na taboa de ventas
        :param matricula: matricula do coche vendido
        :param dni: dni do cliente que adquiriu o coche
        :param fecha: fecha na que se vendeu o vehiculo
        :return: None
        '''
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""insert into ventas (matricula, dni, fecha) values (?,?,?)""", (matricula, dni, fecha))
            numVenta=cursor.execute("Select MAX(numVenta)AS maximo from ventas").fetchall()
            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)
            return numVenta


        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))

    def insertar_datos_usuarios(self,id, contrasinal):
        '''
        metodos para insertar datos na taboa de usuarios
        :param id: identificador de usuario
        :param contrasinal: contrasinal para acceder ao sistema
        :return: None
        '''
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""insert into usuarios (id, contrasinal) values (?,?)""", (id, contrasinal))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))

    #metodos para borrar datos en cada una de las tablas

    def borrar_datos_clientes(self,dni):
        '''
        metodo para borrar os datos da taboa clientes
        :param dni: dni do cliente a borrar
        :return: None
        '''

        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""delete from clientes where dni=(?)""", (dni,))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroBorrado:
            print("Erro no borrado de datos: " + str(erroBorrado))

    def borrar_datos_coches(self,matricula):
        '''
        metodo para borrar entradas da taboa coches
        :param matricula:matricula do coche a borrar
        :return: None
        '''
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""delete from coches where matricula=(?)""", (matricula,))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroBorrado:
            print("Erro no borrado de datos: " + str(erroBorrado))

    def borrar_datos_ventas(self,matricula, dni):
        '''
        metodo para borrar datos da taboa ventas
        :param matricula: matricula do coche do que queremos borrar os datos
        :param dni: dni do cliente
        :return: None
        '''
        try:
            cursor = metodosBase.conectar(self)

            cursor.execute("""delete from ventas where matricula=(?) and dni=(?)""", (matricula, dni))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroBorrado:
            print("Erro no borrado de datos: " + str(erroBorrado))

    def borrar_datos_usuarios(self,id):
        '''
        borrar datos dos usuarios
        :param id: identificador de usuario
        :return: None
        '''
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""delete from usuarios where id=(?)""",(id,))
            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)


        except dbapi2.DatabaseError as erroBorrado:
            print("Erro no borrado de datos: "+str(erroBorrado))

    #metodos para modificar os datos en cada unha das taboas
    def modificar_datos_clientes(self,dni, nome,fecha, telefono, direccion, codPostal):
        '''
        modificar os datos dun cliente marcado
        :param dni: dni do cliente
        :param nome: nome do cliente
        :param fecha: fecha de nacemento do cliente
        :param telefono: telefono do cliente
        :param direccion: direccion do cliente
        :param codPostal: codigo postal do cliente
        :return: None
        '''

        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""update clientes set dni=?, nomeCompleto=?,fechaNac=?, telefono=?, direccion=?, codPostal=? where dni=?""", (dni, nome,fecha, telefono, direccion, codPostal, dni))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)
        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))

    def modificar_datos_coches(self,matricula, marca, modelo, km, ano, precio, clase, automatico, motor, caballos, vendido):
        '''
        modificar datos da taboa de datos coches
        :param matricula: matricula do coche a modificar
        :param marca: marca do coche a modificar
        :param modelo: modelo do coche
        :param km: kilometraje do coche
        :param ano: ano de matriculacion
        :param precio: precio de venta
        :param clase: clase do coche
        :param automatico: booleano que indica si e automatico(true) ou non (false)
        :param motor: cilindrada do coche
        :param caballos: potencia do cochen
        :param vendido: boolean True o coche xa foi vendido False non
        :return: None
        '''
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""update coches set matricula=?, marca=?, modelo=?, kilometraje=?, 
            ano=?, precio=?, clase=?, automatico=?, motor=?, caballos=?, vendido=? where matricula=? """, (matricula, marca, modelo, km, ano, precio, clase, automatico, motor, caballos, matricula, vendido))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))

    def modificar_datoventa_coches(self, matricula,vendido):
        '''
        metodo para marcar que un coche foi vendido despois de facer esta operacion
        :param matricula: matricula do coche a modificar
        :param vendido: dato de vendido true ou false
        :return: None
        '''
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""update coches set  
                vendido=? where matricula=? """, (
            vendido, matricula))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))

    def modificar_datos_ventas(self,matricula, dni, fecha):
        '''
        metodo para modificar os datos sobre a venda dun vehiculo
        :param matricula: matricula do coche vendido
        :param dni: dni do dono do coche
        :param fecha: fecha de venta

        :return: None
        '''
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""update ventas set matricula=?, dni=?, fecha=? where matricula=? and dni=?""", (matricula, dni, fecha, matricula, dni))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))

    def modificar_datos_usuarios(self,id, contrasinal):
        '''
        metodo para modificar os datos dun usuario
        :param id: identificador do usuario
        :param contrasinal: contrasinal do usuario
        :return: None
        '''
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""update usuarios set id=?, contrasinal=? where id=?""", (id, contrasinal, id))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))

    def compobrar_usuarios(self, id, contrasinal):
        '''
        metodo para comprobar que o usuario introducido e contrasinal coincida con algun da base de datos
        :param id: identificador insertado
        :param contrasinal: contrasinal insertado
        :return: True en caso de que exista o usuario, False en caso contrario
        '''
        try:
            cursor = metodosBase.conectar(self)
            resultados = cursor.execute("select count(*) from usuarios where id=? and contrasinal=?", (id,contrasinal)).fetchall()
            metodosBase.cerrar(self)
            print(resultados[0][0])

            if(resultados[0][0]>0):
                return True
            else:
                return False


        except dbapi2.DatabaseError as erroConsulta:
            print("Erro na consulta de datos: " + str(erroConsulta))

    def listar_coches(self):
        '''
        metodo para listar os coches todos da base de datos que non haxan sido vendidos, co fin de mostralos no programa para a sua venta
        :return: Coches, lista de todos os coches dispoñibles na base de datos
        '''
        cursor=metodosBase.conectar(self)
        resultados=cursor.execute("select * from coches where vendido=0")
        coches =tuple (resultados.fetchall())
        metodosBase.cerrar(self)
        return coches

    def listar_coches_matricula(self, matricula):
        '''
        metodo para listar os coches por unha matricula determinada
        :param matricula: matricula do coche a encontrar
        :return: Coches, lista cos datos da coincidencia atopada
        '''
        cursor = metodosBase.conectar(self)
        resultados = cursor.execute("select * from coches where matricula=?", (matricula,))
        coches = tuple(resultados.fetchall())
        metodosBase.cerrar(self)
        return coches

    def listar_clientes(self):
        '''
        metodo para listar os clientes da base de datos
        :return: Clientes, lista cos datos do clientes
        '''
        cursor = metodosBase.conectar(self)
        resultados = cursor.execute("select * from clientes")
        clientes = tuple(resultados.fetchall())
        metodosBase.cerrar(self)
        return clientes

    def listar_clientes_dni(self,dni):
        '''
        metodo para listar os clientes cun dni concreto
        :param dni: dni do cliente a buscar
        :return: clientes, lista cos datos do cliente
        '''
        cursor = metodosBase.conectar(self)
        resultados = cursor.execute("select * from clientes where dni=?",(dni,))
        clientes = tuple(resultados.fetchall())
        metodosBase.cerrar(self)
        return clientes

    def listar_ventas_marca(self):
        '''
        metodo para listar as ventas agrupandoas pola marca
        :return: coches, lista cos datos dos coches
        '''
        cursor=metodosBase.conectar(self)
        resultados=cursor.execute("select count (matricula), marca from coches where vendido=1 group by marca")
        coches = tuple(resultados)


        metodosBase.cerrar(self)
        return coches

    def listar_ventas_anoMatricula(self):
        '''
        lista de coches agrupado polo ano de matriculacion
        :return: coches, lista de datos dos coches agrupados por ano
        '''
        cursor=metodosBase.conectar(self)
        resultados=cursor.execute("select count (matricula), ano from coches where vendido=1 group by ano")
        coches = tuple(resultados)


        metodosBase.cerrar(self)
        return coches