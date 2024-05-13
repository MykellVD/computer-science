# program that counts number of "bob"s in a string
def count_bobs(string):
    bob_count = 0
    count = 0
    while len(string) > 2:
        if(string[0] == "b" and string[1] == "o" and string[2] == "b"):
            bob_count+=1
            string = string[2:]
                    
        string = string[1:]
        count += 1
    return bob_count

print("no overlap bob tests")
print(count_bobs("azcbobobegghakl")) # = 1
print(count_bobs("doijfbobboboijbob")) # = 3
print(count_bobs("bobaoboboaidjbobd")) # = 3
print(count_bobs("bobbobbobbobbob")) # 5

# if you want to count all occurances of bob with overlaps
# ex: bobob = 2
# then this works

def count_bobs(string):
    bob_count = 0
    for i in range(len(string) - 2):
        if string[i:i+3] == 'bob':
            bob_count += 1
    return bob_count

print()
print("overlap bob tests")
print(count_bobs("azcbobobegghakl")) # = 2
print(count_bobs("doijfbobboboijbob")) # = 3
print(count_bobs("bobaoboboaidjbobd")) # = 3
print(count_bobs("bobbobbobbobbob")) # 5
