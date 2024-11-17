# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 10:47:14 2024

@author: PC
"""

def question_1(n: int) -> bool:
    if n<=1:
        print(f"{n} không phải là số nguyên tố ")
        return False 
    for i in range(2,int(n**0.5)+1):
        if n%2==0:
            print(f"{n} không phải là số nguyên tố ")
            return False
    print(f"{n} là số nguyên tố ")
    return True

print(question_1(11 ))
print(question_1(4 ))

from typing import Tuple
import random 
def question_2(n: int) -> Tuple[int, float]:
    ds=[random.randint(1,100) for i in range(n)]
    print(f"{n} số ngẫu nhiên từ 1 đến 100:",ds  )
    tong= sum(ds)
    trung_binh= tong/n
    return tong, trung_binh
print(question_2(5))
print(question_2(10))

from typing import Tuple
def question_3(s: str) -> Tuple[int, int]:
    viet_hoa=0
    viet_thuong=0
    for i in s:
        if i.isupper():
            viet_hoa+=1
        elif i.islower():
            viet_thuong+=1
    return viet_hoa, viet_thuong
print(question_3("Hello World"))
print(question_3("Python Programming"))

def question_4(n: int) -> bool:
    if n%2==0:
        return True
        print(f"{n} là số chẵn ")
    else:
        return False
        print(f"{n} là số lẻ ")
s= int(input("Nhập số nguyên: "))
print(question_4(s ))

from typing import Optional
def question_5(lst: list, x: int) -> Optional[int]:
    for i in range(len(lst)):
        if x in lst:
            return lst.index(x)
lst=[1,2,3,4,5]
x=3
print(question_5(lst,x))
lst=[10,20,30,40]
x=25
print(question_5(lst,x ))

def question_6(n: int) -> int:
    giai_thua=1
    for i in range(1,n+1):
        giai_thua*=i
    return giai_thua
print(question_6(5))
print(question_6(7 ))

import random 
def question_7(n: int) -> (float, float):
    ds= [round(random.uniform(0,1),4) for i in range(n)]
    print(f"{n} số ngẫu nhiên từ 0 đến 1:",ds )
    so_ln= max(ds)
    so_nn= min(ds)
    return so_ln, so_nn
print(question_7(5))
print(question_7(10))

def question_8(s: str) -> str:
    return s[::-1]
n= input("Nhập chuỗi:")
print(question_8(n))
            
def question_9(s: str) -> bool:
    bien_doi="".join([s[i].lower() for i in range(len(s)) if s[i].isalnum()])
    if  bien_doi== bien_doi[::-1]:
        return True
        print(f"{s} là dãy Palindone ")
    else:
        return False
        print(f"{s} không là dãy Palindone ")
print(question_9("A man, a plan, a canal: Panama"))
print(question_9("race a car"))

from typing import Optional, List 
def question_10() -> Optional[List[int]]:
    ds=input("Nhập danh sách:").split()
    ds=[int(i) for i in ds]
    if not ds:
        return None
    return ds 
print(question_10())

def question_11(n: int) -> int:
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a,b=0,1
        for i in range(2,n+1):
            a,b=b,a+b
        return b
print(question_11(5))
print(question_11(10))

import random 
def question_12() -> bool:
    n =random.randint(1,1000)
    print("Số ngẫu nhiên từ 1 đến 1000:",n )
    if n<=1:
        return False
        print(f"{n} không là số nguyên tố ")
    for i in range(2,int(n**0.5)+1):
        if n%2==0:
            return False
            print(f"{n} không là số nguyên tố")
    return True
    print(f"{n} là số nguyên tố ")
print(question_12())

def question_13(s: str) -> int:
    tach= s.split()
    return len(tach)
print(question_13("Hello world, how are you?"))
print(question_13(" This is a test. "))

def question_14(s: str) -> bool:
    if s.isdigit():
        return True
        print(f"{s} là chữ số ")
    else:
        return False
        print(f"{s} không là chữ số")
print(question_14("12345"))
print(question_14("123a45"))
print(question_14("0123"))

def question_15(value) -> bool:
    if value is None:
        return True
        print("Giá trị nhập vào là None ")
    else:
        return False
        print("Giá trị nhập vào không là None") 
print(question_15(10  ))
print(question_15("Hello"))

def question_16(*args) -> float:
    if not args:
        return None 
    return  sum(args)/len(args)
print(question_16(1,2,3,4,5 ))
print(question_16(10,20))
print(question_16())

import random 
def question_17(n: int) -> list:
    ds=[random.randint(1,100) for i in range(n)]
    ds.sort(reverse=True)
    return ds 
print(question_17(5))

def question_18(s: str) -> str:
    return " ".join(s.split())
print(question_18(" Hello world! "))
print(question_18("Python  is   fun"))

def question_19(x: int, n: int) -> bool:
    if  x>n:
        return True
        print(f"{s} lớn hơn {n}")
    else:
        return False
        print(f"{s} bé hơn {n}") 
s=int(input("Nhập số cần kiểm tra:"))
n=10 
print(question_19(s,n ))

from typing import Optional
def question_20() -> Optional[str]:
    n= input("Nhập giá trị:")
    if not n:
        return None
    return n
print(question_20())

from typing import Optional, List, Tuple
def question_21(nums: list[int], target: int) -> Optional[tuple[int, int]]:
    n=set()
    for i in nums:
        number= target -i
        if number  in n:
            return (number,i )
        n.add(i)
    return None 
nums = [2, 7, 11, 15]
target = 9
print(question_21(nums, target ))

nums = [1, 2, 3, 4, 5] 
target = 10
print(question_21(nums, target ))

def question_22(nums: list[int]) -> None:
    so_khac_khong=[i for i in nums if i!=0]
    so_khong= nums.count(0)
    return so_khac_khong + ([0]*so_khong)
nums = [0, 1, 0, 3, 12]
print(question_22(nums))

def question_23(nums: list[int]) -> bool:
    if len(nums) != len(set(nums)):
        print("Có ít nhất một giá trị xuất hiện hơn 1 lần ")
        return True
    else:
        print("Tất cả các phần tử đều khác nhau ")
        return False
nums=[1,2,3,1]
print(question_23(nums))

nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(question_23(nums))

nums = [1, 2, 3, 4]
print(question_23(nums))

def question_24(nums: list[int]) -> int:
    for i in nums:
        if nums.count(i) > (len(nums)// 2):
            return i
nums = [3, 2, 3]
print(question_24(nums))

nums = [2, 2, 1, 1, 1, 2, 2]
print(question_24(nums))

def question_25(nums: list[int]) -> list[int]:
    ds=[i**2 for i in nums]
    return sorted(ds )
nums = [-4, -1, 0, 3, 10]
print(question_25(nums))

nums = [-7, -3, 2, 3, 11]
print(question_25(nums))

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
    for i in range(1, len(strs)):
        while tien_to and tien_to!=strs[i][:len(tien_to)]:
            tien_to=tien_to[:-1]
            if not tien_to:
                return ""
    return tien_to 

def question_28(s: str) -> Dict[str, int]:
    dem={}
    for i in range(len(s)):
        if s[i] in dem:
            dem[s[i]]+=1
        else:
            dem[s[i]]=1
    return dem

def question_29(nums: List[int]) -> Optional[Tuple[int, int]]:
    nums.sort()
    n=len(nums)
    if n%2==0:
        return (nums[n//2-1]+nums[n//2])/2
    else:
        return nums[n//2]
    
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
        if (dem[i] /len(tach))>0.2:
            kq.append(i)
    return kq[:n] if len(kq)>=n else []

def question_32(nums: List[int]) -> Tuple[List[int], List[int]]:
    so_chan= sorted([i for i in nums if i%2==0], reverse=True )
    so_le=sorted([i for i in nums if i%2!=0])
    return so_chan,so_le

def question_33(nums: list[int]) -> tuple[int, int]:
    n=sorted(set(nums))
    return (n[-2],n[4]) if len(n)>4 else None

def question_34(s: str) -> int:
    ds,dodai_ln,trai=set(),0,0
    for phai in range(len(s)):
        while  s[phai] in ds:
            ds.remove(s[trai])
            trai+=1
        ds.add(s[phai])
        dodai_ln=max(dodai_ln,phai-trai+1)
    return dodai_ln

def question_35(s: str) -> str:
    for i in range(len(s),0,-1):
        for j in range(len(s)-i+1):
            if s[j:j+i] in s[j+1:]:
                return s[j:j+i]
    return ""

def question_36(nums: list[int]) -> list[list[int]]:
    if nums==1:
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
        elif i-gia_nn>loinhuan_ln:
            loinhuan_ln=i-gia_nn
    return loinhuan_ln 
        


            
            

