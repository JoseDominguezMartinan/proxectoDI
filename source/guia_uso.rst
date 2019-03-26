Guia de uso para su evaluación
******************************

Menu de enlaces:

-  `Login`_
-  `Ventana de coches`_
- `Ventana de clientes`_
- `Estructura de la base de datos`_


Login
=====
 - Usuario: *1*

 - Contraseña: *abc123.*

Uso de las ventas
=================

Ventana de coches
-----------------

En la ventana de coches podremos realizar cualquier accion sobre ellos
La ventana esta estructurada con un Stack switcher, compuesto de dos                                                                      |
ventanas, la ventana Compra, para añadir coches, y venta para el resto
de acciones.

comprar
+++++++
Ventana donde añadiremos coches a la base de datos.
En ella debemos insertar todos los datos, en caso contrario nos
saltara un aviso.
Podremos limpiar todos los campos en caso de necesitarlo.

vender
++++++
En esta ventana tenemos una lista de los coches disponibles para su venta.
No están todos los de la base de datos, dado que los coches ya vendidos los
seguimos almacenando para otros usos.
Podemos filtrar la lista de coches seleccionando una categoria en el combo box
de filtro e insertando un valor.
*Para volver a listar el contenido solo es necesario darle al botón filtrar con
el campo del valor vacio*

Para modificar una entrada es necesario seguir lo siguientes pasos:

    #. Pulsar el botón modificar.
    #. Seleccionar la fila a modificar
    #. Cambiar el campo directamente en la tabla
    #. Al pulsar intro el campo se actualizara directamente

El botón informe generará automaticamente (avisandonos de ello), un informe
con datos de las ventas de coches, tanto por marcas como por año de matricula.
El informe estará disponible automaticamente en la carpeta ventanas del proyecto.

El botón vender abrirá una nueva ventana que procederé a explicar a continuación.

ventana venta de coches
+++++++++++++++++++++++

En esta ventana procederemos a asignar una venta a un cliente, rellenando una
entrada en la base de datos, dado lo siguiente:

    #. El campo matrícula se asignará automaticamente por la fila seleccionada.Para vender otro coche se recomienda empezar el proceso desde la ventana anterior.
    #. El Dni del cliente tiene que existir en la base de datos, por tanto si no esta registrado hacerlo con anterioridad.
    #. La fecha, sera en formato DD/MM/AA , para facilitar esto, dispones de un calendario para pulsar sobre el dia que autocompleta el campo.
    #. *Al pulsar sobre vender se generará automaticamente la factura, disponible en la carpeta ventanas del proyecto*

**Nota importante: La factura contiene una imagen, que para su correcta inserción necesita la ruta absoluta, por tanto para funcionar bien tendrá que ser modificada.**

La ventana fue diseñada en Glade para abordar asi  todo el temario del curso.

Ventana de clientes
-------------------
Funcionamiento similar a la ventana de coches.
Tiene un stack con la ventana Añadir y Gestión.
La ventana añadir funcionará igual que en los coches, pudiendo limpiar y salir, y necesitando que ningún campo este en blanco.
La ventana gestión será igual que en los coches, cambiando en este caso un botón para borrar la entrada.
Los coches no podrán ser eliminados, pero los clientes si.

Estructura de la base de datos
------------------------------
En las siguientes tablas se muestra la estructura de la base de datos:


* Coches

========== ========== =========  ===========  =======  =======  =====  ==========  =====  ========  =======

Matricula   Marca     Modelo     Kilometraje   Año     Precio   Clase  Automatico  Motor  Caballos  Vendido
========== ========== =========  ===========  =======  =======  =====  ==========  =====  ========  =======
texto       texto       texto     Numero      Entero   Decimal  texto  boolean     texto  numero    boolean
========== ========== =========  ===========  =======  =======  =====  ==========  =====  ========  =======

* Clientes


========== ========== ==========  ==========  ==========  =========
DNI          Nombre     F.Nac.     Telefono   Dirección    c.postal
========== ========== ==========  ==========  ==========  =========
texto       texto       texto     texto        texto       texto
========== ========== ==========  ==========  ==========  =========

* ventas

====== ========= ====== ======
numero matricula  dni   fecha
====== ========= ====== ======
texto  texto     texto  texto
====== ========= ====== ======

* Usuarios

===== ======
ID     PASS
===== ======
texto texto
===== ======

+------------------+---------------+
|  **ID**          |   **PASS**    |
+==================+===============+
|   1              |  ABC123.      |
+------------------+---------------+


Hipervínculo
+++++++++++++
`Repositorio <https://www.github.com/josedominguezmartinan/proxectoDi>`_

:download: `Descargar esta guia <_static/exemplo.rst>`_




.. image:: logo.jpg
  :align:  left



COCHESJOSE S.L.

VENDIENDO COCHES DESDE 1994
