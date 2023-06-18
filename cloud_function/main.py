from google.cloud import storage
from google.cloud import firestore
import json

def function_uwee(event, context):

        # Obtener el nombre del archivo JSON creado en Cloud Storage
        bucket_name = 'uwee'  # Cambiar el nombre del bucket aquí
        file_name = event['name']

        # Crear una instancia del cliente de Cloud Storage
        storage_client = storage.Client()

        # Obtener el objeto JSON desde Cloud Storage
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        json_data = blob.download_as_text()

        # Convertir el JSON a un diccionario de Python
        data = json.loads(json_data)

        # Guardar los datos en Cloud Firestore
        firestore_client = firestore.Client()
        collection = firestore_client.collection('users')
        collection.document().set(data)

        return 'Datos guardados en Cloud Firestore'
