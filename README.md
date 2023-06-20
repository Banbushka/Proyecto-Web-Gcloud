# Este es el readme de mi proyecto de goglecloud. Bienvenido.
## El ejercicio trata de montar una app formulario, que recoja datos mediante un html los guarde en modo json en un bucket de google storage y que mediante una cloud function se guarde automaticamente en una tabla de firestore. Por ultimo nos muestra los datos guardados en nuestra web.
## La segunda parte del ejercicio es que todo este se realize mediante un cloud build conectado a este repositorio, para que se active cuando se ejecute un commit en la rama de main.
Lo primero es deciros como estan organizadas mis carpetes.
Come veis tenemos una archivo llamado cloudbuil_function.yml el cual hace el deployment de la funcion que necesitamos para que nuestro programa funcione bien, si observais se conecta con nuestra carpeta cloud_function.
Dentro de la carpeta de cloud_function tenemos dos archivos, un requirements.txt con las especificaciones a descargar para que el programa funcione y un main.py que es el codigo que quiero que tenga mi funcion.

Por otro lado, tenemos la carpeta cloud_run que tiene dentro el archivo cloudbuild_run.yml que es el que se encarga del deployment de la web.
Esta a su vez esta a su vez interactura con una serie de archivos (Dockerfile, web.py, requirements.txt y a su vez templates y static).
Ensi el deployement de la app lo que hace es crear una imagen con ese dockerfile junto a las especificaciones de mi web.py y los requirements.txt, a continuacion lo sube a un repo en gcloud y por ultimo lanza un cloudrun con esa imagen.

Para que esto funcion, en la cuenta que estemos trabajando de gcloud tenemos que tener los permisos necesarios para qeu pueda interactuar con los servicios de gcloud.