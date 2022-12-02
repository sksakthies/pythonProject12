print("hello world!")
print(1+2)
print(7*6)
print()
#strings
print("the enda" ,"or is it ?","keep watching to learn more about python",3)
print('today is good day to learn python')
print('python is fun')
print("python strings are easy to use")
print('we can even include "quotes" in string')
#joining of strings concadenation
print("hello" + " world")
greeting="hello"
name="sakthi"
print(greeting + name)
print(greeting + ' ' +name)
#escape characters"\"
splitstring="this string has been\nsplit over\nseversl\nlines"
print(splitstring)

tabbedstring="1\t2\t3\t4\t5"
print(tabbedstring)

print('the pet shop owner said "No, no, e\'s uh,....he\'s resting",')
#or
print("the pet shop owner said  'No, no, 'e's uh,...he's resting\".")
print("""the pet shop owner said  "No, no,'e's uh,...he's resting'.""")

anothersplitstring="""this string has been \
split over \
several \
lines"""
print(anothersplitstring)


print("c:\\users\\timbuchalka\\notes.txt")
print(r"c:\user\timbuchalka\notes.txt")

print("\\test")
print("doesn\'t")
print("\"python\"")
print("python","\n","lang")
print("python","\t","lang")

print(r"c:users\timbuchlka\notes.txt")


#varaibles and types
#variable is nothing but give a meaningful name to the area of memory

#numeric data type
#int float complex there is no size to store the python int



a=12
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

print()
for i in range(1,a//b):
    print(i)
print()
i=2
while i<=a/b:
    i=i+1


    print(i)

print()

i=1
print(i)
i=2
print(i)
i=3
print(i)

print(a+b/3-4*12)
print(a+(b/3)-(4*12))
print((((a+b)/3)-4)*12)

c=a+b
d=c/3
e=d-4
print(e*12)



print(a /(b*a)/b)
#       012345678901234
parrot="Norwegian blue"
#       43210987654321
print(parrot)

print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])


print()
#negative indexing in the string

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print()

#slicing


print(parrot[0:6])#norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14])
print(parrot[10:])
print(parrot[11:13])
print(parrot[6:])
print(parrot[:6])

print(parrot[:9]+parrot[9:])

print(parrot[:])

print(parrot[1:14:3])

print()
print(parrot[-4:-2])
print(parrot[-4:13])
print(parrot[-14:-8])
print(parrot[-14:-1])


print(parrot[0:14:2])
print(parrot[0:6:2])
print(parrot[0:6:3])


number="9,223;372:036 854,775;807"
separtors=(number[1::4])
print(separtors)
print(number[0::1])

letters="abcdefghijklmnopqrstuvwxyz"
backword=letters[25:0:-1]
print(backword)
print(letters[25:0:-1])
print(letters[25:0:-2])
print(letters[25:-25:-1])

print(letters[16:13:-1])

print(letters[-22:-27:-1])

print(letters[:-9:-1])
print(letters[-4:])
print(letters[-1:])
print(letters[:-1])
print(letters[0])
print(letters[25:17:-1])



# string operators

# sequence operators


string1= "he's "
string2= "probably "
string3= "pining "
string4= "for the "
string5= "fjords "

print(string1+ string2+ string3+ string4 + string5)

print("he's " "probably " "pining " " for the " " fjords ")


print("hello "*5)

print("hello " *(5+4))
print("hello "*5 +"4")

today="friday"

print("fri" in today)
print("day" in today)
print("thur" in today)
print("parrot"in "fjords")

#string replacement field str() is string function

age=24
print("my age is " +str(age) +" years ")

print("my age is {0} years".format(age))


print("there is {0} days in {1},{2},{3},{4},{5},{6},{7}".format(31,"jan","mar","may","jul","sep","nov","dec"))

print("jan: {2},feb: {0}, mar: {2}, apr: {1}, may: {2}, jun: {1}, jul: {2}, sep:{1}, oct: {2}".format(28,30,31))

