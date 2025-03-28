
# @Author  : loong2525
# @File    : list.py
# @Software: vscode

#list first meeting
message = "hello world"
print(message)

name=["shi","jin","jia"]
print("My name is "+name[0].title()+" "+name[1].title()+name[2])

#字符串操作:对name做.操作
'''
name[0].title()                  #首字母大写
name.upper()                     #全部大写
name.lower()                     #全部小写
name.rstrip()                    #删除末尾空白
name.lstrip()                    #删除开头空白
name.strip()                     #删除两端空白
#列表操作
name.sort()                      #永久排序以“a”-“z”
name.sort(reverse=True)          #永久排序以“z”-“a”
sorted(name)                     #临时排序以“a”-“z”
len(name)                        #获取列表长度
name.append("chen")              #在列表末尾添加元素
name.insert(0,"shi")             #在列表任意位置添加元素
del name[0]                      #删除列表任意位置元素
name.pop(0)                      #删除列表任意位置元素并返回
name.remove("shi")               #删除列表中指定元素
name.clear()                     #清空列表
name.copy()                      #复制列表
name.index("shi")                #查找列表中指定元素位置'
'''





#for 遍历列表

for i in name:
    print(i.upper())
for i in range(1,6,2):            #从1到6，步长为2;range(start,stop,step)
    print(i)


number = list(range(1,6))         #创建数字列表
for num in number:  
    print(num**2)                 #python支持指数运算符**
'''
min(number)                      #获取数字列表最小值
max(number)                      #获取数字列表最大值
sum(number)                      #获取数字列表和
'''
print(str(min(number)) + ',' + str(max(number)) + ',' + str(sum(number)))
#列表解析：通过列表解析创建列表
squares = [value**2 for value in range(1,11)]
print(squares)

#切片操作
name = ["shi","jin","jia","chen","xiao","tong"]     #注意这里覆盖了上面的name
print("1."+str(name[0:3]))
print("2."+str(name[:3]))                                #索引的省略
print("3."+str(name[3:]))

#复制列表
name_again = name[:]                                #[:]表示复制列表
print("4."+str(name_again))
#注意：比较两种方式
name_again = name[:]
name_error = name
name_again.append("chen")
name_error.append("xiao")
print("<1>"+str(name_again))                               #name_again是name的副本，添加元素不影响原列表
print("<2>"+str(name_error))                               #name_error和name指向同一列表，添加元素会影响原列表

#元组操作
#元组是不可变的列表，不能修改元素
name = ("shi","jin","jia","chen","xiao","tong")            #注意元组用()表示，只能被覆盖，不能修改
print(name)                    
name = ("他已经被覆盖")
print(name)                                              





#if 语句
names = {"Shi Jinjia","Chen Xiaotong"}
print (names)
for name in names:
    if name == "Shi Jinjia":                
        print("hello, Shi Jinjia")               
    elif name == "Chen Xiaotong":               #当if为0，elif才会执行
        print("hello, Chen Xiaotong")       
    else:
        print("error")
#__注意__：if区分大小写

print('shijinjia是否在列表中：\n' )           #判断元素是否在列表中
if "Shi Jinjia" not in names:               #判断元素是否在列表中
    print("NO")
else:
    print("YES")

name = []                    
if name :                                    #if判断列表是否为空
    print("列表不为空")
else:
    print("列表为空")



