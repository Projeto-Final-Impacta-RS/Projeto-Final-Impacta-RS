
# Rodar o projeto local
python manage.py runserver

# Acessar opções para configurações do Django
python manage.py

# Criar uma imagem docker
docker build --tag projeto_final_impacta_rs:latest .

# Criar um container docker para rodar local
docker run --name projeto_final_impacta_rs -d -p 8000:8000 projeto_final_impacta_rs:latest

# Criar um tag docker para publicar em um container registry
docker tag projeto_final_impacta_rs projetofinalimpactars.azurecr.io/projeto_final_impacta_rs:latest

# Publicar a imagem no container registry
docker push projetofinalimpactars.azurecr.io/projeto_final_impacta_rs:latest

