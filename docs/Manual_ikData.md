



# Ik Data
  
Envia documentos a IkData para ser analizados y extraer información.
  
![banner](imgs/Modulo_IKData.jpg)

## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.

## Como usar este módulo
  
Para utilizar este módulo tienes que tener cuenta habilitada para usar con Ik Data. Tienes que tener los proyectos ya creados que analizaran los documentos en la misma plataforma.

## Descripción de los comandos

### Conectar a IkData
  
Conecta a IkData para empezar a interactuar
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de usuario|Usuario de IkData con el cual interactuar.|usuario|
|Password|Password del usuario de IkData|********|
|Asignar resultado a variable|Variable donde guardar el resultado de la conexion.|Variable|

### Subir imagen para analizar
  
Subir una imagen para analizar
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seleccionar un archivo||C:/Usuario/Documentos|
|ProjectId|ProjectId con el cual se quiere analizar el documento.|4|
|Nombre con el cual subir|Nombre con el cual se desea subir a la plataforma (adicionalmente tendra un timestamp en el nombre).|4|
|Asignar resultado a variable||Variable|

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
