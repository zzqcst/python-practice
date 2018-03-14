import requests
import time
from bs4 import BeautifulSoup
from lxml import etree

# link = "https://www.baidu.com"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
# r = requests.get(link, headers=headers)
# soup = BeautifulSoup(r.text, 'lxml')
# title = soup.find('div', class_='qrcode-text').p.b.text.strip()
# print(title)
# with open('result.txt', 'w+') as file:
#     file.write(title)
# print('文本编码：', r.encoding)
# print('响应状态码：', r.status_code)

key_dic = {'key1': 'value1', 'key2': 'value2'}


# r = requests.get('http://httpbin.org/get', params=key_dic, headers=headers)
# print(r.url)
# print(r.text)


# 豆瓣top250电影排行榜
def get_movies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
    link = 'https://movie.douban.com/top250'
    cookies = {}
    cookie = "ll=118123; bid=w1YOdx0gLVo; __utmc=30149280; __utmc=223695111; _vwo_uuid_v2=DA32C34DDE18098256E5B4A30F80AF0B1|6473f7fd6c1a4af4a52eaefe878dc591; ps=y; ue=1025887167@qq.com; dbcl2=91206054:0SkQZIBrMN4; ck=hh_8; __utma=30149280.49989366.1520840472.1520840472.1520852845.2; __utmb=30149280.0.10.1520852845; __utmz=30149280.1520852845.2.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utma=223695111.2142919457.1520840472.1520840472.1520852845.2; __utmb=223695111.0.10.1520852845; __utmz=223695111.1520852845.2.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1520852846%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Falias%3D18624323501%2540163.com%26redir%3Dhttps%253A%252F%252Fmovie.douban.com%252Ftop250%253Fstart%253D25%26source%3DNone%26error%3D1012%22%5D; _pk_ses.100001.4cf6=*; push_noty_num=0; push_doumail_num=0; ap=1; _pk_id.100001.4cf6=096805f367ac313a.1520840472.2.1520854004.1520842497."
    for line in cookie.split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    print('cookies:', cookies, end='\n\n')
    movie_names = []
    origin_names = []
    for i in range(0, 10):
        param = {'start': 25 * i}
        result = requests.get(link, params=param, headers=headers, cookies=cookies)
        soup = BeautifulSoup(result.text, 'lxml')
        movie_list_page = soup.find_all('div', class_='hd')
        for movie in movie_list_page:
            movie_name = movie.a.text.replace('\n', '').replace('\xa0', ' ').split('/')
            movie_names.append(movie_name[0].strip())
            origin_names.append(movie_name[1].strip())
    return movie_names, origin_names


# movies, origin = get_movies()
# print('共%d部电影，大陆译名如下：%s\n外文名如下：%s\n' % (len(movies), movies, origin))

# 动态抓取天猫评论
import json

