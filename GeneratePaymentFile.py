# -*- coding: utf-8 -*-
import names
import random
invoiceStartNumber = 1000
amountRange = 100
    
with open("Payment.txt", "w") as file:
    for i in range(0,100):
        name = names.get_full_name()
        amount = round(random.random()*amountRange*random.choice([1,-1]),2)
        file.write(str(invoiceStartNumber + i) + '|' + name + '|' + str(amount)+'\n')
    
