# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:12:21 2017

@author: Chengzhi Zhao
"""
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
#Store Rule data in Redis as key value pair, make multiple ID as a tuple as a key
with open ('Rule.txt','r') as inputfile:
    for line in inputfile.readlines()[1:]:
        RuleGroupID,RuleID,TypeID,FieldName = line.split('|')
        ruleID = (int(RuleGroupID),int(RuleID),int(TypeID))
        r.set('Rule:'+str(ruleID),FieldName[:-1])

#Store Rule Relationship Data        
with open ('RuleRelationship.txt','r') as inputfile:
    for line in inputfile.readlines()[1:]:
        RuleGroupID,RuleID,NextRuleGroupID,NextRuleID,Parenthesis,LogicalOperation = line.split('|')
        ruleID = (int(RuleGroupID),int(RuleID))
        nextRuleID = (int(0 if NextRuleGroupID == '' else NextRuleGroupID),int(0 if NextRuleID == '' else NextRuleID))
        ruleConcatenation = (Parenthesis,LogicalOperation)
        r.set('RuleRelationship:' + str(ruleID), (nextRuleID,ruleConcatenation))
        
#Get some Data!!
with open('Payment.txt','r') as inputfile:
    for line in inputfile.readlines()[1:]:
        invoiceNumber, name, amount = line.split('|')
        nameAmount = (name, float(amount[:-1]))
        r.set('Payment:' + invoiceNumber, nameAmount)