from typing import List, Any

import requests
import socket
import random
import re
import time
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.filedialog
from bs4 import BeautifulSoup


socket.setdefaulttimeout(30)

# 用户代理池的构建
uapools = [
    "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
    "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
    "Mozilla/2.02E (Win95; U)",
    "Mozilla/3.01Gold (Win95; I)",
    "Mozilla/4.8 [en] (Windows NT 5.1; U)",
    "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
    "HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.2; U; de-DE) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/234.40.1 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-us; htc_bahamas Build/CRB17) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; HTC Desire 1.19.161.5 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 1.5; de-ch; HTC Hero Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.1; en-us; HTC Legend Build/cupcake) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 1.5; de-de; HTC Magic Build/PLAT-RC33) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 FirePHP/0.3",
    "Mozilla/5.0 (Linux; U; Android 1.6; en-us; HTC_TATTOO_A3288 Build/DRC79) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-us; T-Mobile G1 Build/CRB43) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari 525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-gb; T-Mobile_G2_Touch Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Milestone Build/ SHOLS_U2_01.03.1) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.0.1; de-de; Milestone Build/SHOLS_U2_01.14.0) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522  (KHTML, like Gecko) Safari/419.3",
    "Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-ca; GT-P1000M Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.6; en-us; SonyEricssonX10i Build/R1AA056) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
]


def novel(url_novel):
    plogSaveName = 'jianlai.txt'
    url = url_novel
    nov_headers = {
        "User-Agent": random.choice(uapools)
    }
    res = requests.get(url, headers=nov_headers)
    time.sleep(3)
    content = res.content.decode('utf-8')
    pat = '<div id="BookText">(.*?)<script'
    pat_title = '<h1>(.*?)</h1>'
    rst_title = re.compile(pat_title).findall(content)
    print(rst_title)
    with open(plogSaveName, 'a') as fileobject:
        fileobject.writelines('\n'+rst_title[0]+'\n')

    rst = re.findall(pat, content, re.S)

    for rets in rst:
        pat_rets = "<p>(.*?)</p>"
        nov_con = re.findall(pat_rets, rets)
        for nov_cons in nov_con:
            try:
                with open(plogSaveName, 'a') as fileobject:
                     fileobject.writelines(nov_cons + '\n')
            except Exception as ex:
                continue
# -----------------------------------------------------


def new_novel_detail(url, novel_name):
    # https://www.biqubao.com/    的具体每一章内容的结构爬出代码
    nov_headers = {
        "User-Agent": random.choice(uapools)
    }
    res = requests.get(url, headers=nov_headers)
    res.encoding = 'gbk'
    soup = BeautifulSoup(res.text, 'html.parser')

    rst_title = soup.h1.text
    rst_novel = soup.find_all('div', id="content")[0].text.replace('    ', '\n').replace(u'\xa0', u' ')
    print(rst_title)
    try:
        with open(novel_name, 'a') as fileobject:
            fileobject.writelines(rst_title + '\n')
            fileobject.writelines(rst_novel + '\n')
    except Exception as ex:
        print('repr(e):\t', repr(ex))
        with open(novel_name, 'a') as fileobject:
            fileobject.writelines(rst_title + '\n')
            fileobject.writelines(repr(ex) + '\n')


def biquge_info(url):
    # https://www.biqubao.com/  小说章节链接爬出代码
    global each_url
    novel_total_num = 0
    novel_current_num = 0
    text.set('下载中...')
    nov_headers = {
        "User-Agent": random.choice(uapools)
    }
    res = requests.get(url, headers=nov_headers)
    res.encoding = 'gbk'
    soup = BeautifulSoup(res.text, 'html.parser')
    rst_novel_urls = soup.find_all('dd')  # 每章的标题和链接位置
    rst_novel_title = soup.h1.text  # 小说标题
    print(rst_novel_title)
    txt_novel = rst_novel_title + '.txt'
    title.set(txt_novel)
    root.update()

    novel_total_num = rst_novel_urls.__len__()  # 小说总章节数
    for each in rst_novel_urls:
        each_url = each.a.get('href')
        final_url = each_url.split('/')[-1]
        # print(" 标题：{}，链接：{}".format(each.a.string, each_url))
        novel_current_num = novel_current_num + 1
        percent = int(100*novel_current_num/novel_total_num)
        text.set('下载了 '+percent.__str__()+'%')
        percent_x = int(300*novel_current_num/novel_total_num)
        process(percent_x)

        url_str = url + final_url
        print(url_str)
        new_novel_detail(url_str, txt_novel)
    text.set('下载完成')


def process(x):
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 21, width=0, fill='green')
    canvas.coords(fill_line, (1, 1, x, 22))
    root.update()


def btn_point():
    novel_url = txt_url.get()
    # novel_title = txt_title.get()
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 21, width=0, fill='white')
    canvas.coords(fill_line, (1, 1, 300, 22))
    root.update()
    biquge_info(novel_url)


if __name__ == '__main__':

    # # 全局变量
    # novel_total_num = 0
    # novel_current_num = 0

    root = Tk()
    root.title('biquge.info 小说下载器')
    root.resizable(False, False)
    root.geometry('400x200')
    # tkinter.messagebox.showinfo('messagebox','This is a dialog')
    path_var = tkinter.StringVar()
    text = StringVar()
    text.set('下载进度：')
    title = StringVar()
    title.set('未输入书名')

    lab1 = tkinter.Label(root, text='小说下载器').grid(row=0, column=0)
    lab2 = tkinter.Label(root, text='小说书名：').grid(row=1, column=0)
    lab3 = tkinter.Label(root, text='小说首页：').grid(row=2, column=0)

    # 设置下载进度条
    lab5 = tkinter.Label(root, textvariable=text).place(x=0, y=100)
    canvas = tkinter.Canvas(root, width=300, height=20, bg='white')
    canvas.place(x=65, y=100)

    # txt_title = tkinter.Entry()
    txt_title = tkinter.Label(root, textvariable=title)
    txt_title.grid(row=1, column=1)
    txt_url = tkinter.Entry()
    txt_url.grid(row=2, column=1)
    btn: None = tkinter.Button(root, text='下载_提交', command=btn_point).grid(row=3, column=2)
    root.mainloop()

    # biquge_info('https://www.biquge.info/41_41185/')
