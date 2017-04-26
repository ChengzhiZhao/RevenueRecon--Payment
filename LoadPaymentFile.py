# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:12:21 2017

@author: Chengzhi Zhao
"""
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
with open('Payment.txt','r') as inputfile:
    for line in inputfile.readlines()[1:]:
        invoiceNumber, name, amount = line.split('|')
        nameAmount = (name, float(amount[:-1]))
        r.set(invoiceNumber, nameAmount)