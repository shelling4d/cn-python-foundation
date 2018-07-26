"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

call_num = [x[0:4:3] for x in calls]  ##创建一个主叫号码，通话时间序列
called_num = [x[1:4:2] for x in calls]  ##创建一个被叫叫号码，通话时间序列

d = dict()  # 创建一个空字典

for i in call_num:

    if i[0] in d:
        d[i[0]] = int(d[i[0]]) + int(i[1])
    else:
        d[i[0]] = int(i[1])

for j in called_num:
    if j[0] in d:
        d[j[0]] = int(d[j[0]]) + int(j[1])
    else:
        d[j[0]] = int(j[1])

max_time_phone = max(d, key=d.get)
max_time = d[max_time_phone]
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_time_phone, max_time))

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""