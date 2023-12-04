
# Implementando Reconhecimento Facial usando Amazon Rekognition

Este repositório contém scripts Python para interagir com o serviço Amazon Rekognition. Cada script realiza uma etapa específica.

## Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Além disso, instale a biblioteca boto3 usando o seguinte comando:

```bash
pip install boto3
```

### Configuração do AWS Credentials
Antes de executar os scripts, configure suas credenciais da AWS. Você pode fazer isso configurando um arquivo ~/.aws/credentials ou exportando variáveis de ambiente. Certifique-se de ter permissões suficientes para usar o serviço Amazon Rekognition.

1. Criar uma Coleção
O script create_collection.py cria uma coleção no Amazon Rekognition.

```bash
python create_collection.py
```

2. Indexar Rostos em uma Coleção
O script index_faces.py faz upload de uma imagem para o Amazon S3 e indexa os rostos na coleção.

```bash
python index_faces.py
```

3. Comparar Rostos em uma Coleção
O script search_faces.py faz upload de uma segunda imagem e compara os rostos com a coleção.

```bash
python search_faces.py
```

### Blog
Para instruções detalhadas, consulte o [Blog Post](https://multilingue.dev.clouddog.com.br/blog/implementando-reconhecimento-facil-usando-amazon-rekognition/).