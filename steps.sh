### STEP GITHUB

###########################################################################################################################
## ATENÇÃO: Antes de executar esse script, realize o commit para não perder alterações não salvas.                       ##
## ATENÇÃO: Altere <my-branch> pelo nome da sua branch   >>>>>    exemplo: feature/my-branch                             ##
## ATENÇÃO: Não subir as alterações desse arquivo <steps.sh> para a branch e nem para o repositório remoto               ##
## ATENÇÃO: Para executar esse arquivo, abrir o terminal do git bash na raiz desse diretorio e executar o comando abaixo ##
########### ~> steps.sh                                                                                         ###########
###########################################################################################################################


# 1. Selecione a sua branch
git checkout -B <my-branch>

# 2. Execute o comando git fetch para baixar as alterações mais recentes do repositório remoto.
git fetch

# 3. Execute o comando git pull para baixar as alterações mais recentes do repositório remoto e mesclá-las com a sua branch local.
git pull

# 4. Altere para a branch develop
git checkout -B develop

# 5. Execute o comando git fetch para baixar as alterações mais recentes do repositório remoto.
git fetch

# 6. Execute o comando git pull para baixar as alterações mais recentes do repositório remoto e mesclá-las com a sua branch local.
git pull

# 7. Altere para a branch pessoal
git checkout -B <my-branch>

# 8. Execute o comando git merge para mesclar as alterações da branch develop com a sua branch pessoal.
git merge develop

# 9. Resolva os conflitos, se houver.

# 10. Suba as alterações para o repositório remoto.

# 11. Criei um pull request para a branch develop.      ex.  feature/my-branch  ->  develop

# 12. Crie um pull request para a branch main.          ex.  develop  ->  main

