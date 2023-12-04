import boto3

# Inicialize o cliente do Rekognition
rekognition_client = boto3.client('rekognition', region_name='us-east-1')

# Nome da coleção
collection_id = 'tutorial_colecao_clouddog'

# Criação da coleção
response = rekognition_client.create_collection(
    CollectionId=collection_id
)

# Exibe a resposta
print(f"Coleção '{collection_id}' criada com sucesso: {response}")
