# _*_ coding:utf-8 _*_\
import requests#导入模块
import obsear
url = 'http://www.ycgwl.com/Mobile/index.aspx' #url统一资源定位符
# def download_img(url):
response = requests.get(url) #发送请求，下载数据
# print response.text #输出网页源码
html = response.text
# # <img id="img" src="//car2.autoimg.cn/cardfs/product/g10/M00/0C/6E/1024x0_1_q87_autohomecar__wKgH4FijtkSAd8ZvAAN9pa735R8368.jpg" onside="1" style="cursor: url(&quot;/images/next.cur&quot;), pointer;">
img_url = obsear.findall(r'<img src="(.*?)"', html)[0] #获取图片url正则表达式
img_url = 'http:'+ img_url
print (img_url)
#     img_response = requests.get(img_url) #下载图片
#     img_data = img_response.content
# print img_data
# 持久化入库，写文件
#     print (img_response.content)
# f = open('C:/Users/tzhangw/Desktop\1.jpg','wb')
# f.write(img_data)
# f.close()
#     img_file_name = img_url.split('/')[-1]
#     with open('C:/Users/tzhangw/Desktop/spider/'+img_file_name ,'wb') as f:
#         f.write(img_data)
# # var nexturl = '/photo/31525/1/4087890.html'
#     nexturl = re.findall(r"var nexturl = '(.*?)'",html)[0]
#     print nexturl
#     if nexturl:
#         nexturl = 'https://car.autohome.com.cn' + nexturl
#         download_img(nexturl)
# download_img(url)