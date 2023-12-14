import requests
import base64
import time
import traceback

class IkDataObj:
    
    def __init__(self, username, password, server):
        self.username = username
        self.password = password
        self.server = server
        self.server = server

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

        r = requests.post(f"{self.server}/api/AuthenticationService/verifyAuthentication", headers=headers)
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

        r = requests.post(f"{self.server}/app/UploadService/BatchReceiver", headers=headers, data=data, files=files)

        return r # true or false see status_code

    def getBatchInstances(self):
        
        headers = {
            "token" : self.token
        }
    
        r = requests.get(f"{self.server}/api/BatchManagementService/getBatchInstances", headers=headers)

        return r

    def getBatchInfo(self, batchId):

        headers = {
            "token" : self.token
        }

        params = {
            "batchId" : batchId
        }
        r = requests.get(f"{self.server}/api/BatchManagementService/getBatchInfo", headers=headers, params=params)

        return r

    def getBatchJson(self, idIknoPlus):

        headers = {
            "token" : self.token
        }

        params = {
            "batchID" : idIknoPlus
        }
        r = requests.get(f"{self.server}/api/ValidationService/getBatchJson", headers=headers, params=params)

        return r

    def waitForResponse(self, idIknoPlus):
        a = {"status":""}

        while a and a["status"] not in ("VALIDATE", "OPEN"):
            print(a["status"])
            try:
                a = self.getBatchInfo(idIknoPlus).json()
            except Exception as e:
                traceback.print_exc()
                print(e)
            time.sleep(2)

            if a["status"] == "ERROR":
                raise Exception("An error ocurred uploading the file. Please check the response in your IkData server.")

        # return responseFromApi
        
