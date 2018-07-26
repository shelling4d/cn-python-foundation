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

txtphone_out = [x[0] for x in texts]  # 提取发送电话列表
txtphone_in = [y[1] for y in texts]  # 提取接收电话列表

callphone_out = [m[0] for m in calls]  # 提取主叫电话列表
callphone_in = [n[1] for n in calls]  # 提取被叫电话列表

# 电话号码列表集合化，并取并集

all_phone = set(txtphone_out) | set(txtphone_in) | set(callphone_out) | set(callphone_in)
phone_num = len(all_phone)

print("There are {count} different telephone numbers in the records.".format(count=phone_num))


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records.
"""
