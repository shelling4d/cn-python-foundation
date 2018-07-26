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

# 建立短信号码集合，包含发送号码和接收号码
TextPhone = set([x[0] for x in texts]) | set([x[1] for x in texts])
# 建立被叫号码集合
CalledPhone = set([y[1] for y in calls])
# 建立主叫号码集合
CallPhone = set([y[0] for y in calls])

# 根据特征 推销电话： 0短信 0被叫 all主叫
SalesCalls = CallPhone - (TextPhone | CalledPhone)
SalesCalls_list = list(SalesCalls)
SalesCalls_list.sort()

print("These numbers could be telemarketers: ")

# 遍历打印SalesCalls_list
for SalesCall in SalesCalls_list:
    print(SalesCall)

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""
