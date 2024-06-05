# Smart_Entregas
Desenvolvimento de uma prova de conceito de sistema de logística e gestão de entregas de pacotes “última milha” em um ambiente pequeno, e uma plataforma móvel de transporte capaz de realizar as entregas em si. Através de um software gerencial, utilizado pelo porteiro do condomínio para cadastrar encomendas recebidas no nome de um morador.

## Tutorial: Ativando Ambiente Virtual, Dockerfile e Instalando Pacotes Python

Neste tutorial, você aprenderá como ativar um ambiente virtual Python (venv), como construir e executar uma imagem Docker usando um Dockerfile e como instalar pacotes Python de um arquivo `requirements.txt` usando o pip.

### Ativando Ambiente Virtual (venv)

#### Criar Ambiente Virtual

Para criar um ambiente virtual Python, execute o seguinte comando no terminal:

```bash
python3 -m venv nome_do_ambiente
```
## Ativar Ambiente Virtual
Para ativar o ambiente virtual, use o comando apropriado para o seu sistema operacional:
- No Linux ou macOS:
```bash
source nome_do_ambiente/bin/activate
```
- Para Windows
```bash
nome_do_ambiente\Scripts\activate
```

## Dockerfile
#### Construir Imagem Docker
Para construir uma imagem Docker usando um Dockerfile, siga estas etapas:

1. Crie um Dockerfile na raiz do seu projeto com as instruções para construir sua imagem Docker.

2. No terminal, navegue até o diretório do seu projeto onde o Dockerfile está localizado.

3. Execute o seguinte comando para construir a imagem Docker:

```bash
docker build -t nome_da_imagem .
```

## Executar Contêiner Docker
Após construir a imagem Docker, você pode executar um contêiner usando a imagem:

```bash
docker run -it nome_da_imagem
```

# Instalação de Pacotes Python a partir de requirements.txt
Para instalar pacotes Python a partir de um arquivo requirements.txt usando o pip, execute o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```
