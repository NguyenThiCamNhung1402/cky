# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:46:54 2024

@author: PC
"""

def question_1(n:int)-> bool:
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
#print(question_1(4  ))

from typing import Tuple 
import random 
def question_2(n:int)-> Tuple[int,float]:
    ds=[random.randint(1,100 ) for i in range(n)]
    tong=sum(ds)
    trung_binh=tong/n
    return tong, trung_binh 
#print(question_2(5 ))

from typing import Tuple 
def question_3(s:str)->Tuple [int,int]:
    kt_hoa=0
    kt_thuong=0
    for i in s:
        if i.isupper():
            kt_hoa+=1
        elif i.islower():
            kt_thuong+=1
    return kt_hoa, kt_thuong 
#print(question_3("Python Programming"))

def question_4(n:int)-> bool:
    return n%2==0
#print(question_4(7 ))

from typing import Optional 
def question_5(lst:list,x:int)-> Optional[int]:
    if x in lst:
       return lst.index(x)
    return None 
#lst=[10,20,30,40 ]
#print(question_5(lst,25 ))

def question_6(n:int)-> int:
    giai_thua=1
    for i in range(1,n+1  ):
        giai_thua*=i
    return giai_thua
#print(question_6(7 ))

import random
def question_7(n:int)->(float,float):
    ds=[random.uniform(0,1) for i in range(n)]
    so_lon_nhat=max(ds)
    so_nho_nhat=min(ds)
    return so_lon_nhat, so_nho_nhat
#print(question_7(5))

def question_8(s:str )->str:
    return s[::-1 ]
#n =input("Nhập chuỗi cần đảo:")
#print(question_8(n ))

def question_9(s:str) -> bool:
    bien_doi="".join([s[i].lower() for i in range(len(s)) if s[i].isalnum()])
    return bien_doi== bien_doi[::-1 ]
#print(question_9("race a car"))

from typing import Optional , List 
def question_10()-> Optional[List[int]]: 
    ds=input("Nhập danh sách:").split()
    ds=[int(i) for i in ds ]
    if not ds:
        return None
    return ds
#print(question_10())

def question_11(n:int)-> int:
    if n<0:
        return "Nhập sai"
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        a,b=0,1
        for i in range(2,n+1):
            a,b=b,a+b
        return b
#print(question_11(5 ))

import random 
def question_12()-> bool:
    n= random.randint(1,1000 )
    print("Số ngẫu nhiên:",n )
    if n<= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
#print(question_12())

def question_13(s:str)-> int:
    n=s.split()
    return len(n)
#print(question_13(" This is a test. " ))

def question_14(s:str)-> bool:
    return s.isdigit()
#print(question_14("0123"))

def question_15(value)->bool:
    return value is None
#print(question_15(10 ))

def question_16(*args ) -> float:
    if not args :
        return None
    return sum(args )/len(args )
#print(question_16(1,2,3,4,5 ))

import random 
def question_17(n:int) -> list:
    ds=[random.randint(1,100) for i in range(n)]
    ds.sort(reverse=True)
    return ds 
#print(question_17(5 ))

def question_18(s:str) -> str:
    return " ".join(s.split())
#print(question_18("  Hello  world!  "))

def question_19(x:int,n:int)-> bool:
    return x>n
#print(question_19(5,10 ))

from typing import Optional 
def question_20() -> Optional[str]:
    n=input("Nhập giá trị:")
    if n=="":
        return None
    return n
#print(question_20())

from typing import Optional 
def question_21(nums: list[int], target: int) -> Optional[tuple[int, int]]:
    n=set() 
    for i in nums:
        number= target -i 
        if number  in n:
            return (number, i )
        n.add(i )
    return None
nums= [2,7,11,15 ]
target= 9 
#print(question_21(nums, target ))

def question_22(nums:list[int])->None:
    so_khac_khong= [i for i in nums if i!=0]
    so_khong= nums.count(0)
    return so_khac_khong + ([0]*so_khong)
nums=[0,1,0,3,12 ]
#print(question_22(nums))

def question_23(nums:list[int]) -> bool:
    return len(nums) != len(set(nums))
nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
#print(question_23(nums))

def question_24(nums:list[int]) -> int:
    for i in nums:
        if nums.count(i) > (len(nums)/2):
            return i
nums=[2, 2, 1, 1, 1, 2, 2]
#print(question_24(nums))

from typing import List  
def question_25(nums: list[int]) -> list[int]:
    n= [i**2 for i in nums ]
    return sorted(n)
nums = [-4, -1, 0, 3, 10]
#print(question_25(nums))

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
#print(question_26("bb" ))

def question_27(strs: list[str]) -> str:
    if not strs:
        return ""
    tien_to=strs[0 ]
    for i in range(1,len(strs)):
        while tien_to and tien_to != strs[i][:len(tien_to)]:
            tien_to=tien_to[:-1]
            if not tien_to:
                return ""
    return tien_to 
strs=["dog", "racecar", "car"]
#print(question_27(strs))

from typing import Dict 
def question_28(s: str) -> Dict[str, int]:
    dem={}
    for i in range(len(s)):
        if s[i] in dem:
            dem[s[i]] += 1
        else:
            dem[s[i]]=1
    return dem 
#print(question_28("test"))

from typing import Optional, List, Tuple 
def question_29(nums: List[int]) -> Optional[Tuple[int, int]]:
    nums.sort()
    n= len(nums  )
    if n%2==0:
        return (nums[n//2-1] + nums[n//2])/2 
    else:
        return nums[n//2]
nums=[1,3,4,2,5 ]
#print(question_29(nums))
 
from typing import Dict  
def question_30(paragraph: str) -> Dict[str, int]:
    tach = paragraph.split()
    kq = {}
    for i  in tach:
        if i  not in kq:
            kq[i ] = tach.count(i )
    return kq
#print(question_30("hello world hello"))

from typing import List 
def question_31(paragraph: str, n: int) -> List[str]:
    tach= paragraph.split()
    dem={}
    for i in tach:
        if i in dem:
            dem[i]+=1
        else:
            dem[i]=1
    kq=[]
    for i in dem:
        if (dem[i]/ len(tach ))>0.2:
            kq.append(i)
    return kq[:n] if len(kq)>=n else []
paragraph = "apple apple banana orange orange apple"
n = 2
#print(question_31(paragraph, n ))

from typing import List, Tuple 
def question_32(nums: List[int]) -> Tuple[List[int], List[int]]:
   so_chan=sorted([i for i in nums if i%2==0],reverse=True)
   so_le=sorted([i for i in nums if i%2!=0])
   return so_chan, so_le 
nums = [4, 1, 3, 2, 7, 8, 5]
#print(question_32(nums ))

def question_33(nums: list[int]) -> tuple[int, int]:
    s=sorted(set(nums))
    return (s[-2],s[4]) if len(s)>4 else None 
nums = [1, 3, 2, 5]
#print(question_33(nums))

def question_34(s: str) -> int:
    ds, dodai_ln, trai = set(),0,0 
    for phai in range(len(s)):
        while s[phai] in ds:
            ds.remove(s[trai])
            trai+=1 
        ds.add(s[phai])
        dodai_ln= max(dodai_ln, phai-trai+1)
    return dodai_ln        
#print(question_34("pwwkew"))
#print(question_34("abcabcbb"))

def question_35(s: str) -> str:
    for i in range(len(s),0,-1):
        for j in range(len(s)-i +1):
            if s[j:j+i] in s[j+1:]:
                return s[j:j+i]
    return ""
#print(question_35("aabcdeaabcd"))

def question_36(nums: list[int]) -> list[list[int]]:
    if len(nums)==1:
        return [nums[:]]
    kq=[]
    for i in range(len(nums)):
        for p in question_36(nums[:i] + nums[i+1:]):
            kq.append([nums[i]] +p)
    return kq
nums=[1,2,3 ]
#print(question_36(nums))
nums=[1]
#print(question_36(nums))

def question_37(s: str) -> bool:
    danh_sach=[]
    quy_dinh={"(":")","{":"}","[":"]"}
    for i in s:
        if i in quy_dinh:
            danh_sach.append(i)
        elif not danh_sach or quy_dinh[danh_sach[-1]]!=i:
            return False
        else:
            danh_sach=danh_sach[:-1]
    return not danh_sach 
    #if not danh_sach
        #return True
    #else:
        #return False            
s = "{[]}"
#print(question_37(s))

def question_38(n: int) -> int:
    if n==1:
        return 1
    a,b=1,1
    for i in range(2,n+1):
        a,b=b,a+b
    return b
#print(question_38(3 ))

def question_39(prices: list[int]) -> int:
    gia_nn = float("inf")
    loinhuan_ln= 0
    for i in prices:
        if i < gia_nn:
            gia_nn=i
        elif i- gia_nn> loinhuan_ln:
            loinhuan_ln=i-gia_nn
    return loinhuan_ln
prices = [7, 6, 4, 3, 1]
#print(question_39(prices ))
            

