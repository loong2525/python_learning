# @Author  : loong2525
# @File    : input and while.py
# @Software: vscode

#user's input 

age = input("Tell me your age,and I will repeat it back to you:")
print (age)
#Notice: input将用户的输入视为string
# if you use "python 2.7",please use the raw_input() instead of the input()

age = int(age)
if age >= 18:
    print("you are a adult")

# while and sign
active = True
while active :
    
    if age=="quit":
        active = False
    else:
        age = input("Tell me your age,and if you input the 'quit',the program will end")

#notice: break and continue is useful,still

# use while to deal with the list and dictionary

list = ['A','B','a','b']
while 'b' in list:
    list.remove('b')
print (list)

while list :
    print ("NOT NULL")
#python 认为字符串，列表，字典都可以被认为为表达式





