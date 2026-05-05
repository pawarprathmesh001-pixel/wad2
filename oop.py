#OOP
# class My_Class:
#  def __init__(sf,name,roll=12,age=21,branch="IT"):
#     sf.name=name
#     sf.roll=roll
#     sf.age=age
#     sf.branch=branch
#     # print("Name", sf.name)
#     # print("roll",sf.roll)
#     # print("age",sf.age)
#     # print("branch",sf.branch)
# s1=My_Class("Rahul") 
# print(s1._name)         

# encapsulation
# class student:
#     def __init__(self,name,roll):
#         self.__name=name
#         if roll>0 and roll<100:
#             self.__roll=roll
#         else:
#             r1=eval(input("Enter Roll :"))
#             self.__roll=rl
#     def info(self):
#         print("Name : ",self.__name," Roll.no : ",self.__roll)
# s1=student("riddhi",90)
# s1.info()


# inheritance
# class vehicles:
#     _Brand=None
#     _Model=None
#     _Engine=none
# class Bike(vehicle)
#     def __init__(self,br,md,Engine):
#         self._Brand=br
#         self._Model=md
#         self._engine=engine
#         print("Brand : ",self._Brand,"Model: ",self._Model,"Engine :",self.engine)


# class vehicles:
#     _Brand=None
#     _Model=None
#     _seats=None
# class Car(vehicles):
#     def __init__(self,br,md,seats):
#         self._Brand=br
#         self._Model=md
#         self._seats=seats
#         print("Brand : ",self._Brand,"Model: ",self._Model,"seats :",self._seats)
# c1=Car("BMW","X7",7)
# print(c1)

# class Book:
#     def __init__(self,title,au,rw):
#         self.title=title
#         self.author=au
#         self.lst_rw=[]
#         self.lst_rw.append(rw)
#     def add_review(self,rw):
#         self.lst_rw.append(rw)
#         print(rw)
#         print()
#     def count_review(self):
#         print("the count of review ",len(self.lst_rw))
#     def display_all_reviews(self):
#         for i in self.lst_rw:
#             print(i)
#             print()
# b1=Book("Chhavva","Shivaji Sawant","Very Good Book")
# b1.add_review("Very Nice")

class Shape():
    def area():
        pass
class Circle(Shape):
    def __init__(self,rd):
        self.rd=rd
    def area(self):
        self.area=3.14*(self.rd**2)
        print("area of circle is : ",self.area)
class Rectangle(Shape):
    def area(self,l,b):
        print("Area of rectangle is ",l*b)
class Triangle(Shape):
    def area(self,b,h):
        print("Area of triangle ",0.5*b*h)
c1=Circle(4)
c1.area()
print(c1)
r1=Rectangle()
r1.area(10,5)
t1=Triangle()
t1.area(5,5)