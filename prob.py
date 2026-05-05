# lst=["hi",1,2,3,[9,8,7,6,["a","b","c","d",],10,20,30,],[True,False],10,2]
# lst[4][4].append("e")
# print(lst)
# lst[4].pop()
# print(lst)
# lst[5].pop()
# print(lst)

#insert(idx,val)

# lst1=["Hi","Hello","No"]
# lst1.insert(1,10)
# print(lst)

# #extend(list)
# lst.extend(lst1)
# print(lst)
# lst[4][4].extend(lst1)
# print(lst1)

#tupple is immutable 
# tup=(1,2,3,4,5,4,5,4,4,3,4,4,)
# print(tup)
# tup1=tuple()
# print(tup1)
# tup2=(2,)
# print(tup2)
# t=tup.count(4)
# print(t)


# t=tup.index(4)
# print(t)

#set
# st1={1,2,3,4,5,6,7}
# st2={1,5,90,54,3,4,80}
 
# #union  :- combines the set
# print(st1.union(st2))

# #intersection :- common elements
# print(st1.intersection(st2))

# #add :-add the elements
# st1.add(8)
# print(st1)


# lst=["hi",1,2,3,[9,8,7,6,["a","b","c","d",],10,20,30,],[True,False],10,2]
# st1={"spinach","Potato","chilli",1,2,3,}
# st2={"spinach","hii","chilli",1,2,"hello"}
# st3=(st1.union(st2))
# lst.append(st3)
# print(lst)


#Dictionary
# student=["Raj","Male","Pune",3,20]
# student={
#     "Name":"Raj",
#     "roll-no":90,
#     "age":21,
#     "city":"pune",
#     "cgpa":8.8,
#     "mob-no":9112484912
# }
# print(student["Name"])
# print(student["roll-no"])
# print(student["age"])
# print(student["city"])
# print(student["cgpa"])
# student["qualification"]="Btech"
# print(student)
# print(student.get("marks"))
# print(student.keys())
# print(type(student.keys()))
# print(student.values())
# print(type(student.values()))
# print(student.items())#return in objects form


#Decision control statement
#if-else
# num1=10
# if num1==5:
#     print(True)
# else:
#     print(False)

# age=15
# if age>=18:
#      print("Eligible for voting")
# else:
#     print("not eligible for voting")

#if-elif-else
# color=input("enter color red/green/yellow:")
# if color=="red":
#     print("stop")
# elif color=="green":
#     print("go")
# elif color=="yellow":
#     print("wait")
# else:
#     print("Invalid choice ")
    

# number=eval(input("enter the number"))
# if number>0:
#     print("postive number ")
# elif number<0:
#     print("negative number ")
# else:
#     print("zero")

# print("1.Tea,2.Coffe,3.Black Tea")
# ch=eval(input("enter your choice"))
# match(ch):
#     case 1:
#         print("Tea is ready")
#     case 2:
#         print("Coffe is ready")
#     case 3:
#         print("Black Tea is ready")
#     case _:
#         print("Invalid choice")

#Looping statements 
#while loop 
# num=1
# while num<=10:
#     print(num)
#     num=num+1

# num=1
# while num<=20:
#     if num%2==0:
#         print(num)
#     num=num+1

# num=1
# while num<=20:
#     if num%2!=0:
#         print(num)
#     num=num+1


#for loop 
# for i in range(1,11,1):
#     print(i)
    
# for i in range(21,1,-1):
#     print(i)

#factorial 
# num=eval(input("enter number :"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
#     print(fact)

# num=5
# for i in range(1,11):
#     print(num*i)        
 #take a string and check the vowels in it

# text="Here we can find the vowels in python"

# vowels="aeiouAEIOU"
# for char in text:
#  if char in vowels:
#   print(char)