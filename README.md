
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
O script create-collection.py cria uma coleção no Amazon Rekognition.

```bash
python create-collection.py
```

2. Indexar Rostos em uma Coleção
O script index-collection.py indexa os rostos de uma foto do bucket s3 na coleção do rekognition.

```bash
python index-collection.py
```

3. Comparar Rostos em uma Coleção
O script search-faces-by-image.py compara os rostos de uma fot odo bucket s3 com a coleção do rekognition.

```bash
python search-faces-by-image.py
```

### Blog
Para instruções detalhadas, consulte o [Blog Post](https://multilingue.dev.clouddog.com.br/blog/implementando-reconhecimento-facil-usando-amazon-rekognition/).