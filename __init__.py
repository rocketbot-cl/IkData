# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import sys

GetParams = GetParams # type: ignore
SetVar = SetVar # type: ignore
PrintException = PrintException # type: ignore

base_path = tmp_global_obj["basepath"] # type: ignore
cur_path = base_path + 'modules' + os.sep + 'ikData' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from ikDataObj import IkDataObj # type: ignore

global ikData_I

module = GetParams("module")

try:

    if (module == "connectToIkData"):

        username = GetParams("username")
        password = GetParams("password")
        server = GetParams("server")
        
        ikData_I = IkDataObj(username, password, server)

        ikData_I.requestToken()

        resultConnection = False

        if ikData_I.token != "":
            resultConnection = True
        
        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultConnection)

    if (module == "sendFileToAnalyze"):
        
        fileToUpload = GetParams("fileToUpload")
        projectId = GetParams("projectId")
        nameToUpload = GetParams("nameToUpload")

        fileToUpload = fileToUpload.replace("\\", "/")

        if not nameToUpload:
            nameToUpload = fileToUpload.split("/")[-1]

        resultAnalyze = ikData_I.sendFileToAnalyze(fileToUpload, projectId, nameToUpload).content.decode()

        isItUploaded = False

        ikData_I.waitForResponse(resultAnalyze)

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultAnalyze)

    if (module == "getBatchInstances"):
        
        resultBatchInstances = ikData_I.getBatchInstances().json()

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultBatchInstances)

    if (module == "getBatchInfo"):

        idIknoPlus = GetParams("idIknoPlus")
        
        resultBatchInfo = ikData_I.getBatchInfo(idIknoPlus).json()

        if resultBatchInfo == "Non-existent batch":
            raise Exception("Non-existent batch")

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultBatchInfo)

    if (module == "getBatchJson"):

        idIknoPlus = GetParams("idIknoPlus")
        
        resultBatchJson = ikData_I.getBatchJson(idIknoPlus).json()

        if resultBatchJson == "":
            raise Exception("Non-existent batch")

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultBatchJson)

except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
    PrintException()
    raise e
