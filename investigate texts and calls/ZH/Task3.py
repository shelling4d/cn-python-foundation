"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# 建立一个二维列表，主叫、被叫
l = ([x[0:2] for x in calls])

# 建立一个空列表，用来盛放班加罗尔主叫、被叫号码
new_l = []

n = 0
for i in l:
    if '(080)' in i[0]:
        new_l.append(i)
        if '(080)' in i[1]:
            n = n + 1
code_list = []
for j in new_l:
    # 提取固定电话的区号，如果号码中存在"(",则该电话号码是固定电话，找到")"第一次出现的索引。得到区号
    if '(' in j[1]:  # 获得区号加入代码序列
        code_list.append(j[1][1:j[1].index(')')])
    elif ' ' in j[1]:  # 获得移动代码加入代码序列
        if j[1][0] in '789':
            code_list.append(j[1][:4])
    else:
        code_list.append('140')

# 列表转换为集合来去除重复
code_set = set(code_list)

code_list = list(code_set)

# 列表排序
code_list.sort()

print("The numbers called by people in Bangalore have codes:")
for name in code_list:
    print(name)
print("{}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    '%.2f%%' % (n / len(new_l) * 100)))

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
