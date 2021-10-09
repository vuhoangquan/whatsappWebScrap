# mbbank https doesnot allow web scrapping or sth wrong with the
# client/sever certificate for requests lib to work
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.mbbank.com.vn/ExchangeRate'

try:
    response = requests.get(url) # this should give response 200 
    # page1 = requests.get(ap)
except requests.exceptions.ConnectionError:
    r.status_code = "Connection refused"


# soup = BeautifulSoup(response.text, "html.parser")
# soup.findAll('td') # this find all <a> tag
#----------------------------------------------------------------

# # Parse HTML and save to BeautifulSoup object
# soup = BeautifulSoup(response.text, "html.parser")

# # To download the whole data set, let's do a for loop through all a tags
# line_count = 1 #variable to track what line you are on
# for one_a_tag in soup.findAll('td'):  #'a' tags are for links
#     if line_count >= 36: #code for text files starts at line 36
#         link = one_a_tag['href']
#         download_url = 'http://web.mta.info/developers/'+ link
#         urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
#         time.sleep(1) #pause the code for a sec
#     #add 1 for next line
#     line_count +=1