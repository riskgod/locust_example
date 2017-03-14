#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from locust import HttpLocust, TaskSet, task
import json

with open('./assignAgentData.json') as assignAgent:
    assignAgentData = json.load(assignAgent)

with open('./finalQuotationData.json') as finalQuotation:
    finalQuotationData = json.load(finalQuotation)

with open('./createPaData.json') as createPa:
    createPaData = json.load(createPa)

with open('./createPsData.json') as createPs:
    createPsData = json.load(createPs)

with open('./createPfcData.json') as createPfc:
    createPfcData = json.load(createPfc)

with open('./submitEsubData.json') as submitEsub:
    submitEsubData = json.load(submitEsub)

with open('./addmailData.json') as addmail:
    addmailData = json.load(addmail)

with open('./finalComputeAllData.json') as finalComputeAll:
    finalComputeAllData = json.load(finalComputeAll)


def qp(l):
    l.client.get("/qp")

def getRandomAndRSAPublicKey(l):
    l.client.get("/getRandomAndRSAPublicKey")

def quotation(l):
    l.client.post("/quotation", {"reqType":"PS", "occupationCode":"", "residencyCode":"1", "age":"1"})

def assignAgent(l):
    l.client.post("/assignAgent", assignAgentData)

def finalQuotation(l):
    l.client.post("/finalQuotation", finalQuotationData)    

def createPa(l):
    l.client.post("/createPa", createPaData)    

def createPs(l):
    l.client.post("/createPs", createPsData)

def createPfc(l):
    l.client.post("/createPfc", createPfcData)    

def submitEsub(l):
    l.client.post("/submitEsub", submitEsubData)  

def computeAll(l):
    l.client.post("/computeAll", {"age":"34", "gender":"M", "smoker":False, "selectedTerm":15, "selectedOptionCode":3, "selectedOptionVal": 2, "totalYearlyPremium": 6000, "sumAssured": 0.0})

def fetchAppData(l):
    l.client.post("/fetchAppData", {"erefNo": "11905CODNG01"})    

def occupationList(l):
    l.client.post("/occupationList", { "reqType": "PA", "occupationCode": "1"})      

def occupationSpecial(l):
    l.client.post("/occupationSpecial", { "occupationId": "APER"})  

def dropdowns(l):
    l.client.post("/dropdowns", { "dropDownCode": "PFCOPT066"})  

def financials(l):
    l.client.post("/financials", { "dropDownCode": "OCB"})  

def addmail(l):
    l.client.post("/addmail", addmailData)  

def postalcode(l):
    l.client.post("/postalcode", { "postalCode": "649185" })  

def makepayment(l):
    l.client.post("/makepayment", {"amt":"6045.78", "ref":"03137CODNG01", "cur":"SGD", "returnUri":"/payment_return"})

def finalComputeAll(l):
    l.client.post("/finalComputeAll", finalComputeAllData)    

@task
def uploadImage(self):
    response = self.client.get("/uploadImage")
    csrftoken = response.cookies['csrftoken']
    attach = open('./img.jpg', 'rb')

    r = self.client.post("/uploadImage", data={
        'csrfmiddlewaretoken': csrftoken,
        'password': smart_str(u'wkefjgui'),
        'payload': smart_str(u'kjsdgfljdsh'),
        'commit': smart_str(u'Вкрапить / Embed'),
         }, files={'docfile': attach})


class UserBehavior(TaskSet):
    tasks = {qp: 1, getRandomAndRSAPublicKey: 1, quotation: 1, assignAgent: 1, finalQuotation: 1, createPa: 1, createPs: 1, createPfc: 1, submitEsub: 1, computeAll: 1, fetchAppData: 1, occupationList: 1, dropdowns: 1, financials: 1, addmail: 1, postalcode: 1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000