from sqlite3 import dbapi2
from sqlite3.dbapi2 import Connection, Cursor




class metodosBase:
    bbdd: Connection

    def conectar(self):


        metodosBase.bbdd = dbapi2.connect("gestionAplicacion.db")
        cursor = metodosBase.bbdd.cursor()
        # Este código de creación da base de datos. Executar só unha vez
        return cursor



    def cerrar(self):
        try:
            metodosBase.bbdd.close()
        except dbapi2.DatabaseError as erroSQL:
            print("Erro ao cerrar a conecion: "+str(erroSQL))

    def crear_tablas(self):
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""create table if not exists clientes (dni varchar primary key,nomeCompleto varchar(100),
            telefono varchar(12), direccion varchar(60),codPostal varchar(8) )""")

            cursor.execute("""create table if not exists coches (matricula varchar primary key,marca varchar(60),modelo varchar(60),
                            kilometraje float, ano int,precio float, clase varchar(20),
                             automatico boolean, motor varchar, caballos int, vendido boolean )""")

            cursor.execute("""create table if not exists ventas (matricula varchar, dni varchar, fecha datetime, 
                             primary key(matricula, dni), foreign key (matricula) references coches(matricula),
                              foreign key (dni) references clientes(dni))""")

            cursor.execute("""create table if not exists usuarios (id varchar primary key,contrasinal varchar(30) ) """)
            metodosBase.bbdd.commit()

            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroSQL:
            print("Erro na creación da base de datos: "+str(erroSQL))

        else:
            print("A base de datos creada correctamente")

    #metodos para insertar datos en cada una de las tablas

    def insertar_datos_clientes(self,dni, nome, telefono, direccion, codPostal):

        try:
            cursor = metodosBase.conectar()
            cursor.execute("""insert into clientes (dni, nome, telefono, direccion, codPostal) values (?,?,?,?,?)""", (dni, nome, telefono, direccion, codPostal))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)
        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))


    def insertar_datos_coches(self,matricula, marca, modelo, km, ano, precio, clase, automatico, motor, caballos, vendido):
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""insert into coches (matricula, marca, modelo, 
            kilometraje, ano, precio, clase, automatico, motor, caballos, vendido) values (?,?,?,?,?, ?, ?,?,?,?,?)""", (matricula, marca, modelo, km, ano, precio, clase, automatico, motor, caballos, vendido))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)
            #para indicar que non hubo erros, devolvemos unha variable booleana
            return True

        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))
            # se hubo erro devolvemos false
            return False

    def insertar_datos_ventas(self,matricula, dni, fecha):
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""insert into ventas (matricula, dni, fecha) values (?,?,?)""", (matricula, dni, fecha))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))

    def insertar_datos_usuarios(self,id, contrasinal):
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""insert into usuarios (id, contrasinal) values (?,?)""", (id, contrasinal))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))

    #metodos para borrar datos en cada una de las tablas

    def borrar_datos_clientes(self,dni):

        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""delete from clientes where dni=(?)""", dni)

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroBorrado:
            print("Erro no borrado de datos: " + str(erroBorrado))

    def borrar_datos_coches(self,matricula):
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""delete from coches where matricula=(?)""", matricula)

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroBorrado:
            print("Erro no borrado de datos: " + str(erroBorrado))

    def borrar_datos_ventas(self,matricula, dni):
        try:
            cursor = metodosBase.conectar(self)

            cursor.execute("""delete from ventas where matricula=(?) and dni=(?)""", (matricula, dni))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroBorrado:
            print("Erro no borrado de datos: " + str(erroBorrado))

    def borrar_datos_usuarios(self,id):
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""delete from usuarios where id=(?)""",id)
            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)


        except dbapi2.DatabaseError as erroBorrado:
            print("Erro no borrado de datos: "+str(erroBorrado))

    #metodos para modificar os datos en cada unha das taboas
    def modificar_datos_clientes(self,dni, nome, telefono, direccion, codPostal):

        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""update coches set dni=?, nome=?, telefono=?, direccion=?, codPostal=? where dni=?""", (dni, nome, telefono, direccion, codPostal, dni))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)
        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))

    def modificar_datos_coches(self,matricula, marca, modelo, km, ano, precio, clase, automatico, motor, caballos, vendido):
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""update coches set matricula=?, marca=?, modelo=?, kilometraje=?, 
            ano=?, precio=?, clase=?, automatico=?, motor=?, caballos=?, vendido=? where matricula=? """, (matricula, marca, modelo, km, ano, precio, clase, automatico, motor, caballos, matricula, vendido))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))

    def modificar_datoventa_coches(self, matricula,vendido):
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""update coches set  
                vendido=? where matricula=? """, (
            vendido, matricula))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))

    def modificar_datos_ventas(self,matricula, dni, fecha, compVend):
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""update ventas set matricula=?, dni=?, fecha=?, compVend=? where matricula=? and dni=?""", (matricula, dni, fecha, compVend, matricula, dni))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))

    def modificar_datos_usuarios(self,id, contrasinal):
        try:
            cursor = metodosBase.conectar(self)
            cursor.execute("""update usuarios set id=?, contrasinal=? where id=?""", (id, contrasinal, id))

            metodosBase.bbdd.commit()
            metodosBase.cerrar(self)

        except dbapi2.DatabaseError as erroInsercion:
            print("Erro na inserción de datos: " + str(erroInsercion))

    def compobrar_usuarios(self, id, contrasinal):
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
        cursor=metodosBase.conectar(self)
        resultados=cursor.execute("select * from coches where vendido=0")
        coches =tuple (resultados.fetchall())
        metodosBase.cerrar(self)
        return coches

