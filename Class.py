# class Student :

#   def set_name(self,name):
#     self.name = name
  
#   def get_name(self):
#     return self.name
  
# student1 = Student()
# student1.set_name("Sukhman")
# print(student1.name)

# print(student1.get_name())

# student2 = Student()
# student2.set_name("Jashan")
# print(student2.get_name())



# class Rectangle :

#   def __init__(self,height,width):  
#     self.width = width
#     self.height = height

#   def area(self):
#     return self.height*self.width
  
#   def perimeter(self):
#     return 2*(self.height + self.width)

# height = int(input('Enter the height :'))
# width = int(input('Enter the width : '))
# rectangle1 = Rectangle(height,width)
# # rectangle1.set_dimensions(height,width)

# print("The height is :",rectangle1.height)
# print('The width is :',rectangle1.width)

# print('The area is :',rectangle1.area())
# print('The perimeter is :',rectangle1.perimeter())



# public modifier
# class ABC :
#   def __init__(self):
#     self.public_attribute = None

#   def public_function():
#     pass


# private modifier
# class ABC:
#   def __init__(self):
#     self.__private_attribute = None

#   def __private_function():
#     pass

# protected modifier
# class ABC:
#   def __init__(self):
#     self._protected_attribute = None

#   def _protected_function():
#     pass


# class parent:
#   def __init__(self):
#     self.super_attribute = True
#     print('This is the parent class')

# class Child(parent):
#     def __init__(self):
#       super().__init__()
#       print('This is the child class')
#       print(self.super_attribute)


# child1 = Child()



# class vehicle():
#   def __init__(self,seating_capacity):
#     self.seating_capacity = seating_capacity

#   def get_fare(self):
#     return self.seating_capacity * 100
  

# class Bus(vehicle):
#   def __init__(self,seating_capacity):
#     super().__init__(seating_capacity)

#   def get_fare(self):
#     vehicle_fare = super().get_fare()
#     maintainence_fare = vehicle_fare * 0.1
#     total_fare = maintainence_fare + vehicle_fare
#     return total_fare

# vehicle1 = vehicle(50)
# print('Vehicle fare :',vehicle1.get_fare())

# Bus1 = Bus(50)
# print('Bus fare ;',Bus1.get_fare())


# class Animal:
#   def speaks(self):
#     pass

# class Dog(Animal):
#   def speaks(self):
#     print('Barks')

# class Cat(Animal):
#   def speaks(self):
#     print('Meow')

# class Cow(Animal):
#   def speaks(self):
#     print('Mooo')


# dog = Dog()
# cat = Cat()
# cow = Cow()

# dog.speaks()
# cat.speaks()
# cow.speaks()


# class ComplexNumber :
#   def __init__(self,real,img):
#     self.real = real
#     self.img = img

#   def __add__(self,other):
#     return ComplexNumber(self.real + other.real, self.img + other.img)
  
# c1 = ComplexNumber(2,4)
# c2 = ComplexNumber(5,8)
# c4 = ComplexNumber(6,8)
# c3 = c1 + c2 + c4
# print(c3.real , '+',c3.img,'i')


a = int(input('Enter a :'))
b = int(input('Enter b :'))

try:
  result = a/b
except ZeroDivisionError:
  result = None
  print('Error : Cannot divide by zero')
finally : 
  print('Division operation completed :',result)

