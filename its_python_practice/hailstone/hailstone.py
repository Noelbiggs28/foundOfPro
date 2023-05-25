usernum = int(input('Enter starting number: '))
def hailstone(num):
    count = 0
    if num <= 0:
        return 'please enter a positive number you!'
    if num ==1:
        return 0

    while num != 1:
        if num % 2 == 0:
            num /= 2
            count += 1
        else:
            num = num * 3 + 1
            count += 1
    return count    
print(hailstone(usernum))

