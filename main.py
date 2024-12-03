# print("Hello World")
# print(5)
# import pandas

# print("Hi")
# print(11 * 11, )
# print(10 - 3)
# print(10 + 3)
# print(9 / 3)
# this is comment
# comment 2
# comment 3
# print("hey i am a \"good boy\"\nand this viewer is aslo a good boy/girl")
# print("hey", 6, 7, sep="-", end="\n")
# print("harry")
# a = 123
# b = "google"
# c = 321
# d= True
# print(a + c)
# print("name is ",b)
# print("type of a is", type(a))
# print("thetype os", type(b))
# print("the program for calculater")
# print("here we have tow static number 50 and 40\nand we operating on it")
# a=50
# b=40
# print("the adittion of two number is",a+b)
# print("the subtraction of two number is",a-b)
# print("the devidation of two number is",a/b)
# print("the multiplication of two number is",a*b)
# a="1"
# b="3"
# print(a+b)#this is string variable
# print(int(a)+int(b))#this is explicit typecastiin
# #implicit typecasting
# c= 2.6#floting point number
# d=5#integer
# print(c+d)
# #input function
# a=input("enter your first name:")
# b=input("enter your last name:")
# print("your name is:",a+b)
# intiger numbers
# x=input("enter first number:")
# y=input("enter second number:")
# print("addition is :",int(x)+int(y))
# print("substraction is :",int(x)-int(y))
# print("Multiplication is :",int(x)*int(y))
# print("dividation is :",int(x)/int(y))
#string
# name= "harry"
# friend="rohan"
# apple="the apple is s good \"fruit\""
# print(name)
# print(friend)
# print(apple)
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# for character in apple: print(character)
##string slicing
# fruit="mango"
# mangolen=len(fruit)
# print(mangolen)
# print(fruit[0:4])
# print(fruit[2:4])
# print(fruit[0:-2])
# print(fruit[-4:-2])
# print(fruit[:len(fruit)-4])
# nm="harry"
# print(nm[-4:-2])
# print(nm[-3:-1])

## string method
##string is imutable
# a = "! Harry !!!"
# print(len(a))  #this is a lenth counting
# print(a.upper())  #this is upper case of string
# print(a.lower())  #this is lower case of string
# print(a.rstrip(
#     "!"))  #this is remove the trailing character and not leading character
# print(a.replace(a, "john"))  #this is replace the string
# print(a.split(" "))  #this is split the string and show in list
# blogheading = "intRoduction tO js"
# blogtxt = "we are knowing about js also we write some programs in js, js is good for learing"
# print(blogheading.capitalize())  #this convert string to capitalize
# print(blogheading.center(
#     50))  #this is center the string and add the space which we specify
# print(len(blogheading))
# print(blogtxt.count(
#     "js"))  #this is count the repeated times of string in  large string
# print(blogheading.endswith(
#     "js"))  #this is check the string is end with the given string or not
# print(
#     blogheading.endswith("tO", 10, 15)
# )  #this is check the string is end with string in specyfic range in long string
# print(blogtxt.find("js"))
# print(blogtxt.find("jss"))
# # print(blogtxt.index("jss"))
# str="WeareLiveat9pm"
# print(str.isalnum())
# print(str.isalpha())
# print(str.islower())
# print(str.isprintable())
# print(str.isspace())
# print(str.istitle())
# print(str.startswith("we",0,10))
# print(str.swapcase())
# print(blogheading.title())

#if else condition
a=int(input ("enter your age: """))
print("your age is: ",a)
if(a>18):
  print("you are eligible for draving")
else:
  print ("your not eligible for draving")