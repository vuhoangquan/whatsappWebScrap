import requests
import urllib.request
import time
from bs4 import BeautifulSoup
# from BeautifulSoup import BeautifulSoup

url = 'https://web.whatsapp.com/'
# headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
headers = ({'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1'})
# # try:
# #     response = requests.get(url,headers=headers) # this should give response 200 
# #     # page1 = requests.get(ap)
# # except requests.exceptions.ConnectionError:
# #     r.status_code = "Connection refused"

# # response = requests.get(url,headers=headers,verify='C:/Users/vuhoa/Downloads/cert.pem') # this should give response 200 
response = requests.get(url,headers=headers) 
# # response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# soup = BeautifulSoup(response.text, "lxml") 
# # tree = BeautifulSoup(url)
# good_html = soup.prettify()   
# # soup.findAll('td') # this find all <a> tag
# # soup.findAll('_35k-1 _1adfa _3-8er')          
# # print(soup.findAll('_35k-1 _1adfa _3-8er'))
# # print(soup.findAll(id='app')) 

# #----------------------------------------------------------------

# # # Parse HTML and save to BeautifulSoup object

# print(soup.find(class_="_35k-1 _1adfa _3-8er")) 
# data = soup.find_all('div')
# data = soup.find_all('a')
# # print(soup.find_all('span'))
# # print(soup.find_all('span', attrs={"class":"_35k-1 _1adfa _3-8er"}))

# for item in data[:-1]:
#     # print(len(item))
#     print(item.text)
#     # if len(item)!=0:
#         # print('111')
#         # print(item("span")[0].text)
#     #    print('\n')

# # print(data[14].text)
# print(len(data))
# # print(data[1].text)
# # print(data[2].text)
# ---------------------------------------
# class list set
class_list = set()
  
# Page content from Website URL
page = requests.get( url )
  
# parse html content
soup = BeautifulSoup( response.text , 'html.parser')
  
# # get all tags
# tags = {tag.name for tag in soup.find_all()}
  
# # iterate all tags
# for tag in tags:
  
#     # find all element of tag
#     for i in soup.find_all( tag ):
  
#         # if tag has attribute of class
#         if i.has_attr( "class" ):
  
#             if len( i['class'] ) != 0:
#                 class_list.add(" ".join( i['class']))

# for tag in soup.find_all('div'):
#         classid=tag.get('class')
#         if classid==['TbtXF']:
#             print(classid)
#             print(tag)

print(soup.find("h1").text)
print(soup.find("h1").findNext("h1").text)
print(soup.find("h1").findNext("h1").findNext("h1").text)
# print(soup.find("h1").findNext("h1").findNext("h1").findNext("h1").text)