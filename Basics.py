
def uppercase(str_data):
    result = ''
    for char in str_data:
        if ord(char) >= 65:
            result += chr(ord(char) - 32)
    return result
print(uppercase('abcde'))

#1 manager
l=[]
a=[1,9,7,6,2,3]
for i in range(0,len(a)-1):
    j=i
    while j!=len(a):
        j+=1
        if a[i]>a[j]:
            if j==len(a)-1:
                l.append(a[i])
                j+=1
        else:
            break
l.append(a[i]+1)
for i in range(len(l)):
    print(l[i],end=",")
    
#5And OR XOR
n=input("enter the input in the form of 0, 1, A, B, C such that the string length must be odd:")
l=list(n)
for i in range(len(l)):
    if(l[i]=='A'):
        l[i+1]=int(l[i-1])*int(l[i+1])
    elif(l[i]=='B'):
        if(l[i-1]==1 or l[i+1]==1):
            l[i+1]=1
        elif(l[i-1]==0 or l[i+1]==1):
            l[i+1]=1
        elif(l[i-1]==1 or l[i+1]==0):
            l[i+1]=1
        else:
            l[i+1]=0
    elif(l[i]=='C'):
        if(l[i-1]==1 and l[i+1]==1):
            l[i+1]=0
        elif(l[i-1]==0 and l[i+1]==0):
            l[i+1]=0
        else:
            l[i+1]=1
print(l[-1])


#3Prefix Suffix
def longestPrefixSuffix(s) : 
	n = len(s) 
	for res in range(n // 2, 0, -1) : 
		prefix = s[0: res] 
		suffix = s[n - res: n] 
		
		if (prefix == suffix) : 
			return res 
	return 0
	
s = input("enter the string:")
print(longestPrefixSuffix(s)) 

#4 closest Number
def closestNumber(n, m):
    q = n / m
    n1 = m * q

    if (n * m) > 0:
        n2 = m * (q + 1)
    else:
        n2 = m * (q - 1)
    if abs(n-n1) < abs(n-n2):
        return n1
    return n2 
n=int(input("enter the number n:"))
m=int(input("enter the number m:"))
print(closestNumber(n,m))

#Pattern 
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
m=pattern(5)

def pattern(n):
    for i in range(n,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print("\r")
m=pattern(5)
print("\n")

def pattern(n):
     k=n*2-2
     for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
m=pattern(5)

def pattern(n):
     k=0
     for i in range(n,0,-1):
        for j in range(0,k):
            print(end=" ")
        k=k+2
        for j in range(0,i):
            print("*",end=" ")
        print("\r")
m=pattern(5)
print("\n")

def pypart2(n): 
	k = 2*n - 2
	for i in range(0, n): 
		for j in range(0, k): 
			print(end=" ") 
		k = k - 1
		for j in range(0, i+1): 
			print("* ", end="") 
		print("\r") 
n = 5
pypart2(n) 
def pypart3(n): 
	k = n - 1
	for i in range(n,0,-1): 
		for j in range(0, k): 
			print(end=" ") 
		k = k + 1
		for j in range(0, i): 
			print("* ", end="") 
		print("\r") 
n = 5
pypart3(n) 
print("\n")
def pypart4(n): 
    num=65
    for i in range(0,n): 
        for j in range(0, i+1): 
            print(chr(num), end=" ") 
            num+=1
        print("\r") 
n = 5
pypart4(n) 
print("\n")

#Substring
test_str = input("enter the string:") 
print("The original string is : " + str(test_str)) 
res = [test_str[i: j] for i in range(len(test_str)) 
          for j in range(i + 1, len(test_str) + 1)] 
print("All substrings of string are : " + str(res))

