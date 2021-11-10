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
        



# "EXPECTATION_FAILED"
if __name__ == "__main__":

    ikData_I = IkDataObj("rocketbot", "eeb7aLah#")
    ikData_I.requestToken()
    ikData_I.waitForResponse("B84")

    # username = "rocketbot"
    # password = "eeb7aLah#"

    # preEncoding = f"{username}:{password}"
    # preEncodingByes = preEncoding.encode('ascii')
    # inbase = base64.b64encode(preEncodingByes)
    # inbaseMessage = inbase.decode('ascii')
    # headers = {
    #     "Authorization": "Basic cm9ja2V0Ym90OmVlYjdhTGFoIw=="
    #     }

    # r = requests.post("https://app.ikdata.co:8023/api/AuthenticationService/verifyAuthentication", headers=headers)

    # # print(r.content)
    # print(r.content)
    # print(r.status_code)
    # token = r.content.decode()
    # print(token)

    # # headers = {
    # #     "token" : f"{token}",
    # #     "Content-Type": "multipart/form-data"
    # # }

    # headers = {
    #     "token" : f"{token}",
    #     "Accept":""
    # }

    # filePath = "C:/Users/Caleb/Downloads/Manual_SystemPlus_ES.pdf"

    # data = {
    #     "projectID" : '4'
    # }

    # files = {
    #     ('file',('probandoManual.pdf',open(filePath,'rb'),'application/pdf'))
    # }

    # r2 = requests.post("https://app.ikdata.co:8023/app/UploadService/BatchReceiver", headers=headers, data=data, files=files)

    # print(r2.content)
    # print(r2.text)
    # print(r2.status_code)
    # print(headers)
    # print(data)

    # # headers = {
    # #     "token" : f"{token}"
    # #     }

    # # r3 = requests.get("https://app.ikdata.co:8023/api/BatchManagementService/getBatchInstances", headers=headers)

    # # print(r3.content)
    # # print(r3.text)
    # # print(r3.status_code)

    # # headers = {
    # #     "token" : f"{token}"
    # # }

    # # params = {
    # #     "batchId" : "55"
    # # }
    # # r4 = requests.get("https://app.ikdata.co:8023/api/BatchManagementService/getBatchInfo", headers=headers, params=params)

    # # print(r4.content)
    # # print(r4.text)
    # # print(r4.status_code)

    # # headers = {
    # #     "token" : f"{token}"
    # # }

    # # headers = {
    # #     "token" : "748cf43e49ac8cd7a1c1b3769d44a437eee4151e"
    # # }

    # # params = {
    # #     "batchID" : "B58"
    # # }
    # # r5 = requests.get("https://app.ikdata.co:8023/api/ValidationService/getBatchJson", headers=headers, params=params)

    # # print(r5.content)
    # # print(r5.text)
    # # print(r5.status_code)
