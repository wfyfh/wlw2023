my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.get('name'))  # 输出：Alice
print(my_dict.get('gender'))  # 输出：None
print(my_dict.get('gender', 'unknown'))  # 输出：unkn

import json

strDict = '{"city": "广州", "name": "小黑"}'

r = json.loads(strDict) # json数据自动按Unicode存储

print(r)