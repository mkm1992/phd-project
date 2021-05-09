# -*- coding: utf-8 -*-
"""
Created on Wed May  5 11:40:48 2021

@author: 
"""

import zeep

wsdl = "https://wsvc.cdiscount.com/MarketplaceAPIService.svc?wsdl"
client = zeep.Client(wsdl=wsdl)
print(client.service.Method1('Zeep', 'is cool'))