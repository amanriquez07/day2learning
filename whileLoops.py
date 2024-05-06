# nums = [1, 2, 3, 4, 5,]
# for num in nums:
#     for letter in 'abc':
#         print(num, letter)  
#         # nested forloop


#     if num == 3:
#         # print('Found! ')
#         continue
#     print(num)

# # RANGES and arrange of numbers
# for i in range(77):
#     print(i)

# # WHILE LOOPS - are for when you dont know a number you want to start or stop with (they go on forever)         unless you tell python to add one(for x)- it will always stay zero
# x = 0
# while True:
#     if x == 5:
#         break
#     print(x)
#     x += 1



while True:
    print("Enter your name:")
    name = input()
    if name == 'your name':
        print("your name is" +name)
        break
    else:
        print("Thank you!")