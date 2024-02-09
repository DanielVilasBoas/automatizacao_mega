# Projeto de Automatização de Processamento de Dados da Mega-Sena

Este projeto visa automatizar o processo de coleta, processamento e armazenamento de dados da Mega-Sena. Através de uma série de scripts Python, o projeto baixa os resultados dos sorteios, organiza-os, e os insere em um banco de dados para análise posterior.

## Estrutura do Projeto

-  <b>Scripts Python:</b> Os scripts individuais estão organizados em diretórios lógicos dentro da estrutura do projeto.
-  <b>Arquivos de Configuração:</b> O arquivo <b>'requirements.txt'</b> lista as dependências do projeto, enquanto o  <b>'.gitignore'</b> exclui arquivos e diretórios desnecessários do versionamento Git.
-  <b>Documentação:</b> Incluí comentários nos scripts para explicar o propósito de cada função e módulo. Além disso, o arquivo <b>'README.md'</b> contém instruções sobre como configurar e executar o projeto.

## Como Usar

1.  Configuração do Ambiente:
-    Instale as dependências do projeto listadas no arquivo requirements.txt.
-    Certifique-se de ter um banco de dados MySQL configurado e acessível.

2.   Execução dos Scripts:
-    Execute o script principal <b>executar_scripts.py</b> para iniciar o processo de automatização.
-    Este script executa sequencialmente os seguintes scripts: <b>baixar_resultados.py, apagar_tabela.py, gerar_db.py e popular_db.py</b>.

3. Contribuição:
-  Sinta-se à vontade para contribuir com novas funcionalidades, correções de bugs ou melhorias na documentação. Abra um <i>Pull Request</i> e aguarde a revisão.
