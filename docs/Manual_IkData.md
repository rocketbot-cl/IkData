# Ik Data
  
<<<<<<< HEAD:docs/Manual_ikData.md
Send documents and analyze them with AI on Ik Data.  
=======
Envia documentos a IkData para ser analizados y extraer información.
  
![banner](imgs/Modulo_IKData.jpg)

>>>>>>> 08ad4a087d9ade36ab028733c13e89235eb5d484:docs/Manual_IkData.md

*Read this in other languages: [English](Manual_IkData.md), [Português](Manual_IkData.pr.md), [Español](Manual_IkData.es.md)*
  
<<<<<<< HEAD:docs/Manual_ikData.md
![banner](imgs/Banner_IkData.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  
=======
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.  


>>>>>>> 08ad4a087d9ade36ab028733c13e89235eb5d484:docs/Manual_IkData.md


## Description of the commands

### Connect to IkData
  
Connects to IkData for interactions
|Parameters|Description|example|
| --- | --- | --- |
<<<<<<< HEAD:docs/Manual_ikData.md
|Username|User from IkData that you want to interact with.|username|
|Password|Password of username from IkData.|********|
|Server|Server that you want to interact with.|https://myapp.ikdata.com:8037|
|Assign result to variable|Variable where to save conection result.|Variable|
=======
|Nombre de usuario|Usuario de IkData con el cual interactuar.|usuario|
|Password|Password del usuario de IkData|********|
|Servidor|Servidor con el cual interactuar.|https://myapp.ikdata.com:8037|
|Asignar resultado a variable|Variable donde guardar el resultado de la conexion.|Variable|
>>>>>>> 08ad4a087d9ade36ab028733c13e89235eb5d484:docs/Manual_IkData.md

### Upload image to analyze
  
Upload an image to analyze
|Parameters|Description|example|
| --- | --- | --- |
|Select a file|Path to file|C:/User/Documents|
|ProjectId|ProjectId with you want to analyze the document.|4|
|Assign result to variable|Variable where the result will be stored|Variable|

### Get Batch Instances
  
Obtains batch instances and data.
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to variable|Variable where to save batch info.|Variable|

### Get Batch Info
  
Obtains info about a batch.
|Parameters|Description|example|
| --- | --- | --- |
|idIknoPlus|idIknoPlus of the batch you want to obtain complete information in json.|B4|
|Assign result to variable|Variable where to save batch info.|Variable|

### Get Batch JSON
  
Obtains info about a batch.
|Parameters|Description|example|
| --- | --- | --- |
|idIknoPlus|idIknoPlus of the batch you want to obtain complete information in json.|B4|
|Assign result to variable|Variable where to save batch info.|Variable|
