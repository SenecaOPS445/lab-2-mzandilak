#!/usr/bin/env python3
'''
Author:  Maryam Zandilak
Author ID:  mzandilak
Date Created:  2024/05/21

'''
import sys

if len(sys.argv) != 2:
    count = 3 
else:
    count = int(sys.argv[1])
    
while count!= 0:
        print(count)
        count= count - 1

print('blast off!')
