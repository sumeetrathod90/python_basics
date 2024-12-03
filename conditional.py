#if else condition
a=int(input ("enter your age: """))
print("your age is: ",a)
if(a>18):
  if(a>18 and a<60):
    print("you are eligible for draving")
  else:
    print ("you are not eligible for draving")
elif(a==18):
  print("you are eligible for learning")
else:
  print ("your not eligible for draving")