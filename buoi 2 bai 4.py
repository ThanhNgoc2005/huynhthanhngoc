# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:41:36 2024

@author: Admin
"""

a=float(input("nhap canh a:"))
b=float(input("nhap canh b:"))
c=float(input("nhap canh c:"))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("a,b,c la 3 canh tam giac va day la tam giac deu")
    elif a==b or c==b or a==c:
        print("a,b,c la 3 canh tam giac va la tam giac can")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("a,b,c la 3 canh tam giac va la tam giac vuong")
    else:
        print("a,b,c la 3 canh cua tam giac")
else:
        print("a,b,c khong la 3 canh cua tam giac")
         