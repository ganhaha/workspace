from weibo import APIClient
import requests
import time

'''
url_get_token = 'https://api.weibo.com/oauth2/access_token'

#构建POST参数
playload = {
            'client_id':'1642434127',
            'client_secret':'ae7024f7b235004ff36710eb14196d5b',
            'grant_type':'authorization_code',
            'code':'b93849053d8d8acaac1d64a892369fb4',
            'redirect_uri':'https://api.weibo.com/oauth2/authorize',
}
#POST请求
r = requests.post(url_get_token,data=playload)
print(r.text)
'''
#输出响应信息
'''
app_key='1642434127'
app_secret='ae7024f7b235004ff36710eb14196d5b'
callback_url='https://api.weibo.com/oauth2/authorize'
client=APIClient(app_key=app_key,app_secret=app_secret,redirect_uri=callback_url)
url=client.get_authorize_url()
'''

weibo_post_url = 'https://upload.api.weibo.com/2/statuses/upload.json'
status_content = open('G:\weibo\weibo_pic\\2\content.txt', 'r')#open content

gif_num=1
for status_content_line in status_content:#chenck lines in content
        print(status_content_line)

        load = {
                'access_token': '2.00P_4PFGBJUJnB9ac935ac650Y5alC',
                'status': status_content_line,
                }#weibo API

        files = {'pic': open('G:\weibo\weibo_pic\\2\\' + str(gif_num) + '.gif', 'rb')}
        r = requests.post(weibo_post_url, data=load, files=files)
        gif_num = gif_num + 1
        time.sleep(30)
        print(r.text)
open('G:\weibo\weibo_pic\\2\content.txt', 'r').close() #close content







