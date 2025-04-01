
# @Author  : loong2525
# @File    : dictionary.py
# @Software: vscode

# dictionary first meeting
#字典用于关联起相关信息
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
#字典是一系列的键-值对 (key-value pair)
#字典的键是唯一的，值可以是重复的
#字典的值可以是任何数据类型
#字典的键可以是任何不可变的数据类型
#字典的键可以是字符串、数字、元组等不可变的数据类型

#添加键-值对
alien_0 ['x_position']=0
alien_0 ['y_position']=25
print(alien_0)
#删除键-值对
del alien_0['points']
print(alien_0)
#修改字典的值
alien_0['color']='yellow'
print(alien_0)

#遍历字典
for key, value in alien_0.items():
    print(key + ': ' + str(value))
#遍历字典的键
for key in alien_0.keys():
    print(key)
#遍历字典的值
for value in alien_0.values():
    print(value)

#字典的嵌套 字典和列表的结合
# ~列表中的字典
alien_0={'color': 'green', 'points': 5}
alien_1={'color': 'yellow', 'points': 10}
alien_2={'color': 'red', 'points': 15}
aliens=[alien_0, alien_1, alien_2]
print(aliens)
#注意：列表中的每一个字典都是独立的，可以修改
# ~字典中的字典
#aliens={alien_0, alien_1, alien_2}
# print(aliens)                 error: TypeError: unhashable type: 'dict'---字典直接作为键是被警告的
#字典中的字典是不可变的，不能修改

for color, points in alien_0.items():            #用.items()方法遍历字典
    print(color + ': ' + str(points))

'''
被function调用的函数
'''
def test():
    print("the test function is called")