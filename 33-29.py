# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 22:35:03 2024

@author: PC
"""

def question_33(nums: list[int]) -> tuple[int, int]:
    s=sorted(set(nums))
    return (s[-2],s[4]) if len(s)>4 else None

def question_34(s: str) -> int:
    ds,dodai_ln, trai=set(),0,0
    for phai in range(len(s)):
        while s[phai] in ds:
            ds.remove(s[trai])
            trai+=1
        ds.add(s[phai])
        dodai_ln=max(dodai_ln, phai-trai+1)
    return dodai_ln

def question_35(s: str) -> str:
    for i in range(len(s),0,-1):
        for j in range(len(s)-i+1):
            if s[j:j+i] in s[j+1:]:
                return s[j:j+i]
    return ""

def question_36(nums: list[int]) -> list[list[int]]:
    if len(nums)==1:
        return [nums[:]]
    kq=[]
    for i in range(len(nums)):
        for p in question_36(nums[:i]+nums[i+1:]):
            kq.append([nums[i]]+p)
    return kq

def question_37(s: str) -> bool:
    danh_sach=[]
    quy_dinh={"(":")","{":"}","[":"]"}
    for i in s:
        if i in quy_dinh:
            danh_sach.append(i)
        elif not danh_sach or quy_dinh[danh_sach[-1]]!=i:
            return False
    if not danh_sach:
        return True
    else:
        return False

def question_38(n: int) -> int:
    if n==1:
        return 1
    a,b=1,1 
    for i in range(2,n+1):
        a,b=b,a+b
    return b 

def question_39(prices: list[int]) -> int:
    gia_nn=float("inf")
    loinhuan_ln=0
    for i in prices:
        if i<gia_nn:
            gia_nn=i
        elif i- gia_nn>loinhuan_ln:
            loinhuan_ln=1-gia_nn
    return loinhuan_ln 
    