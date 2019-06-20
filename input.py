# 1. input()
#name = input("please enter your name: ")
#print("Hello, " + name + "!")

# 使用int()来获取数值输入
age = input("How old are you? ")
# 默认input的是字符串，尝试运行下面的程序即可知道
age = int(age)
if age >= 18:
    print("\n you are an adult")
else:
    print("you are not an adult")

# python2 使用 raw_input() 来提示用户输入；Python2 也有input()函数，但是它将输入解读为python代码
