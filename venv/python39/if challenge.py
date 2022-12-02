name=input("enter the your name:")
age=int(input("enter your age here:"))
if(age<=18 and age>=31):
    print("you {} can go to holiday".format(name))
else:
    print("your {} not eligible for the vacation visit after ".format(name))
