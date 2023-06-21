# App de formulario con pipiline de despliegue automático y canalización de datos

**Este proyecto consta de dos partes.**

1- Montar una app web que recoja datos introducidos por el cliente, los guarde en una base de datos (cloud storage), que a su vez traspase estos datos a una tabla de datos (firestore/datastore) y que se muestren mediante la interfaz de la web, todo esto con los servicios de Gcloud.

2- Realizar tanto el deployment de la cloud function y de la cloud run utilizadas para levantar toda la app, mediante dos activadores conectados a este repositorio, tal que al realizar un commit en alguna de las carpetas asociadas se lanzen los deployments y por tanto se levante la web.


___Pasos a seguir___

* Primero, deberemos crear un bucket dentro de cloud storage y nuestra entidad/tabla en firestore/datastore.

* Segundo, usaremos nuestro cloudbuild_function.yml en el cual se describe el entorno usado para la funcion, la carpeta asociada a la funcion [(cloud_function)](cloud_function), el trigger que queremos utilizar para que se active la funcion y la region.

* Tercero, usaremos nuestro archivo cloudbuild_run.yml, en el que especificamos el deployment, este primero configura el entorno, luego crea la imagen a partir de la carpeta [(cloud_run)](cloud_run), sube la imagen a un repo de gcloud y por ultimo la despliga con las especificaciones descritas alli.


Por ultimo, dentro de cada carpeta hay un ReadMe que explica màs detalladamente dicha parte en cuestion. Espero que os ayude.
