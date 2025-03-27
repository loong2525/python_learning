message = "hello world"
print(message)

name=["shi","jin","jia"]
print("My name is "+name[0].title()+" "+name[1].title()+name[2])

#字符串操作
name.title()                     #首字母大写
name.upper()                     #全部大写
name.lower()                     #全部小写
name.rstrip()                    #删除末尾空白
name.lstrip()                    #删除开头空白
name.strip()                     #删除两端空白
#列表操作
name.sort()                      #永久排序以“a”-“z”
name.sort(reverse=True)          #永久排序以“z”-“a”
sorted(name)                     #临时排序以“a”-“z”
len(name)                        #列表长度
name.append()                    #在列表末尾添加元素
name.insert(0,"shi")             #在列表任意位置添加元素
del name[0]                      #删除列表任意位置元素
name.pop(0)                      #删除列表任意位置元素
name.remove("shi")               #删除列表中指定元素

