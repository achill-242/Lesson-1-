#dictionaries
#key-value pair



diary = {
    "Achilleas" : "blue" ,
    "Yiannis" : "red" ,
    "Stef" : "pink"
}

print(diary)
print(diary["Achilleas"])

# top print: prints the whole diary
# print with square brackets prints only what on the right of it 
# print only keys
print(diary.keys()) #this is to only print keys
print(diary.values()) # this is to only print values


for key in diary.keys():
    print(key, diary[key])