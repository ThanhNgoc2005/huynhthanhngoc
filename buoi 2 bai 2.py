# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:44:01 2024

@author: Admin
"""

a=float(input("Nhap diem trung binh:"))
if a<3.5:
    print(" Hoc luc kem ")
elif a<=3.5 and a<5.0:
    print("Hoc luc yeu")
elif a<=7.0 and a<8.0:
    print("Hoc luc kha")
elif a<=8.0 and a<9.0:
    print(" Hoc luc gioi")
elif a<=9.0 and a<=10:
    print(" Hoc luc xuat sac")
else:
    print(" khong xac dinh")
    