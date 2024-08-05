# name = input("what is your name?")
# if name == "elisabeth":
#     print("welcome on board queen")
# else:
#     print("good morning")


# animals_and_numbers = ["zebra", "cat", "otter", "rabbit", 1, 4]

# print(animals_and_numbers)
# print(len(animals_and_numbers))
#
# print(animals_and_numbers[1])
# print(animals_and_numbers[-1])
# print(animals_and_numbers[0:3])
#
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)
#
# fruits = ['apple', 'banana', 'orange']
# fruits.append('cherry')
# print(fruits)
#
# fruits.insert(2, 'lemon')
# print(fruits)

# fruits.remove('orange')
# print(fruits)
# fruits.insert(3, 'kiwi')
# print(fruits)
# print(fruits)
# fruits[3] = 'kiwi'
# print(fruits)
#
# lst = [3, 0, 1, 5, 2]
# x = 2
#
# print(lst[0])
# print(lst[3])
# print(lst[2])
# print(lst[-2])
# print(lst[2+1])
# print(lst[2]+1)
# print(lst[lst[2]])
# print(lst[lst[lst[2]]])

# create a program to prompt the user to insert item into an empty list

# def print_list(l):
#     for num in l:
#         print(num, ' ', end='')
# l= []
# while True:
#     answer =('enter a number')
#     if answer == "101":
#         break
#     l.append(int(answer))
#
# print_list(l)
#
# my_list = []
# elements = int(input("how many items do you want in your list?"))
# for i in range(elements):
#     item = input("please enter an item of your list: ")
#     my_list.append(item)
#
# print("my final list is", my_list)
#
# global_list = ("tree", 99, 'mouse')
# print(type(global_list))
#
# my_list = list(global_list)
# print(type(my_list))

# tuple1 = ("orange", [10,20,30], (5,15,25))
# print(tuple1[1][1])
# print(tuple1[2][1])
# tuple1[1][1] = 40
# print(tuple1)
#
# tuple1 = (23,1,45,67,45,9,55,45)
# tuple2 = (100,200)
#
# print(tuple1.index(45))
# print(tuple1.count(45))
# print(tuple1 + tuple2)
# print(len(tuple2))
# print(max(tuple1))
# print(min(tuple1))
#
# print(23 in tuple1)
#
# print("cat" not in tuple2)
#
# dict3 = {'Mohan': 95, 'Ram': 89, 'Suhel': 92, 'Sangeeta': 85}
# print(dict3)
# dict3['Safa'] = 99
# print(dict3)
#
# dict3['Ram'] = 75
# print(dict3)

# for x, y in dict3.items():
#     print(x, "grade is", y)
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10,20,30]
#
# full_dict = dict(zip(keys, values))
# print(full_dict)

# set1 = {"apple", "cherry", 3 ,"mango"}
# set2 = {3, 9, 12,}
# union_sets = set1 | set2
# print(union_sets)
#
# intersection_sets = set1 & set2
# print(intersection_sets)
#
# difference_sets = set1 - set2
# print(difference_sets)

# symmetric_differences = set1 ^ set2
# print(symmetric_differences)
#
# set_membership = 3 in set1
# print(set_membership)
#
# set_membership2 = 'apple' in set2
# print(set_membership2)
#
# set_equality = set1 ==set2
# print(set_equality)
#
# subset = set1 <= set2
# print(subset)
#
# proper_subset = set1 < set2
# print(proper_subset)

# sample_set = {'yellow', 'orange', 'black'}
# sample_list = ['blue', 'green', 'red']
#
# sample_set.update(sample_list)
# print(sample_set)



# def welcome_message():
#     print('welcome everyone !')
#
# print(welcome_message())

# def addition(num1, num2):
#     # num1 = 5
#     # num2 = 10
#     n = num1 + num2
#     return n
#
# print(addition(3, 4))
#
# def simple_add():
#     num1 = int(input('enter the 1st number:'))
#     num2 = int(input('enter the 2nd number:'))
#     result = num1 + num2
#     return result
#
# print(simple_add())

# def login_check():
#     username = (input('enter the username:'))
#     password = (input('enter the password:'))
#     if username == 'admin' and password =='password':
#         print('access granted!')
#     else:
#         print('access denied')
#         return(login_check())
#
# print(login_check())

# q1
# list1 = [2,4,5,6,7]
# list2 = ['dog', 'cat', 'bear']

# q16
# e= ['708596@gmail.com', '1345993@outlook.com']
# # print(type(emails_students))
# names = [n.split('@',1)[0] for n in e]
# print(names)
# domain = [i.split('@', -1)[-1] for i in e]
# print(domain)
#
# tuple_emails =tuple(e)
# tuple_usernames =tuple(names)
# tuple_domains =tuple(domain)
#
# print(tuple_emails)
# print(tuple_usernames)
# print(tuple_domains)


# q17
names = tuple(input('what are the students names?'))
for i in names:
    user_name = tuple(input('enter your name student:'))
    if user_name in names:
        print('student present')
    else:
        print('student not in list')

