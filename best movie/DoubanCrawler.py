# coding=utf-8
"""
项目2 豆瓣上最好的电影

在这个项目中, 你将会从豆瓣电影的网页中获取你最爱的三个类别，各个地区的高评分电影，收集他们的名称、评分、电影页面的链接和电影海报的链接。最后对收集的数据进行简单的统计。
这个项目不会提供任何 python 代码，你应该新建文件 `DoubanCrawler.py`, 并在其中逐个完成每个任务。注意这些任务并不是并列关系，后面的任务很可能需要用到前面任务的代码或函数，前面任务的对错也很可能会影响后面任务的对错。你可能会需要多次来回修改才能完成项目。
"""

"""导入模块"""
import csv
import requests
from bs4 import BeautifulSoup
import expanddouban

urls = "https://movie.douban.com/tag/#/"  # 豆瓣电影分类页面

"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
    url = 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=' + str(category) + "," + str(location)
    return url


# 打印测试
url = getMovieUrl("喜剧", "美国")
print("url:", url)

"""获取HTML"""
html = expanddouban.getHtml(url)


# print("html2:", html)


# 创建电影类
class Movie():
    def __init__(self, name, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link

    def show(self):
        return "{},{},{},{},{},{}".format(self.name, self.rate, self.location, self.category, self.info_link,
                                          self.cover_link)


"""
return a list of Movie objects with the given category and location.
"""
def getMovies(category, location):
    movies = []
    for loc in location:
        url = getMovieUrl(category, location)
        html = expanddouban.getHtml(url, True)
        soup = BeautifulSoup(html, 'html.parser')
        content_a = soup.find(id='content').find(class_='list-wp').find_all('a', recursive=False)
        print("捕捉内容为：", content_a)
        for element in content_a:
            M_name = element.find(class_='title').string
            M_rate = element.find(class_='rate').string
            M_category = category
            M_info_link = element.get('href')
            M_cover_link = element.find('img').get('src')
            movies.append(Movie(M_name, M_rate, M_location, M_category, M_info_link, M_cover_link).show())
    return movies

content = getMovies("喜剧", "美国")
favorites = ("喜剧", "科幻", "动作")

"""写入CSV文件"""
with open('movies.csv', 'w', newline='') as f:
    spamwriter = csv.writer(f, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_NONE)

types = ("剧情", "喜剧", "动作", "爱情", "科幻", "悬疑", "惊悚", "恐怖", "犯罪", "同性",
         "音乐", "歌舞", "传记", "历史", "战争", "西部", "奇幻", "冒险", "灾难", "武侠", "情色")
locations = ("中国大陆", "美国", "香港", "台湾", "日本", "韩国",
             "英国", "法国", "德国", "意大利", "西班牙", "印度", "泰国", "俄罗斯", "伊朗", "加拿大", "澳大利亚", "爱尔兰", "瑞典", "巴西丹麦")
