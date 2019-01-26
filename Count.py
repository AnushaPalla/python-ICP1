string1=input("enter the string:")
print(len(string1))
digits=0
words=0
letters=0
for i in string1:
    if i.isdigit():
        digits=digits+1
    if i.isalpha():
        letters=letters+1
print("number of digits in given string is:",digits)
print("number of letters in given string is:",letters)
print("number of words in given string is:",len(string1.split()))
