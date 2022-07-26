# Proyecto_final
ENTREGA DEL PROYECTO FINAL.-

Esta es una Página Web ---- >>> "Bazar Enzo". 
Lo hice con el proposito personal, para darle utilidad en un emprendimiento familiar, y para poder practicar mas en profundidad este hermoso mundo de la programación.

# Documentacion
Este es un proyecto, planteado por CODERHOUSE donde la idea de la entrega es implementar lo aprendido en la cursada de PYTHON.
Donde utilizamos el framework de Django, y templates provenientes de Bootstrap para darle un buen formato a la APP, ya que el fuerte nuestro no es el front-end, sino el backend.Adaptamos esta visualizacion usando la herencia de padre a hijo para altenar las diferentes vistas.

# models.py
En este archivo se encuentra los modelos de datos usado para el backend del ingreso de stock al bazar, busqueda laboral, y pedidos por encargue. Tambien se encuentra el @models.py/ bazar donde se encuentra todo lo agregado desde la web o la bd.

# views.py
Acá encontraremos las vistas creadas y moldeadas para la navegacion de la web. Entre algunas tenemos:

#Inicio: Es la pantalla de inicio de la aplicacion #bazar  #buscar producto # pedidos por encargue # busqueda laboral. Tambien encuentran vistas, que requieren de usuarios con permisos de modificar bd o la web en si . Por Ejemplo #agregar Bazar : Es la Vista para la Administracion de los precios, imagenes , etc  del Porfolio Los siguientes son las funcionalidades CRUD  #eliminar_bazar #editar_bazar

# forms.py
En este archivo se encuentra el formulario que hace envio de los datos ingresados al backend para el Registro de datos del bazar. Llamados BazarFormulario  es el Forms para el formulario del agregado.
///formularioPedidoMayor es el formulario para le encargue de un articulo que busca el cliente. 
///Postulacion es el formulario para una postulacion de busqueda laboral.

Tenemos UserRegisterForm y UserEditForm Para el manejo de los Usuarios dentro del sistema

# urls.py
Archivo donde está la configuración de rutas para las Vistas de la Web del Bazar.

# templates
En esta carpeta encontraras todos los HTML configurados para el funcionamiento y visualización de la APP. en todos se utilizo Herencia por Django y manejo de datos.

# Autor
@ Quiroga, Maximiliano
@Estudiante de Ing. en Electronica (orientacion en Redes)
@Tecnico Superior en Energía (orientacion industrial)
@Tecnico en Electrónica
@LinkedIn : https://www.linkedin.com/in/maximiliano-quiroga-711b9b219
