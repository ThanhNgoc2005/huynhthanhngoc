# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:12:47 2024

@author: Admin
"""

e = float(input("Nhập số km quãng đường đi được: "))

if e >= 0:
    if e <= 1 : 
        tongtien = 20
    elif e <= 3:
        tongtien = 20 + 13*(e-1) 
    elif e <= 8 :
        tongtien = 20 + 13*(e-1) + 12*(e-3)
    else:
        tongtien = 20 + 13*(e-1) + 12*(e-3) + 10*(e-8)
    if tongtien >= 100 :
        tongtien = tongtien*(1 - 8/100)  
    print(f"Tổng tiền taxi cần trả là {tongtien:.0f}k")
else:
    print("Không xác định")