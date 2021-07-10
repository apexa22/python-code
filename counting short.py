# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:33:38 2021

@author: Lenovo
"""

def main():
    t = input()
    w = raw_input()
    w = w.split()
    for i in range(100):
        print w.count((str)(i)),
    
if __name__ == '__main__':
    main()