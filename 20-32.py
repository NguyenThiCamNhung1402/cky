# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 22:48:56 2024

@author: PC
"""

from typing import Optional
def question_20() -> Optional[str]:
    n=input("Nhập:")
    if not n:
        return None
    return n

def question_21(nums: list[int], target: int) -> Optional[tuple[int, int]]:
    n =set()
    for i in nums:
        number=target-i
        if number in n :
            return (number,i)
        n.add(i)
    return None

def question_22(nums: list[int]) -> None:
    so_khac_khong=[i for i in nums if i!=0]
    so_khong= nums.count(0)
    return so_khac_khong + ([0]*so_khong)

def question_23(nums: list[int]) -> bool:
    if len(nums)!= len(set(nums)):
        return True
    else:
        return False
    
def question_24(nums: list[int]) -> int:
    for i in nums :
        if nums.count(i) > (len(nums)//2):
            return i

def question_25(nums: list[int]) -> list[int]:
    ds=[i**2 for i in nums ]
    return sorted(ds)

def question_26(s: str) -> int:
    ktu=set()
    do_dai=0 
    for i in range(len(s)):
        if s[i] in ktu:
            ktu.remove(s[i])
            do_dai+=2
        else:
            ktu.add(s[i])
    if ktu:
        do_dai+=1
    return do_dai

def question_27(strs: list[str]) -> str:
    if not strs:
        return ""
    tien_to=strs[0]
    for i in range(1,len(strs)):
        while tien_to and tien_to!= strs[i][:len(tien_to)]:
            tien_to=tien_to[:-1]
            if not tien_to:
                return ""
    return tien_to
from typing import Dict 
def question_28(s: str) -> Dict[str, int]:
    dem={}
    for i in range(len(s)):
        if s[i] in dem:
            dem[s[i]]+=1
        else:
            dem[s[i]]=1
    return dem 
from typing import Optional, List, Tuple 
def question_29(nums: List[int]) -> Optional[Tuple[int, int]]:
    s= sorted(nums)
    n= len(s)
    if n%2==0:
        return (s[n//2-1]+s[n//2])/2
    else:
        return s[n//2]

def question_30(paragraph: str) -> Dict[str, int]:
    tach=paragraph.split()
    kq={}
    for i in tach:
        if i not in kq:
            kq[i]=tach.count(i)
    return kq

def question_31(paragraph: str, n: int) -> List[str]:
    tach=paragraph.split()
    dem={}
    for i in tach:
        if i in dem:
            dem[i]+=1
        else:
            dem[i]=1
    kq=[]
    for i in dem:
        if (dem[i]/len(tach))>0.2 :
            kq.append(i)
    return kq[:n] if len(kq)>=n else []

def question_32(nums: List[int]) -> Tuple[List[int], List[int]]:
    so_chan=sorted([i for i in nums if i%2==0],reverse=True)
    so_le=sorted([i for i in nums if i%2!=0])
    return so_chan, so_le 

            
