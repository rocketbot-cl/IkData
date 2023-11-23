# Ik Data
  
Envíe documentos y analícelos con IA en Ik Data.  


  
![banner](imgs/Banner_IkData.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Conectar a IkData
  
Conecta a IkData para empezar a interactuar
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de usuario|Usuario de IkData con el cual interactuar.|usuario|
|Password|Password del usuario de IkData|********|
|Servidor|Servidor con el cual interactuar.|https://myapp.ikdata.com:8037|
|Asignar resultado a variable|Variable donde guardar el resultado de la conexion.|Variable|

### Subir imagen para analizar
  
Subir una imagen para analizar
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seleccionar un archivo|Ruta donde está el archivo|C:/Usuario/Documentos|
|ProjectId|ProjectId con el cual se quiere analizar el documento.|4|
|Asignar resultado a variable|Variable donde se guardará el resultado|Variable|

### Instancias de lotes
  
Obtiene las instancias de lotes con sus datos.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a variable|Variable donde guardar el resultado de los lotes.|Variable|

### Información de lote
  
Obtiene información de un lote en específico.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|idIknoPlus|idIknoPlus del lote que se desea obtener completamente en json.|B4|
|Asignar resultado a variable|Variable donde guardar el resultado de los lotes.|Variable|

### Información de lote completo en JSON
  
Obtiene completa información de un lote en específico en formato JSON.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|idIknoPlus|idIknoPlus del lote que se desea obtener completamente en json.|B4|
|Asignar resultado a variable|Variable donde guardar el resultado de los lotes.|Variable|
