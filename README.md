# Bienvenido a mi primer proyecto de con Gcloud

* Este proyecto consta de dos partes.

1- Montar una app web que recoja datos introducidos por el cliente, los guarde en una base de datos, que a su vez traspase estos datos a una tabla de datos y qu se muestren por al app, todo esto con los servicios de Gcloud.

2- Realizar tanto el deployment de la cloud function y de la cloud run utilizadas para levantar toda la app, mediante dos activadores conectados a este repositorio, tal que al realizar un commit em alguna d elas carpetas asociadas se lanzen los deployments.
Lo primero es deciros como estan organizadas mis carpetas.

Come veis tenemos una archivo llamado cloudbuil_function.yml el cual hace el deployment de la funcion que necesitamos para que nuestro programa funcione bien, si observais se conecta con nuestra carpeta cloud_function.

Dentro de la carpeta de cloud_function tenemos dos archivos, un requirements.txt con las especificaciones a descargar para que el programa funcione y un main.py que es el codigo que quiero que tenga mi funcion.



Por otro lado, tenemos la carpeta cloud_run que tiene dentro el archivo cloudbuild_run.yml que es el que se encarga del deployment de la web.

Esta a su vez esta a su vez interactura con una serie de archivos (Dockerfile, web.py, requirements.txt y a su vez templates y static).

Ensi el deployement de la app lo que hace es crear una imagen con ese dockerfile junto a las especificaciones de mi web.py y los requirements.txt, a continuacion lo sube a un repo en gcloud y por ultimo lanza un cloudrun con esa imagen.



Para que esto funcion, en la cuenta que estemos trabajando de gcloud tenemos que tener los permisos necesarios para qeu pueda interactuar con los servicios de gcloud.