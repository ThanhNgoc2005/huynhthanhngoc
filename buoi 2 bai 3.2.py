# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:12:45 2024

@author: Admin
"""

a=float(input("nhap gia tri a:"))
b=float(input("nhap gia tri b:"))
c=float(input("nhap gia tri c:"))
d=float(b**2-4*a*c)
if d<0:
    print("phuong trinh vo nghiem")
elif d>0:
    print("phuong trinh co 2 nghiem phan biet:",(-b+d**0.5)/(2*a),(-b-d**0.5)/(2*a))
else:
    print("phuong trinh co nghiem kep:",-b/2*a)
    
        