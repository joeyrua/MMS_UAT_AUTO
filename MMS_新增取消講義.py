import undetected_chromedriver as uc
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
URL = uc.Chrome()
wait = ui.WebDriverWait(URL,10)
action = ActionChains(URL)

URL.maximize_window()
URL.get("https://oneclub.backstage-uat.oneclass.com.tw/")


#----登入MMS帳密----
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/div/input"))
account = URL.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/div/input")
account.send_keys("ONE50397")#帳號

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div/input"))
password = URL.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div/input")
password.send_keys("juan7890")#密碼
password.send_keys(Keys.ENTER)#打完帳密按下Enter

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[1]/div[2]"))
member_manage = URL.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[1]/div[2]")
member_manage.click()#會員管理

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[9]"))
shippment_management = URL.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[9]")
shippment_management.click()#出貨管理

time.sleep(5)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[12]/div/div/div/a[1]/div[2]"))

#//*[@id="root"]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[12]/div/div/div/a[1]/div[2]