introstring=input("enter your introdution:")
print(introstring)
charactercount=0
wordcount=1
for i in introstring:
    charactercount=charactercount+1
    if(i== ' ') :
        wordcount=wordcount+1

print("number of words in the string:")
print(wordcount)

print("number of charaters in a string:")
print(charactercount)