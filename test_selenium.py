# Whatsapp changes the class name - used a class generator?
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=/Users/vuhoangquan/Library/Application\ Support/Google/Chrome/Default");

# driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver = webdriver.Chrome(executable_path='/Users/vuhoangquan/code/chromedriver', options=options)
driver.get('http://www.google.com/');

time.sleep(3) # Let the user actually see something!

search_box = driver.find_element_by_name('q')
search_box.send_keys('web.whatsapp')
search_box.submit()

titles_element = driver.find_elements_by_xpath("//h3[@class='LC20lb DKV0Md']")
titles_element[0].click()

time.sleep(10) # sleep for login with QR code -- must do manually

try:
    # third_result=driver.find_element_by_class_name("_1Ek-U")
    third_result=driver.find_element_by_class_name("_28-cz")
    third_result.click()
    # third_result.send_keys('group')

    # try:
    #     result1=driver.find_element_by_class_name("_2MwRD")
    #     # result1.click()
    #     result1.send_keys('test')
    #     time.sleep(1)
    # except ElementNotInteractableException:
    #     print('cannot send key to this1 field')

    # try:
    #     result2=driver.find_element_by_class_name("OTBsx")
    #     result2.click()
    #     result2.send_keys('test')
    #     time.sleep(1)
    # except ElementNotInteractableException:
    #     print('cannot send key to this2 field')
    
    # click search button
    try:
        # result3=driver.find_element_by_class_name("_3xzAH")
        result3=driver.find_elements_by_class_name("iy1jQ")
        result3.click()
        # result3.send_keys('test')
        time.sleep(1)
    except:
        print('cannot send key to this3 field')
    
    # try:
    #     result4=driver.find_element_by_class_name("_3H1Lp")
    #     result4.click()
    #     result4.send_keys('test')
    #     time.sleep(1)
    # except:
    #     print('cannot send key to this4 field')

    # try:
    #     result5=driver.find_element_by_class_name("_1rPZq _1-jFy")
    #     result5.click()
    #     result5.send_keys('test')
    #     time.sleep(1)
    # except:
    #     print('cannot send key to this5 field')

    # try:
    #     result6=driver.find_element_by_class_name("_1rPZq _2w7RB")
    #     result6.click()
    #     result6.send_keys('test')
    #     time.sleep(1)
    # except:
    #     print('cannot send key to this6 field')

    # try:
    #     result7=driver.find_element_by_class_name("_2MwRD")
    #     result7.click()
    #     # result7.send_keys('test')
    #     time.sleep(1)
    # except:
    #     print('cannot send key to this7 field')
    
    # try:
    #     result8=driver.find_element_by_class_name("_2_1wd copyable-text selectable-text")
    #     result8.click()
    #     result8.send_keys('test')
    #     time.sleep(1)
    # except:
    #     print('cannot send key to this8 field')

    # click filter key
    try:
        # result9=driver.find_elements_by_class_name("_3H1Lp")
        result9=driver.find_elements_by_class_name("_3mVPR")
        result9=driver.find_elements_by_class_name("_26c7g")

        result9[1].click()
        # result9.send_keys('test')
        time.sleep(1)
    except:
        print('cannot send key to this9 field')

    # try:
    #     result10=driver.find_element_by_class_name("_3el0F")
    #     result10.click()
    #     # result10.send_keys('test')
    #     time.sleep(1)
    # except:
    #     print('cannot send key to this10 field')        

    # this part get group chats name
    # try:
    #     result01=driver.find_elements_by_class_name("_35k-1")
    #     result01=driver.find_elements_by_class_name("_ccCW")

    #     for each_result in result01:
    #         try:
    #             driver.execute_script("window.scrollTo(0, 1080)") #scroll down 1 screen 
    #             time.sleep(1)
    #             driver.execute_script("window.scrollTo(0, 0)") #scroll top
    #             print(' group name: '+each_result.text) # print groups name
    #             each_result.click()
    #             time.sleep(1)
    #         except Exception as e:
    #             print(' <+> buged '+e+'\n')
    #     # print(result01[0].text)
    #     # result9.send_keys('test')
    #     time.sleep(1)
    # except Exception as e:
    #     print('cannot send key to this 01 field '+e)

except NoSuchElementException:
    print('cant find the element in page')

# time.sleep(10)

# first_result=driver.find_element_by_class_name("_2_1wd copyable-text selectable-text"); # no such element: Unable to locate element ->use xpath
# second_result=driver.find_element_by_class_name("yuRUbf");
# first_result.click()
# first_result.send_keys('group')
# second_result.click()

time.sleep(600) # see screen
# --> start query for the chats !
# .get click on chat 
# .click on ... button
# .click exit group but... (check for people in group first)



driver.quit()