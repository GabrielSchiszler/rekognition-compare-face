import boto3

# Inicialize o cliente do Rekognition
rekognition_client = boto3.client('rekognition', region_name='us-east-1')

# Nome da coleção
collection_id = 'tutorial_colecao_clouddog'

# Nome do bucket do Amazon S3
bucket_name = 'tutorial-rekognition-clouddog'

# Nome da imagem no bucket para comparação
source_image_name = 'compare_image.jpg'

# Caminho da imagem no S3
source_s3_object = {'Bucket': bucket_name, 'Name': source_image_name}

# Comparação de rostos na coleção
response = rekognition_client.search_faces_by_image(
    CollectionId=collection_id,
    Image={'S3Object': source_s3_object}
)

# Exibe a resposta
print(f"Comparação de rostos com sucesso: {response}")
