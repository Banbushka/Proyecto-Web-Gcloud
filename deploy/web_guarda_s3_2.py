from flask import Flask, render_template, request, redirect, url_for
import boto3
import json
import time


app = Flask(__name__)

# Configura la conexión a S3
s3_client = boto3.client('s3')
bucket_name = 'dinamodebejercicio'  # Reemplaza con el nombre de tu bucket en S3

# configura la conexion a dinamodb
dynamodb = boto3.resource('dynamodb')
table_name = 'users'  # Reemplaza con el nombre de tu tabla en DynamoDB
table = dynamodb.Table(table_name)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtiene los datos ingresados en el formulario
        id = int(request.form['id'])  # Convierte el campo 'ID' a un número entero
        nombre = request.form['nombre']
        correo = request.form['correo']
        fecha = request.form['fecha']

        # Crea el objeto JSON con los datos del usuario
        usuario = {
            "ID": id,
            "Nombre": nombre,
            "Correo electrónico": correo,
            "Fecha de registro": fecha
        }

        # Genera un nombre único para el archivo JSON utilizando la fecha y hora actual
        timestamp = int(time.time())  # Obtiene la marca de tiempo actual en segundos
        file_name = f'datos_{timestamp}.json'  # Nombre del archivo JSON

        # Guarda el objeto JSON en S3
        s3_client.put_object(
            Body=json.dumps(usuario),
            Bucket=bucket_name,
            Key=file_name
        )

        time.sleep(4)
        # Redirecciona a la misma página para recargar
        return redirect(url_for('index'))


    # Obtiene todos los usuarios de la tabla en DynamoDB
    response = table.scan()
    users = response['Items']

    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run()
