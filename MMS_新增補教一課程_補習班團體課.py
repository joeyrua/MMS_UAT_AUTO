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

#----接換List----
time.sleep(3)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[1]/div[2]"))
member_manage = URL.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[1]/div[2]")
member_manage.click()#會員管理

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[3]"))
Tutorial_Center_Management = URL.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[3]")
Tutorial_Center_Management.click()#補教課程管理

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[4]"))
General_Curriculum_Management = URL.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[4]")
General_Curriculum_Management.click()#一般課程管理

#----新增補習班學霸個人課----
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div/div[2]/button"))
add_course = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div/div[2]/button")
add_course.click()#新增課程

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[5]/div[3]/div[2]/button[2]"))
choose_onelink_plus_classroom = URL.find_element("xpath","/html/body/div[5]/div[3]/div[2]/button[2]")
choose_onelink_plus_classroom.click()#選擇新增OneLink+教室

URL.switch_to.window(URL.window_handles[1])#切換到另一個分頁

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div[2]/div[2]/div/div/div/button[1]"))
delete_course = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div[2]/div[2]/div/div/div/button[1]")
action.move_to_element(delete_course).click().perform()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div[2]/div[2]/div/div/input"))
input_course_type = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div[2]/div[2]/div/div/input")
input_course_type.send_keys("補習班團體課 (OneLink+)")
input_course_type.send_keys(Keys.DOWN)
input_course_type.send_keys(Keys.ENTER)


wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/div/div/div/input"))
input_organization = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/div/div/div/input")
input_organization.send_keys("UAT測試機構")#輸入機構名稱
input_organization.send_keys(Keys.DOWN)
input_organization.send_keys(Keys.ENTER)


URL.execute_script("window.scrollBy(0,500)")

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[3]/div[2]/div/div/div/input"))
choose_classroom = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[3]/div[2]/div/div/div/input")
choose_classroom.click()#選擇學校
choose_classroom.send_keys("重慶")
choose_classroom.send_keys(Keys.DOWN)
choose_classroom.send_keys(Keys.ENTER)

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[4]/div[2]/div/div/div/input"))
classroom_name = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[4]/div[2]/div/div/div/input")
classroom_name.send_keys("UAT測試課程")
classroom_name.send_keys(Keys.DOWN)
classroom_name.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[3]/div[2]/div[2]/div/input"))
course_date = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[3]/div[2]/div[2]/div/input")
course_date.send_keys("20240430")#輸入課程日期

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[3]/div[3]/div[2]/div/input"))
start_time = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[3]/div[3]/div[2]/div/input")
start_time.send_keys("1900")#輸入開始時間

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[3]/div[4]/div[2]/div/input"))
input_course_time = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[3]/div[4]/div[2]/div/input")
input_course_time.send_keys("25")


URL.execute_script("window.scrollBy(0,500)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[4]/div[2]/div[2]/div[2]/div/div/input"))
course_lable = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[4]/div[2]/div[2]/div[2]/div/div/input")
course_lable.click()#選擇課程標籤
course_lable.send_keys(Keys.DOWN)
course_lable.send_keys(Keys.ENTER)

teacher_lable = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[4]/div[3]/div[1]")
teacher_lable.click()

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[4]/div[3]/div[2]/div[2]/div/div/input"))
choose_teacher = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[4]/div[3]/div[2]/div[2]/div/div/input")
choose_teacher.click()#選擇老師
choose_teacher.send_keys("林雖運")
choose_teacher.send_keys(Keys.DOWN)
choose_teacher.send_keys(Keys.ENTER)

time.sleep(2)
URL.execute_script("window.scrollBy(0,500)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[5]/div[2]/div[2]/div/input"))
input_course_name = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[5]/div[2]/div[2]/div/input")
input_course_name.click()
input_course_name.send_keys("test")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[5]/div[3]/div[2]/div/textarea[1]"))
input_teach_remind = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[5]/div[3]/div[2]/div/textarea[1]")
input_teach_remind.send_keys("學生不乖")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[6]/div/div[2]/button[3]"))
post = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[6]/div/div[2]/button[3]")
post.click()#發布


wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[3]/div/div[2]/div[2]/div/div/input"))
search_input_organization = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[3]/div/div[2]/div[2]/div/div/input")
search_input_organization.send_keys("UAT測試機構")
search_input_organization.send_keys(Keys.ENTER)

time.sleep(5)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[5]/table/tbody/tr/td[8]/div/div/button"))
edit = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[5]/table/tbody/tr/td[8]/div/div/button")
edit.click()


URL.switch_to.window(URL.window_handles[2])#切換到另一個分頁

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[8]/div/div[1]/div"))
cancel_course = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[8]/div/div[1]/div")
cancel_course.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[5]/div[3]/div/div/div[1]/div[4]/div/textarea[1]"))
cancel_reason=URL.find_element("xpath","/html/body/div[5]/div[3]/div/div/div[1]/div[4]/div/textarea[1]")
cancel_reason.send_keys("aaa")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[5]/div[3]/div/div/div[2]/button[2]"))
confirm_cancel = URL.find_element("xpath","/html/body/div[5]/div[3]/div/div/div[2]/button[2]")
confirm_cancel.click()