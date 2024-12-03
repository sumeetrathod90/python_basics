a = int(input("please enter the current time in 24 hr: "))
print("the time is : ", a)
if (a >= 0 and a < 12):
  print("good morning sir")
elif (a >= 12 and a < 18):
  print("good afternoon sir")
else:
  print("good evining sir")
