change = int(input('Please enter an amount in cents less than a dollar:\n'))
# arr=[25, 10, 5, 1]
# ans=[0,0,0,0]
# for i in range(len(arr)):
#     while change >= arr[i]:
#         change -= arr[i]
#         ans[i] += 1
# print(f"Your change will be:\nQ:{ans[0]}\nD:{ans[1]}\nN:{ans[2]}\nP:{ans[3]}\n")
Quarters = change // 25   
change = change % 25
Dimes = change // 10   
change = change % 10
Nickles = change // 5   
change = change % 5
Pennies = change  

print(f"Your change will be:\nQ: {Quarters}\nD: {Dimes}\nN: {Nickles}\nP: {Pennies}") 