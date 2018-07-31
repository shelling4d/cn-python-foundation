# coding=utf-8
import csv
import requests
from bs4 import BeautifulSoup
import expanddouban

"""
return a string corresponding to the URL of douban movie lists given category and location.
"""


def getMovieUrl(category, location):
    url = 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,{},{}'.format(category, location)
    return url


# 创建电影类
class Movie():
    def __init__(self, name, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link

    def write_data(self):
        return "{},{},{},{},{},{}".format(self.name, self.rate, self.location, self.category, self.info_link,
                                          self.cover_link)

    def get_list(self):
        a = []
        a.append(self.name)
        a.append(self.rate)
        a.append(self.location)
        a.append(self.category)
        a.append(self.info_link)
        a.append(self.cover_link)
        return a


"""
return a list of Movie objects with the given category and location.
"""


def getMovies(category, location):
    movies = []
    url = getMovieUrl(category, location)
    html = expanddouban.getHtml(url, True)
    soup = BeautifulSoup(html, 'html.parser')
    content_a = soup.find(id='content').find(class_='list-wp').find_all('a', recursive=False)
    for element in content_a:
        M_name = element.find(class_='title').string
        M_rate = element.find(class_='rate').string
        M_location = location
        M_category = category
        M_info_link = element.get('href')
        M_cover_link = element.find('img').get('src')
        movies.append(Movie(M_name, M_rate, M_location, M_category, M_info_link, M_cover_link).get_list())
    return movies  # 这里的movies是列表，元素是一个列表


favorite_types = ("剧情", "喜剧", "科幻")
locations = (
    "中国大陆", "美国", "香港", "台湾", "日本", "韩国", "英国", "法国", "德国", "意大利", "西班牙", "印度", "泰国", "俄罗斯", "伊朗", "加拿大", "澳大利亚", "爱尔兰",
    "瑞典", "巴西", "丹麦")

"""将电影信息存储在movies_list里面 """
movies_list = []
for favorite_type in favorite_types:  # 类型有3个
    d_nums = {}
    n = 0
    for loc in locations:  # 地区为全部地区
        tmp_movies = getMovies(favorite_type, loc)
        movies_list = movies_list + tmp_movies
        d_nums[loc] = len(tmp_movies)
        n += len(tmp_movies)
    sorted_d_nuums = sorted(d_nums.items(), key=lambda d_nums: d_nums[1], reverse=True)
    # sortef_d是由元组组成的列表[(key,value), (key,value)]
    with open('output.txt', 'a') as txt:
        txt.write("在{0}类型中，数量排名前三的地区有{1},{2},{3}，分别占此类电影总数的{4:.2%},{5:.2%},{6:.2%}\n".format(favorite_type,
                                                                                             sorted_d_nuums[0][0],
                                                                                             sorted_d_nuums[1][0],
                                                                                             sorted_d_nuums[2][0],
                                                                                             int(sorted_d_nuums[0][
                                                                                                     1]) / n,
                                                                                             int(sorted_d_nuums[1][
                                                                                                     1]) / n,
                                                                                             int(sorted_d_nuums[2][
                                                                                                     1]) / n))
        txt.close()

"""写入CSV文件"""
with open('movies.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(movies_list)
    f.close()
