#***************************************** 使用while循环 ***********************************************************
#current_number = 1
#while current_number <= 5:
#    print(current_number)
    # current_number = current_number +1 的简写
#    current_number += 1

# 让用户选择何时退出
prompt = "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
#message = ""
#while message != 'quit':
#    message = input(prompt)
#    if message != 'quit'
#    print(message)

# 使用标志
#active = True
#while active:
#    message = input(prompt)
#    if message == 'quit':
#        active =False
#    else:
#        print(message)

# 使用 break 退出循环
#while True:
#    city = input(prompt)
#    if city == 'quit':
#        break
#    else:
#        print("I'd love to go to "+city.title()+"!")

# 在循环中使用 continue ， 返回循环的开头，并根据条件测试结果决定是否继续执行循环
current_number = 0
while current_number < 10:
    current_number +=1
    if current_number % 2 ==0:
        continue
    print(current_number)

#************************************使用while 循环处理列表和字典 *****************************************************************
# 1. 在列表之间移动元素
#首先，创建一个待验证的用户列表和一个用于存储已验证用户的空列表
unconfirmed_users = ['Alice','Brain','Candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: "+ current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 2.删除包含特定值的所有列表元素
# 假设你有一个宠物列表，其中包含多个值为‘cat’的元素。要删除所有这些元素，可不断运行一个while循环，直到列表中不再包含值‘cat’,如下所示：
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# 3. 使用用户输入来填充字典
responses = {}

#设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    #提示输入被调查者的名字和回答
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday? ")

    #将答卷存储在字典中
    responses[name] =response

    #看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond?(yes/no) ")
    if repeat == 'no':
        polling_active = False
#调查结束，显示结果
print("\n--- Poll Result ---")
for name,response in responses.items():
    print(name+ " would like to climb "+response+".")

