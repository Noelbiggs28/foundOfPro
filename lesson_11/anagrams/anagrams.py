def validAnagram(string1, string2):
    if len(string1) != len(string2):
        return False
    
    letter_dict = {}
    for letter in string1:
        if letter in letter_dict:
            letter_dict[letter] +=1
        else:
            letter_dict[letter] = 1

    for letter in string2:
        if letter in letter_dict and letter_dict[letter] > 0:
            letter_dict[letter] -= 1
        else:
            return False
    return True


print(validAnagram('aaz', 'zza')) # false
print(validAnagram('anagram', 'nagaram')) # true
print(validAnagram('rat', 'car')) # false
print(validAnagram('qwerty', 'qeywrt')) # true