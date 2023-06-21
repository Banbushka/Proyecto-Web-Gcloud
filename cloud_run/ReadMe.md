# Descripcion de archivos relacionados a nuestra cloud run.

1- Dentro de esta carpeta tenemos unos cuantos archivos: Un Dockerfile, un web.py, un requirements.txt, y dos carpetas un static y un templates.

2- Lo primero seria el Dockerfile el cual es el encargado de contruir un imagen, con base de python, en la cual se copiara el web.py, la carpeta templates y la carpeta static y el archivos requirements.txt, luego este instalara los requirements y ejecutara el web.py.

3- El archivo web.py es nuestra app como tal, la cual interactua con los servicios de gcloud para el guardado y procesado de datos, esta se complementa con un index.html que esta dentro de templates y con un styles.css que esta dentro del static y lo que hacen es dar una interfaz a nuestra app y dejarla chula.

