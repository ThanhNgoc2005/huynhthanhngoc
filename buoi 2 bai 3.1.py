# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:45:42 2024

@author: Admin
"""
a=float(input("nhap gia tri a:"))
b=float(input("nhap gia tri b:"))
if a==0:
    print("phuong trinh vo nghiem")
elif a>0:
    print("phuong trinh co nghiem la ",-b/a)
else:
    print("phuong trinh có nghiem la ",b/a)