from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
# options.add_argument("--user-data-dir=/Users/vuhoangquan/Library/Application\ Support/Google/Chrome");
# options.add_argument("--user-data-dir=/Users/vuhoangquan/Library/Application\ Support/Google");
# options.add_argument("--user-data-dir=/Users/vuhoangquan/Library/Application\ Support/Google/Drive/");
options.add_argument("--user-data-dir=/Users/vuhoangquan/Library/Application\ Support/Google/Drive/user_default");

# option.add_argument(" - incognito")

browser = webdriver.Chrome(executable_path='/Users/vuhoangquan/code/chromedriver', options=options)
# browser = webdriver.Chrome(executable_path='/Users/vuhoangquan/code/chromedriver')
browser.get('http://www.google.com/')
# ------------------------------------------
# browser.get('https://github.com/TheDancerCodes')
# Wait few seconds for page to load
timeout = 3
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))
except TimeoutException:
    print("Timed out waiting for page to load")
#     # browser.quit()

# # find_elements_by_xpath returns an array of selenium objects.
# titles_element = browser.find_elements_by_xpath("//span[@class='text-bold']")
# # use list comprehension to get the actual repo titles and not the selenium objects.
# titles = [x.text for x in titles_element]
# # print out all the titles.
# print('titles:')
# print(titles, '\n')

# language_element = browser.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")
# # same concept as for list-comprehension above.
# languages = [x.text for x in language_element]
# print("languages:")
# print(languages, '\n')

# for title, language in zip(titles, languages):
#     print("RepoName : Language")
#     print(title + ": " + language, '\n')

# content = browser.find_elements_by_class_name('text-bold')
# eachElement = [x.text for x in content]
# print("query returned:")
# print(eachElement)

# browser.quit()
# ----------------------------------------------
# seach for class elem of a page
# --> need to search for elem in whatsapp
# --> click on some elem in page
# --> get those data and create input(filter) list
# --> get those filter and search for matching chats
# --> quit those chat (will have to click pop up confirmation)
# --> MUST make sure correct chats will be deleted
# (confirm list of chats that will be deleted)

# browser.get('http://web.whatsapp.com')
query1 = browser.find_elements_by_class_name('_2_1wd copyable-text selectable-text')
result1 = [x.text for x in query1]
print("query returned:")
print(result1)

query2 = browser.find_elements_by_class_name('_3xzAH')
result2 = [x.text for x in query2]
print("query returned:")
print(result2)

browser.quit()