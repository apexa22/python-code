# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:28:38 2021

@author: Lenovo
"""

# maximum number of activities that can be performed by a single person
def Activities(s, f ):
   n = len(f)
   print ("The selected activities are:")
   # The first activity is always selected
   i = 0
   print (i,end=" ")
   # For rest of the activities
   for j in range(n):
      # if start time is greator than or equal to that of previous activity
         if s[j] >= f[i]:
            print (j,end=" ")
            i = j
# main
s = [1, 2, 0, 3, 2, 4]
f = [2, 5, 4, 6, 8, 8]
Activities(s, f)