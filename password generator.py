import string
import random


s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)

length=int(input("Enter the length of your password:"))

while True:
    try:
        char_number=(length)
        if char_number<5 :
            print("Your password should be atleast of 5.")
            length=int(input("Please enter the length again:"))

        else:
            break
    except:
        print("Enter numbers only:")
        length=int(input("How many characters do you want in your password"))

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

p1 = round(char_number * (30/100))
p2 = round(char_number * (20/100))

result=[]
for x in range(p1):
 
    result.append(s1[x])
    result.append(s2[x])
 
for x in range(p2):
 
    result.append(s3[x])
    result.append(s4[x])



random.shuffle(result)
password="".join(result)
print(" Your Password is:",password)




