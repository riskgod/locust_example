#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from locust import HttpLocust, TaskSet, task
import json

with open('./vender/assignAgentData.json') as assignAgent:
    assignAgentData = json.load(assignAgent)

with open('./vender/finalQuotationData.json') as finalQuotation:
    finalQuotationData = json.load(finalQuotation)

with open('./vender/createPaData.json') as createPa:
    createPaData = json.load(createPa)

with open('./vender/createPsData.json') as createPs:
    createPsData = json.load(createPs)

with open('./vender/createPfcData.json') as createPfc:
    createPfcData = json.load(createPfc)

with open('./vender/submitEsubData.json') as submitEsub:
    submitEsubData = json.load(submitEsub)

with open('./vender/addmailData.json') as addmail:
    addmailData = json.load(addmail)

with open('./vender/finalComputeAllData.json') as finalComputeAll:
    finalComputeAllData = json.load(finalComputeAll)


def webPageLoad(l):
    print(l);
    r = l.client.get("/d2c", verify=False)

def getRandomAndRSAPublicKey(l):
    r = l.client.get("/d2c-service/getRandomAndRSAPublicKey", verify=False)

def quotation(l):
    r = l.client.post("/d2c-service/quotation", {"reqType":"PS", "occupationCode":"", "residencyCode":"1", "age":"1"}, verify=False)
        
def assignAgent(l):
    l.client.post("/d2c-service/assignAgent", assignAgentData, verify=False)

def finalQuotation(l):
    l.client.post("/d2c-service/finalQuotation", finalQuotationData, verify=False)    

def createPa(l):
    l.client.post("/d2c-service/createPa", createPaData, verify=False)    

def createPs(l):
    l.client.post("/d2c-service/createPs", createPsData, verify=False)

def createPfc(l):
    l.client.post("/d2c-service/createPfc", createPfcData, verify=False)    

def submitEsub(l):
    l.client.post("/d2c-service/submitEsub", submitEsubData, verify=False)  

def computeAll(l):
    l.client.post("/d2c-service/computeAll", {"age":"34", "gender":"M", "smoker":False, "selectedTerm":15, "selectedOptionCode":3, "selectedOptionVal": 2, "totalYearlyPremium": 6000, "sumAssured": 0.0}, verify=False)

def fetchAppData(l):
    l.client.post("/d2c-service/fetchAppData", {"erefNo": "11905CODNG01"}, verify=False)    

def occupationList(l):
    l.client.post("/d2c-service/occupationList", { "reqType": "PA", "occupationCode": "1"}, verify=False)      

def occupationSpecial(l):
    l.client.post("/d2c-service/occupationSpecial", { "occupationId": "APER"}, verify=False)  

def dropdowns(l):
    l.client.post("/d2c-service/dropdowns", { "dropDownCode": "PFCOPT066"}, verify=False)  

def financials(l):
    l.client.post("/d2c-service/financials", { "dropDownCode": "OCB"}, verify=False)  

def addmail(l):
    l.client.post("/d2c-service/addmail", addmailData, verify=False)  

def postalcode(l):
    l.client.post("/d2c-service/postalcode", { "postalCode": "649185" }, verify=False)  

def makepayment(l):
    l.client.post("/d2c-service/makepayment", {"amt":"6045.78", "ref":"03137CODNG01", "cur":"SGD", "returnUri":"/payment_return"}, verify=False)

def finalComputeAll(l):
    l.client.post("/d2c-service/finalComputeAll", finalComputeAllData, verify=False)    

def uploadImage(l):
    l.client.post("/d2c-service/uploadImage", data={'docfile': open('./vender/test.jpg', 'rb')}, verify=False)


class UserBehavior(TaskSet):
    tasks = {webPageLoad: 1, getRandomAndRSAPublicKey: 1, quotation: 1, assignAgent: 1, finalQuotation: 1, createPa: 1, createPs: 1, createPfc: 1, submitEsub: 1, computeAll: 1, fetchAppData: 1, occupationList: 1, dropdowns: 1, financials: 1, addmail: 1, postalcode: 1, uploadImage: 1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 30000