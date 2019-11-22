# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

# req = requests.get(url='https://www.biqubao.com/book/18370/7759796.html')
# # print(req.encoding)
# req.encoding = 'gbk'
# # print(req.text)
# # html = 'https://www.biqubao.com/book/17587/9344164.html'
# soup = BeautifulSoup(req.text, 'html.parser')     # html为您的html内容
# print(soup.h1.text)
# contents = soup.find_all('div', id="content")[0].text.replace('    ', '\n')
# # contents = contents.replace('    ', '\n')
# # contents_list = contents.split(
# print(contents)
# # for dd in soup.find_all('dd'):
# #     print(" 标题：{}，链接：{}".format(dd.a.string, dd.a.get('href')))


def new_novel_detail(url, novel_name):
    # https://www.biqubao.com/    的具体每一章内容的结构爬出代码
    # nov_headers = {
    #     "User-Agent": random.choice(uapools)
    # }
    res = requests.get(url)
    res.encoding = 'gbk'
    soup = BeautifulSoup(res.text, 'html.parser')

    rst_title = soup.h1.text
    rst_novel = soup.find_all('div', id="content")[0].text.replace('    ', '\n').replace(u'\xa0', u' ')
    print(rst_title)
    try:
        with open(novel_name, 'a') as fileobject:
            fileobject.writelines(rst_title + '\n')
            fileobject.writelines(rst_novel+ '\n')
    except Exception as ex:
        print('repr(e):\t', repr(ex))
        with open(novel_name, 'a') as fileobject:
            fileobject.writelines(rst_title + '\n')
            fileobject.writelines(repr(ex) + '\n')


if __name__ == '__main__':
    new_novel_detail('https://www.biqubao.com/book/18370/7759796.html', '剑来.txt')