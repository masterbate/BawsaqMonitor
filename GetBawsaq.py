import requests
import json


class bawsaq:
    
    def __init__(self):
        self.bawsaqInfo = {}
        self.pullInfo()
        
    def pullInfo(self):
        request = requests.get('http://grandtheftdata.com/bawsaq/api/')
        applicableInfo = json.loads(request.text)["data"]["XBOX"].itervalues().next()
        for market in applicableInfo:
            self.bawsaqInfo[str(market)] = applicableInfo[market]
            
    def getMarket(self):
        return self.bawsaqInfo
        
    def getSpecificMarket(self, market):
        if market in self.bawsaqInfo:
            return self.bawsaqInfo[market]
        return '404'
        
    def getStrongestMarket(self):
        marketValue = 0
        marketName = ''
        for market in self.bawsaqInfo:
            if self.bawsaqInfo[market] > marketValue:
                marketValue = self.bawsaqInfo[market]
                marketName = market
        return marketName + ':%s' % marketValue
        
    def refreshInfo(self):
        self.pullInfo()
        return
