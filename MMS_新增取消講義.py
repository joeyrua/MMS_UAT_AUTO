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

time.sleep(5)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[10]/div[2]")).click()#出貨管理

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[11]/div/div/div/a[2]/div[2]")).click()#講義出貨管理

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[1]/div/button[3]"))
add_record = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[1]/div/button[3]")
add_record.click()#新增紀錄

URL.switch_to.window(URL.window_handles[1])#切換到另一個分頁

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/form/div[1]/div/div[2]/div[1]/div/div/div/div/input"))
input_OneClub_id = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/form/div[1]/div/div[2]/div[1]/div/div/div/div/input")
input_OneClub_id.send_keys("pink004")#輸入OneClub_id


URL.execute_script("window.scrollBy(0,300)")

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/form/div[2]/div/div[2]/div/label/span[1]"))
check = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/form/div[2]/div/div[2]/div/label/span[1]")
check.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div/button[2]"))
save = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div/button[2]")
save.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[10]/button[2]"))
edit = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[10]/button[2]")
edit.click()

time.sleep(2)
URL.switch_to.window(URL.window_handles[2])#切換到另一個分頁

time.sleep(2)
URL.execute_script("window.scrollBy(0,1200)")

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/form/div[3]/div/div[2]/div[1]/div/div/div"))
choose_handle_state = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/form/div[3]/div/div[2]/div[1]/div/div/div")
choose_handle_state.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[5]/div[3]/ul/li[5]"))
cancel = URL.find_element("xpath","/html/body/div[5]/div[3]/ul/li[5]")
cancel.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div/button[2]"))
save_2 = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div/button[2]")
save_2.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[5]/div[3]/div/div/div[1]/div/div/div/textarea[1]"))
input_reason = URL.find_element("xpath","/html/body/div[5]/div[3]/div/div/div[1]/div/div/div/textarea[1]")
input_reason.send_keys("aaaa")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[5]/div[3]/div/div/div[2]/button[2]"))
confirm_btn = URL.find_element("xpath","/html/body/div[5]/div[3]/div/div/div[2]/button[2]")
confirm_btn.click()