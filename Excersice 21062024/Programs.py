#Right Triangle Star Pattern
# n = 5
# *
# **
# ***
# ****
# *****

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end="")
    print()

# #Palidrome of String
# i/p = naman , nitin, level
# o/p = true
# i/p = pramod
# o/p = false


str = input("Enter a string: ") #aman
rev_str = str[::-1] #aman
if str == rev_str:
    print("True")
else:
    print("False")




#✅ String Reverse
#3-4 ways to do this in Python

# i/p = "1234"
# o/p = "4321"

str = input("Enter a string: ") #aman
rev_str = ""
for i in str:
    rev_str = i + rev_str
    print(rev_str)
    # print(i, end="") #4321

#✅ Count vowels and consonants in a String

def count_vowels_and_consonants(s):
    vowels = 'aeiou'
    s = s.lower()
    vowel_count = 0
    consonant_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

s = input("Enter a string: ")
vowels, consonants = count_vowels_and_consonants(s)
print(f"Vowels: {vowels}, Consonants: {consonants}")

#String s1 = "silent";
#String s2 = "listen";
#namo - mano - onam
#An anagram is a word or phrase formed by rearranging the letters of a different word or phrase

#For example, the word "listen" can be rearranged to form the word "silent".

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if sorted(s1) == sorted(s2):
    print("The strings are anagrams.")

else:
    print("The strings are not anagrams.")






