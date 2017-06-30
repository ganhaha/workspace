import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
import progressbar#进度条模块
import sys
import os

'''
//*[@id="pic-list"]/li[2]/a/img
//*[@id="pic-list"]/li[3]/a/img

'''
def post_weibo():
    weibo_post_url = 'https://upload.api.weibo.com/2/statuses/upload.json'
    status_content=open('G:\weibo\weibo_pic\\2\content.txt', 'r').readline()
    load = {
        'access_token': '2.00P_4PFGBJUJnB9ac935ac650Y5alC',
        'status': status_content,
    }
    open('G:\weibo\weibo_pic\\2\content.txt', 'r').close()

    files = {'pic': open('G:\weibo\weibo_pic\\2\\1.gif', 'rb')}
    r = requests.post(weibo_post_url, data=load, files=files)
    print(r.text)


def save_gif(i,j):

    a=requests.get(driver.find_element_by_class_name('full').get_attribute('href')).content#获取gif图片地址
    with open('G:\weibo\weibo_pic\\' + str(j)+'\\' + str(i+1)+'.gif', 'wb') as pic_gif:
        pic_gif.write(a)

    with open('G:\weibo\weibo_pic\\' + str(j)+'\\' + 'content.txt', 'a') as pic_gif_cotent:
        pic_gif_cotent.write(driver.find_element_by_xpath('//*[@id="pic-intro"]').text + '\n')



url = 'http://tu.duowan.com/m/bxgif'
path = r"D:\Program Files\Python36-32\Scripts\phantomjs.exe"
driver = webdriver.PhantomJS(executable_path=path)
driver.get(url)
driver.maximize_window()


'''
打开第一个大类
'''
for j in range(2,5):
    driver.find_element_by_xpath('//*[@id="pic-list"]/li'+str([j])+'/em/a').click()
    os.mkdir('G:\weibo\weibo_pic\\' + str(j))

#获取第一个大类的第一张图片的地址，并且保存图片,注意一共只有两个窗口，取完gif后关闭。


    window=driver.window_handles
    driver.switch_to.window(window_name=window[1])#切换窗口到打开页面
    driver.maximize_window()
    time.sleep(10)
    '''
    正则表达式提取总页数，并且减掉1，做点击循环
    '''
    patten=re.compile('/(\d+)')
    num=re.search(patten,driver.find_element_by_xpath('//*[@id="seq"]').text)

    for i in range(int(num.group(1))-1):
            save_gif(i,j)
            time.sleep(3)
            ActionChains(driver).click(driver.find_element_by_css_selector('a.next')).perform()#点击下一页
    driver.close()
    driver.switch_to.window(window_name=window[0])
    time.sleep(10)
    pass
    print('第'+str(j)+'页完成!')
    post_weibo()
driver.quit()


