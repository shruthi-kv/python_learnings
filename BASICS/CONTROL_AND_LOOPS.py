age =  34

if(age > 18):
    print("Greater than 18")
    if(age == 34):
        print("you can drive---")
print("thank you----")


# age  = int(input("Enter you age"))

# if(age >18):
#     print("you can drive")
# else:
#     print("you cannot drive")
# print("end of program------------")

age = int(input("enter you age "))

if(age >18):
    print("you can drive")
elif(age == 18):
    print("schdule an interview")
elif(age==0):
    print("you are just born")
else:
    print("you cannot drive")