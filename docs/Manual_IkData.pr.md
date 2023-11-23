# Ik Data
  
Envie documentos e analise-os com IA no Ik Data.  

*Read this in other languages: [English](Manual_IkData.md), [Português](Manual_IkData.pr.md), [Español](Manual_IkData.es.md)*
  
![banner](imgs/Banner_IkData.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Conecte-se ao IkData
  
Conecte-se ao IkData para começar a interagir
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome de usuário|Usuário do IkData com o qual interagir.|usuário|
|Senha|Senha do usuário do IkData.|********|
|Servidor|Servidor com o qual interagir.|https://myapp.ikdata.com:8037|
|Atribuir resultado à variável|Variável onde salvar o resultado da conexão.|Variável|

### Carregar imagem para análise
  
Carregar imagem para análise
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Seleccionar um arquivo|Caminho para o arquivo|C:/Usuario/Documentos|
|ProjectId|ProjectId com o qual você deseja analisar o documento.|4|
|Atribuir resultado à variável|Variável onde o resultado será armazenado|Variable|

### Obter Instâncias de Lotes
  
Obtém instâncias de lotes e dados.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado à variável|Variável onde salvar informações do lote.|Variável|

### Obter informações do lote
  
Obtém informações sobre um lote.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|idIknoPlus|idIknoPlus do lote que você deseja obter informações completas em json.|B4|
|Atribuir resultado à variável|Variável onde salvar informações do lote.|Variável|

### Obter lote JSON
  
Obtém informações sobre um lote.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|idIknoPlus|idIknoPlus do lote que você deseja obter informações completas em json.|B4|
|Atribuir resultado à variável|Variável onde salvar informações do lote.|Variável|
