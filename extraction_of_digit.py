#Extraction of digit n=12345
n=int(input("Enter number which you want digit Extracted"))
num=n
while num>0:
    last_digit=num%10
    print("Your Extracted digit",last_digit)
    num=num//10