cookies = {}
cookie = 'x=__ll%3D-1%26_ato%3D0; t=3e732669d1d08c92b25f140231af20a0; _tb_token_=79b0099cf0738; cookie2=1774070744ad018fdc9d44ebd8ce89ac; cna=gJ8rEwZ//w8CAcrHBiyg3hzP; uc1=cookie14=UoTePlIOFotWUQ%3D%3D&lng=zh_CN&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&existShop=false&cookie21=VT5L2FSpccLuJBreK%2BBd&tag=8&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&pas=0; uc3=nk2=pKj9wYlYgDV8YO0T&id2=UoYdWtDhRfa8GA%3D%3D&vt3=F8dBz4W93Zt5Saw4q14%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; tracknick=%5Cu5DE7%5Cu514B%5Cu529B%5Cu7096%5Cu732A%5Cu8E44; _l_g_=Ug%3D%3D; unb=1737041396; lgc=%5Cu5DE7%5Cu514B%5Cu529B%5Cu7096%5Cu732A%5Cu8E44; cookie1=BxStrI%2BQLQyUTBkUag1DM460%2Bzru7YaYAIFNU0PpDYY%3D; login=true; cookie17=UoYdWtDhRfa8GA%3D%3D; _nk_=%5Cu5DE7%5Cu514B%5Cu529B%5Cu7096%5Cu732A%5Cu8E44; sg=%E8%B9%846e; csg=5d80142e; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; swfstore=95507; whl=-1%260%260%260; pnm_cku822=098%23E1hvaQvUvbpvUvCkvvvvvjiPPFs9ljtUnLSwzjrCPmPW1jt8RszZ0jrbRLzZgjY8RphvCvvvvvvPvpvhvv2MMQhCvvOvCvvvphmtvpvIvvvv2hCvjROvvURFphvWCQvv96CvpC29vvm2phCvhUvvvURFphvp9UyCvvOUvvhCayRivpvUvvmvWxi8E4yEvpCWmjzZvvwTQPL6Yb8raokQiNoxdXQaU%2BFpznQaV5HClb2XSfpAOH2%2BFOcn%2B3C1BRFEDaVTRogRD7zUaXgOfvc61WFve1i%2BVd0DyOvO54wCvvpvvUmm; isg=BB0dLjpjGxqhjf81g66fn3VLLPDd_VegsZF8jt_iXXSjlj3Ip4phXOuPxIqQVmlE'
cookie_dic = cookie.split(';')
for each in cookie_dic:
    name, value = each.split('=', 1)
    cookies[name] = value
# for i in range(0,20):
#     html = requests.get(
#         'https://rate.tmall.com/list_detail_rate.htm?itemId=562948989464&spuId=915190326&sellerId=1114511827&order=3&currentPage=%d&append=0&content=1&tagId=&posi=&picture=&isg=BE1Nk8bSK4oSa4-lM76vL6U7XGAN7YfQ4aEsPo_SxORThmw4V3hszIzU9BrgRpm0&needFold=0&_ksTS=1520855397978_1378&callback=jsonp1379'%i,
#         headers=headers,cookies=cookies)
#     result = json.loads(html.text.replace('jsonp1379(', '').rstrip(')').strip())
#     for comment in result['rateDetail']['rateList']:
#         print(
#             '买家昵称：%s\t商品类型：%s\t买家评论：%s,' % (comment['displayUserNick'], comment['auctionSku'], comment['rateContent']))
#         print('\n')

# 使用selenium

from selenium import webdriver

# chrome_opt = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_opt.add_experimental_option('prefs', prefs)
# chrome_opt.add_argument('start-maximized')
# chrome_opt.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=chrome_opt)
# # driver.get('https://www.baidu.com')
# # content = driver.find_element_by_css_selector('div.qrcode-text')
# # content2 = driver.find_elements_by_tag_name('a')
# # print(content.text)
# # for each in content2:
# #     print(each.text)
# driver.get('http://www.santostang.com/2017/03/02/hello-world/')
# # time.sleep(10)
# print('开始读取评论：')
# driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
#
# for i in range(0, 10):
#     time.sleep(1)
#     comments = driver.find_elements_by_css_selector('div.reply-content')
#     for comment in comments:
#         print(comment.text)
#     try:
#         more_btn = driver.find_element_by_css_selector('button.more-btn')
#         more_btn.click()
#     except Exception:
#         print('\n--------------已读取所有评论---------------')
#         break
#
# driver.quit()

