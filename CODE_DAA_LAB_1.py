import time
import random


def BubbleSort(A):
    x=len(A)

    for i in range(0,x):
        for j in range(0,x-i-1):
            if A[j]>A[j+1]:
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp



def InsertionSort(A):
    x=len(A)

    for j in range(1,x):
        key =A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key



def SelectionSort(C):
    x=len(C)
    for i in range(0,n-1):
        min=i
        for j in range(i+1, n):
            if C[j]<C[min]:
                min=j
        temp=C[min]
        C[min]=C[i]
        C[i]=temp


def MergeSort(D):
    i=0
    j=0
    k=0
    if len(D)>1:
        mid = len(D)//2
        l = D[:mid]
        r = D[mid:]

        MergeSort(l)
        MergeSort(r)

        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                D[k]=l[i]
                i+=1
            else:
                D[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            D[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            D[k]=r[j]
            j+=1
            k+=1


def partition(a,l,h):
    pivot = a[h]
    i=l-1
    for j in range(l,h):
        if a[j]<pivot:
            i=i+1
            a[i],a[j]=a[j],a[i]


    a[i+1],a[h]=a[h],a[i+1]
    return (i+1)
def QuickSort(a,l,h):
    if l<h:
        pi = partition(a,l,h)
        QuickSort(a,l,pi-1)
        QuickSort(a,pi+1,h)


n = int(input("Enter range:"))
print("The number of elements is :", n)

A = random.sample(range(1,1000000),n)
print("BUBBLE SORT:")
print("The input array is",A,end=" ")
print("")
start=time.time()
BubbleSort(A)
end=time.time()
print("Sorted Array",A)
print("Runtime of the program is: ", end-start)

B = random.sample(range(1,1000000),n)
print("INSERTION SORT:")
print("The input array is",B, end=" ")
print("")
start1=time.time()
InsertionSort(B)
end1=time.time()
print("Sorted Array",B)
print("Runtime of the program is: ", end1-start1)

C = random.sample(range(1,1000000),n)
print("SELECTION SORT:")
print("The input array is",C, end=" ")
print("")
start2=time.time()
SelectionSort(C)
end2=time.time()
print("Sorted Array",C)
print("Runtime of the program is: ", end2-start2)

#MergeSort
D = random.sample(range(1,1000000),n)
print("MERGE SORT:")
print("The input array is",D, end=" ")
print("")
start2=time.time()
MergeSort(D)
end2=time.time()
print("Sorted Array",D)
print("Runtime of the program is: ", end2-start2)

#QuickSort
a = random.sample(range(1,1000000),n)
num=len(a)
print("QUICK SORT:")
print("The input array is",a, end=" ")
print("")
start2=time.time()
QuickSort(a,0,num-1)
end2=time.time()
print("Sorted Array",a)
print("Runtime of the program is: ", end2-start2)

