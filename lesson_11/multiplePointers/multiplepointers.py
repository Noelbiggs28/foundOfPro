# def sumZero(ls):
#     length = len(ls)
#     for first_pointer in range(length):
#         for second_pointer in range(first_pointer + 1, length):
#             if ls[first_pointer] + ls[second_pointer] == 0:
#                 return [ls[first_pointer],ls[second_pointer]]
#     return -1


# print(sumZero([-3, -2, -1, 0, 1, 2, 3])) # [-3, 3]
# print(sumZero([-10, -5, 0, 1, 3, 5, 87, 99])) # [-5, 5]
# print(sumZero([-2, 0, 1, 3])) # -1
# print(sumZero([1, 2, 3])) # -1

#def function
#   pointer 1
#   pointer 2
#   while condition
#        result to check
#            return true if met
#            move left pointer
#            mover right pointer
#   nver met return false
    

def sumZero(int_list):
    left = 0
    right = len(int_list) -1
    while left < right:
        total = int_list[left] + int_list[right]
        if total == 0:
            return [int_list[left], int_list[right]]
        elif total > 0:
            right -= 1
        else: 
            left += 1
    return -1

print(sumZero([-3, -2, -1, 0, 1, 2, 3])) # [-3, 3]
print(sumZero([-10, -5, 0, 1, 3, 5, 87, 99])) # [-5, 5]
print(sumZero([-2, 0, 1, 3])) # -1
print(sumZero([1, 2, 3])) # -1
