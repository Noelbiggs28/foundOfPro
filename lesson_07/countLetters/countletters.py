def count_letters(sent):
    amount={}
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cap_letters = sent.upper()
    for letter in alpha:
        if letter in cap_letters:
            amount[letter] = cap_letters.count(letter)
    return amount
print(count_letters("The quown$%#$$#%3 Fox  Dog")) 