# 爬取链家沈阳房源信息：名称，价格，房屋类型，面积，地理位置
# link = 'https://sy.fang.lianjia.com/loupan/rs'
# chrome_opt = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_opt.add_experimental_option('prefs', prefs)
# chrome_opt.add_argument('start-maximized')
# chrome_opt.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=chrome_opt)
# driver.get(link)
# total_page = driver.find_element_by_css_selector("div.page-box>a:nth-last-child(2)")  # 总页数
# print(total_page.text)
# for i in range(1, int(total_page.text) + 1):
#     templink = link + '/pg%d' % i
#     print(templink)
#     driver.get(templink)
#     houses_info = driver.find_elements_by_css_selector("div.resblock-desc-wrapper")
#     print(i)
#     for house in houses_info:
#         name = house.find_element_by_tag_name("a")
#         position = house.find_element_by_css_selector("div.resblock-location").text
#         price = house.find_element_by_css_selector("div.main-price").text
#         house_type = house.find_element_by_css_selector("a.resblock-room").text.replace(" ", "")
#         area = house.find_element_by_css_selector("div.resblock-area").text.replace(" ", "")
#         print("楼盘名称：%-30s楼盘位置：%-30s\t价格：%-30s\t户型：%-30s\t面积：%-30s\t" % (
#         name.text, position.replace(" ", ""), price.replace(" ", ""), house_type, area))
# driver.quit()

# 正则表达式
import re
# line = 'fat cat are smarter than dogs,is it right?'
# m=re.match(r'(.*) are (.*?) dogs',line)
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.groups())

# xpath
# link = "http://www.santostang.com"
# headers= {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
# r = requests.get(link,headers=headers)
# soup = BeautifulSoup(r.text,'lxml')
# # print(soup.get_text())
# # print(soup.prettify())
# #
# first_title = soup.find('h1',class_='post-title').a.text.strip()
# print("第一篇文章的标题是：",first_title)
# title_list = soup.find_all("h1",class_="post-title")
# for i in range(len(title_list)):
#     title = title_list[i].a.text.strip()
#     print("第%d篇文章的标题是：%s:"%(i+1,title))
# # print(x.name for x in soup.find_all(re.compile("^h")))
# # for x in soup.find_all(re.compile("^h")):
# #     print(x.name)
# from lxml import etree
# html = etree.HTML(r.text)
# text = html.xpath("//*[@id='main']/div/div[1]/article[3]/header/h1/a/@href")
# print(text)

# 使用BeautifulSoup和xpath爬取我爱我家北京朝阳租房信息
from lxml import etree
link = "https://bj.5i5j.com/zufang/chaoyangqu/"
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
r=requests.get(link,headers=headers)
# html = etree.HTML(r.text)
# total_page = html.xpath("/html/body/div[4]/div[1]/div[3]/div[2]/a[2]/text()")
# print(total_page[0])
# for i in range(1,int(total_page[0])+1):
#     print("-------------第%d页数据--------------"%i,end='\n')
#     r = requests.get(link+"/n%d"%i, headers=headers)
#     html = etree.HTML(r.text)
#     houses_info = html.xpath("/html/body/div[4]/div[1]/div[2]/ul/li")
#     for house in houses_info:
#         name=house.xpath("./div[2]/h3/a/text()")
#         info = house.xpath("./div[2]/div[1]/p[1]/text()")
#         positon = house.xpath("./div[2]/div[1]/p[2]//text()")
#         price = house.xpath("/html/body/div[4]/div[1]/div[2]/ul/li[2]/div[2]/div[1]/div/p[1]//text()")
#         print("房屋名称：%-20s房屋信息：%-20s房屋位置：%-20s房屋价格：%-20s"%(name,info[0].replace(" ",""),positon,price))
html = BeautifulSoup(r.text,"lxml")
total_page = html.find("div",class_="pageSty rf").contents[1]
for i in range(1,int(total_page.text)+1):
    r = requests.get(link+"/n%d"%i, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    houses_info=soup.select("body > div.pListBox.mar.main > div.lfBox.lf > div.list-con-box > ul > li")
    for house in houses_info:
        name=house.select("h3 > a")[0].text
        info = house.select("div.listX > p")[0].text.strip()
        position = house.select("div.listX > p")[1].text.strip()
        price = house.select("div.jia > p.redC")[0].text.strip()
        print("房屋名称：%-20s房屋信息：%-50s房屋位置：%-50s房屋价格：%-50s" % (name, info.replace(" ",""), position, price))
        pass
    pass
print(total_page.text)