# Link acesso ao projeto Azure
https://projeto-final-impacta-rs.azurewebsites.net/

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

# Link vídeo explicativo da entrega final:
https://www.loom.com/share/a0be2c82b15c44328e974436f4aaf9a0

# Alunos do grupo:
Lucas dos Santos: lucas.dossantos@aluno.faculdadeimpacta.com.br
Robson Soares Sobrinho: robson.sobrinho@aluno.faculdadeimpacta.com.br
Thais Fernanda Melo Santos: thais.melo@aluno.faculdadeimpacta.com.br
Thiago Gomes da Silva: thiago.gomes@aluno.faculdadeimpacta.com.br
Thiago Machado Pereira: thiago.machado@aluno.faculdadeimpacta.com.br

# Link do board do projeto no trello:
https://trello.com/b/Y6YbFWiV/projeto-final-impacta-teste-para-recrutamento-e-sele%C3%A7%C3%A3o-de-candidatos

# Link do projeto no Github:
https://github.com/Projeto-Final-Impacta-RS/Projeto-Final-Impacta-RS

