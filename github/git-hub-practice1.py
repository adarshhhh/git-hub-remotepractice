selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\\Users\Archi\PycharmProject\chrome driver\chromedriver")
driver = webdriver.Firefox(executable_path="C:\\Users\Archi\PycharmProject\chrome driver\geckodriver")
driver = webdriver.Ie(executable_path="C:\\Users\Archi\PycharmProject\chrome driver\IEDriverServer")

driver.get("https://www.amazon.com/")

print(driver.title)        # to capture title of the page
print(driver.current_url)  # to capture current url of the page
print(driver.page_source)  # HTML code for the page

driver.find_element_by_xpath("//*[@id='nav-xshop']/a[2]").click()
time.sleep(5)

#driver.close()             #curruntly focussed browser(parent window will close)
#driver.quit()               #closes all the browser