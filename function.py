# @Author  : loong2525
# @File    : function.py
# @Software: vscode

#define a function
def greet_user(user_name):
    print("hello,"+user_name.title()+"!")
greet_user('loong2525')

#实参：位置实参，关键字实参，列表实参，字典实参
#1.位置实参
def describe_pet(animal_type,pet_name):
    print("I have a "+animal_type+" named "+pet_name.title()+".")
describe_pet('dog','loong')
#2.关键字实参
describe_pet(animal_type='cat',pet_name='loong')
#3.默认值实参
def describe_pet(pet_name,animal_type='cat'):
    print("I have a "+animal_type+" named "+pet_name.title()+".")
describe_pet('loong')
#return作为返回值，可以返回字符串，字典
#传递列表，字典

#传递不是先定义数量的参数
def make_pizza(*toppings):
    print(toppings)
make_pizza('mushrooms','green peppers','extra cheese')



#函数-->模块
#导入模块（复制该文件中的所有代码）
import list
#导入特定函数并用as关键字设置别名(复制特定函数，复制语句)
from dictionary import test as t
#import list = from list import * 
t()
