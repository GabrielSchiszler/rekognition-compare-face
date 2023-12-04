import boto3

# Inicialize o cliente do Rekognition
rekognition_client = boto3.client('rekognition', region_name='us-east-1')

# Nome da coleção
collection_id = 'tutorial_colecao_clouddog'

# Nome do bucket do Amazon S3
bucket_name = 'tutorial-rekognition-clouddog'

# Nome da imagem no bucket
image_name = 'index_faces_image.jpg'

# Caminho da imagem no S3
s3_object = {'Bucket': bucket_name, 'Name': image_name}

# Indexação de rostos na coleção
response = rekognition_client.index_faces(
    CollectionId=collection_id,
    Image={'S3Object': s3_object}
)

# Exibe a resposta
print(f"Rostos indexados com sucesso: {response}")  