print()

print("""jan: {2}
feb: {0} 
mar: {2} 
apr: {1} 
may: {2}
jun: {1} 
jul: {2} 
sep: {1} 
oct: {2}
nov: {1}
dec: {2}""".format(28,30,31))


#string formatting

for i in range(1,13):
    print("No. {0:10} sqarred is {1:12} and cubed is {2:10}".format(i,i**2,i**3))



print("pi approximately {0:12}".format(22/7))
print("pi approximately {0:12f}".format(22/7))
print("pi approximately {0:12.50f}".format(22/7))
print("pi approximately {0:52.50f}".format(22/7))
print("pi approximately {0:62.50f}".format(22/7))
print("pi approximately {0: 72.54f}".format(22/7))


import pyqrcode


QRstr="karthick"

url=pyqrcode.create(QRstr)
url.png("siteqr1.png",scale=8)














print()

print("{0:12}".format(22/7))




for i in range(1,13):
    print("no:{0} squared is {1:} and cube is{2: }".format(i,i**2,i**3))




greeting="hello"

name="vinoth"




age=24
print(age)

print(type(greeting))
print(type(name))
print(type(age))


age_in_age="2 years"

print(name+f" is {age}"+"old")


age_=24
print("my age is%d years" % age_)


major="years"
minor="months"

print("my age is %d %s,%d %s" %(age_,major,6,minor))
print("pi value approximately %f"%(22/7))
print("pi value is approxiately %60.50f"%(22/7))



print()

a=45
b=15
c=3
print(a-b/c)


#blocks

for i in range(1,13):
    print(" no.{} square is {} and cube is {:4}".format(i,i**2,i**3))
    print("*"*80)


i=1
while(i<13):
    print(i)
    i=i+1


i=1
while(i<=13):
    print("no. {} square is {} and cube is {:4}".format(i,i**2,i**3))
    i=i+1

name=input("enter your name here:")
age=int(input("what is your age {0}".format(name)))
print(age)

if age>=18:
    print("you are eligible for voting")
    print('please put an x in the box')
else:
    print("come back in {0} years".format(18-age))


i=1
while(i<=3):
    print("vino")
    i=i+1



for i in range(1,45):
    print("vinoth")

name="flower"
if("p"in name):
    print("yes")
else:
    print("no")



a=float(input("enter a value :"))
b=float(input("enter a value :"))

print("1)addition\n2)subtraction\n3)multiplication\n4)division\n5)total value")

c=float(input("enter your choice :"))
if(c==1):
    print(a+b)
elif(c==2):
    print(a-b)
elif(c==3):
    print(a*b)
elif(c==4):
    print(a/b)
elif(c==5):
    print(a)



else:
    print("invaild input\ntry again")


name=input("enter the name:")
age__=int(input("enter your age:"))
print(age__)

if(age__>18):
    print("your are eligible for voting mr/mrs:{0}".format(name))
elif(age__==18):
    print("your are eligible for voting mr/mrs:{0}".format(name))
else:
    print("please come back in {} years mr/mrs:{}".format(18-age__,name))

answer=5
print("please guess the number  between 1to10")
guess= int(input(""))
if guess<answer:
    print("please the higher")
    guess=int(input())
    guess=int(input())
    if guess==answer:
        print("your guess is correct")
    else:
        print("your guess is wrong")
elif guess>answer:
    print("please guess the lower")
    guess=int(input())
    if guess==answer:
        print("your guess is correct")
    else:
        print("your guess is wrong")
else:
    print("you got it first")

#factorial
n=int(input("the factorial :"))

i=1
s=1
while(i<=n):

    s=s*i

    i=i+1

    print("the factorial of ",i," is ",s)


age1=int(input())
#if age1>=16 and age1<=65:
if 16<=age1<=65:
    print("how are you")

else:
    print("i")


if age<16 or age>65:
    print("hi ")