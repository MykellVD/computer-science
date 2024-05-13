
# function that counts vowels in a given string
def count_vowels(string):
    vowels = ["a","e","i","o","u","y"]
    vowel_count = 0
    for i in string:
        if i in vowels:
            vowel_count += 1
    return vowel_count


print(count_vowels("azcbobobegghakl")) # = 5
print(count_vowels("oawihiohawdfi")) # = 7
print(count_vowels("ojwdafoojdkylund")) # = 6
