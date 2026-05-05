#palindrome
# str1=input("Enter a string")
# str2=str1[::-1]
# print(str2)
# if str1==str2:
#     print("Palindrome")
# else:
#     print("Not palindrome")
  
#unique char
# str1=input("Enter input")
# lst=list()
# for i in str1:
#     if i not in lst:
#         lst.append(i)
#     print(lst)

# str1=input("Enter input")
# lst=list()
# for i in str1:
#     if str1.count(i)==1:
#         lst.append(i)
# print(lst)
# c=str1.count("E")
# print(c)

#Functions:- set of instruction use to perfrom task
#def func_name(para):
# function body
#return 

# def sayHello():
#     print("Hello")
# sayHello()

# def power_num(num):
#     print("Power of ,num,""is",num**2)
# power_num(4)

# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     print(fact)    
# factorial(5)


# def sum_of_number(num):
#     sum=1
#     for i in range(1,num+1):
#         sum+=i
#     print(sum)    
# sum_of_number(5)

# def sum_of_number(num):
#     sum=0
#     for i in range(1,num+1):
#         sum+=i
#     return sum  
# print(sum_of_number(5))

# def sum_of_digits(num):
#     sum=0
#     while num>0:
#         i=num%10
#         sum+=i
#         num//=10
#     return sum
# print(sum_of_digits(12345))   

#prime number
# def prime_number(num):
#     res=0
#     for i in range(2,num):
#         if num%i==0:
#             res=False
#         else:
#             res=True
#         if res==False:
#             print("Prime")
#         else:
#             print("Not Prime")
#     return res
# print(prime_number(11))        
    

# def prime_num(num):
#     for i in range(2,(num//2)+1):
#         if i%2==0:
#             flag=False
#             break
#     if flag==False:
#         print("Not Prime")
#     else:
#         print("Prime")
# prime_num(4)

#update method
# std={
#     "prachi":70,
#     "varsha":45,
#     "rohan":55,
# }
# mar=eval(input("Enter Marks :"))
# nm="rohan"
# std.update({nm:mar})
# print(std)

# std={
#     "prachi":70,
#     "varsha":45,
#     "rohan":55,
# }
# ch=eval(input("Enter the choice"))
# match ch:
#     case 1:
#         name=input("enter the name")
#         marks=eval(input("enter the marks: "))
#         std[name] =marks
#     case 2:
#         name=input("enter the name")
#         marks=eval(input("enter the marks: "))
#         std.update ("{ name,marks}")
#     case 3:
#         name = input("enter the name to search: ")
#         if name in std:
#             print("marks of {name}:{std[name]}")
#         else:
#              print("name not found")
#     case 4:
#         for name,marks in std.items():
#             print(f"{name}: {marks}")
#     case _ :
#         print("invalid choice")
# print(std)

