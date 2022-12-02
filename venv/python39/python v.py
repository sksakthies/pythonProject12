day="monday"
temperature=5
raining=True

if day=="saturday" or temperature>27 and not raining:
    print("go swim")
else:
    print("learn python")

if 1:
    print("true")
else:
    print("false")

name=input("enter your name")
if name!={}:
    print("hello,{}".format(name))
else:
    print("are u with no name")

parrot="norwegian blue"
letter=input("enter the character")
if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("do not have")

activity=input("what are u going to do ?")
if "cinema" not in activity.casefold():
    print("but i want to do")
