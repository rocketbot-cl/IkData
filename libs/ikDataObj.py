import requests
import base64
import time

class IkDataObj:
    
    def __init__(self, username, password):

        self.username = username
        self.password = password

        preEncoding = f"{username}:{password}"
        preEncodingBytes = preEncoding.encode('ascii')
        inBase64 = base64.b64encode(preEncodingBytes)
        inBaseResult = inBase64.decode('ascii')

        self.inBaseAuth = inBaseResult


    def transformToBase64(self, username, password):
        
        preEncoding = f"{username}:{password}"
        preEncodingBytes = preEncoding.encode('ascii')
        inBase64 = base64.b64encode(preEncodingBytes)
        inBaseResult = inBase64.decode('ascii')

        return inBaseResult

    def requestToken(self):
        headers = {
            "Authorization": f"Basic {self.inBaseAuth}"
            }

        r = requests.post("https://app.ikdata.co:8023/api/AuthenticationService/verifyAuthentication", headers=headers)
        print(r.status_code)
        print(r.content)
        if r.content.decode() == "false":
            self.token = ""
        else:
            self.token = r.content.decode()
    
    def sendFileToAnalyze(self, pathToFile, projectId, nameToUpload):
        
        headers = {
            "token" : self.token,
            "Accept":""
        }

        filePath = pathToFile

        data = {
            "projectID" : projectId
        }

        files = {
            ('file',(nameToUpload ,open(filePath,'rb'),'application/pdf'))
        }

        r = requests.post("https://app.ikdata.co:8023/app/UploadService/BatchReceiver", headers=headers, data=data, files=files)

        return r # true or false see status_code

    def getBatchInstances(self):
        
        headers = {
            "token" : self.token
        }
    
        r = requests.get("https://app.ikdata.co:8023/api/BatchManagementService/getBatchInstances", headers=headers)

        return r

    def getBatchInfo(self, batchId):

        headers = {
            "token" : self.token
        }

        params = {
            "batchId" : batchId
        }
        r = requests.get("https://app.ikdata.co:8023/api/BatchManagementService/getBatchInfo", headers=headers, params=params)

        return r

    def getBatchJson(self, idIknoPlus):

        headers = {
            "token" : self.token
        }

        params = {
            "batchID" : idIknoPlus
        }
        r = requests.get("https://app.ikdata.co:8023/api/ValidationService/getBatchJson", headers=headers, params=params)

        return r

    def waitForResponse(self, idIknoPlus):
        a = [{"status":""}]
        while a and a[0]["status"] not in ("VALIDATE", "OPEN"):
            responseFromApi = self.getBatchInstances().json()
            a = list(filter(lambda x: x["idIknoPlus"] == idIknoPlus, responseFromApi))
            time.sleep(2)
        # return responseFromApi
        