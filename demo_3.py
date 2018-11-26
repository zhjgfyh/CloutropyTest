# Date: 2018.11.12
# ToDo: 练习isinstance和列表生成式

# -*- coding:utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)

if L2 == ['hello', 'world', 'apple']:
    print("测试通过")

else:
    print("测试失败")