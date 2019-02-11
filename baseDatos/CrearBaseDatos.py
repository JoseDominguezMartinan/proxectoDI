from sqlite3 import dbapi2
from sqlite3.dbapi2 import Connection, Cursor

bbdd: Connection
cursor: Cursor


def conectar():

    bbdd = dbapi2.connect("gestionAplicacion.dat")
    cursor = bbdd.cursor()
    # Este código de creación da base de datos. Executar só unha vez


def crear_tablas():
    try:
        cursor.execute("""create table if not exists clientes (dni varchar primary key,nomeCompleto varchar(100),
        telefono varchar(12), direccion varchar(60),codPostal varchar(8)""") #Comilla triple

        cursor.execute("""create table if not exists coches (matricula varchar primary key,marca varchar(60),modelo varchar(60),
                        kilometraje float, ano int,precio float, clase varchar(20) )""")  # Comilla triple

        cursor.execute("""create table if not exists ventas (matricula varchar, dni varchar, fecha datetime, 
                        compVend varchar(10), primary key(matricula, dni) )""")  # Comilla triple

        cursor.execute(""""create table if not exists usuarios (id varchar primary key, contrasinal varchar) """)

    except dbapi2.DatabaseError as erroSQL:
        print("Erro na creación da base de datos: "+str(erroSQL))

    else:
        print("A base de datos creada correctamente")

#metodos para insertar datos en cada una de las tablas

def insertar_datos_clientes(dni, nome, telefono, direccion, codPostal):

    try:
        cursor.execute("""insert into clientes (dni, nome, telefono, direccion, codPostal) values (?,?,?,?,?)""", (dni, nome, telefono, direccion, codPostal))

        bbdd.commit()
    except dbapi2.DatabaseError as erroInsercion:
        print("Erro na inserción de datos: " + str(erroInsercion))


def insertar_datos_coches(matricula, marca, modelo, km, ano, precio, clase):
    try:
        cursor.execute("""insert into coches (matricula, marca, modelo, 
        kilometraje, ano, precio, clase) values (?,?,?,?,?, ?, ?)""", (matricula, marca, modelo, km, ano, precio, clase))

        bbdd.commit()

    except dbapi2.DatabaseError as erroInsercion:
        print("Erro na inserción de datos: " + str(erroInsercion))


def insertar_datos_ventas(matricula, dni, fecha, compVend):
    try:
        cursor.execute("""insert into ventas (matricula, dni, fecha, compVend) values (?,?,?,?)""", (matricula, dni, fecha, compVend))

        bbdd.commit()

    except dbapi2.DatabaseError as erroInsercion:
        print("Erro na inserción de datos: " + str(erroInsercion))

def insertar_datos_usuarios(id, contrasinal):
    try:
        cursor.execute("""insert into usuarios (id, contrasinal) values (?,?)""", (id, contrasinal))

        bbdd.commit()

    except dbapi2.DatabaseError as erroInsercion:
        print("Erro na inserción de datos: " + str(erroInsercion))


#metodos para borrar datos en cada una de las tablas

def borrar_datos_clientes(dni):

    try:
        cursor.execute("""delete from clientes where dni=(?)""", dni)

        bbdd.commit()
    except dbapi2.DatabaseError as erroBorrado:
        print("Erro no borrado de datos: " + str(erroBorrado))


def borrar_datos_coches(matricula):
    try:
        cursor.execute("""delete from coches where matricula=(?)""", matricula)

        bbdd.commit()

    except dbapi2.DatabaseError as erroBorrado:
        print("Erro no borrado de datos: " + str(erroBorrado))


def borrar_datos_ventas(matricula, dni):
    try:
        cursor.execute("""delete from ventas where matricula=(?) and dni=(?)""", (matricula, dni))

        bbdd.commit()

    except dbapi2.DatabaseError as erroBorrado:
        print("Erro no borrado de datos: " + str(erroBorrado))


def borrar_datos_usuarios(id):
    try:
        cursor.execute("""delete from usuarios where id=(?)""",id)
        bbdd.commit()

    except dbapi2.DatabaseError as erroBorrado:
        print("Erro no borrado de datos: "+str(erroBorrado))


#metodos para modificar os datos en cada unha das taboas
def modificar_datos_clientes(dni, nome, telefono, direccion, codPostal):

    try:
        cursor.execute("""update coches set dni=?, nome=?, telefono=?, direccion=?, codPostal=? where dni=?""", (dni, nome, telefono, direccion, codPostal, dni))

        bbdd.commit()
    except dbapi2.DatabaseError as erroInsercion:
        print("Erro na inserción de datos: " + str(erroInsercion))


def modificar_datos_coches(matricula, marca, modelo, km, ano, precio, clase):
    try:
        cursor.execute("""update coches set matricula=?, marca=?, modelo=?, kilometraje=?, 
        ano=?, precio=?, clase=? where matricula=? """, (matricula, marca, modelo, km, ano, precio, clase, matricula))

        bbdd.commit()

    except dbapi2.DatabaseError as erroInsercion:
        print("Erro na inserción de datos: " + str(erroInsercion))


def modificar_datos_ventas(matricula, dni, fecha, compVend):
    try:
        cursor.execute("""update ventas set matricula=?, dni=?, fecha=?, compVend=? where matricula=? and dni=?""", (matricula, dni, fecha, compVend, matricula, dni))

        bbdd.commit()

    except dbapi2.DatabaseError as erroInsercion:
        print("Erro na inserción de datos: " + str(erroInsercion))


def modificar_datos_usuarios(id, contrasinal):
    try:
        cursor.execute("""update usuarios set id=?, contrasinal=? where id=?""", (id, contrasinal, id))

        bbdd.commit()

    except dbapi2.DatabaseError as erroInsercion:
        print("Erro na inserción de datos: " + str(erroInsercion))

