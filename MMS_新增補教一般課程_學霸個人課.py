import undetected_chromedriver as uc
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

URL = uc.Chrome()
wait = ui.WebDriverWait(URL,10)

URL.maximize_window()
URL.get("https://oneclub.backstage-uat.oneclass.com.tw/")

#----登入MMS帳密----
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[1]/div/input"))
account = URL.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[1]/div/input")
account.send_keys("ONE50397")#帳號

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[2]/div/input"))
password = URL.find_element("xpath","/html/body/div/div[2]/div[2]/div[2]/div[2]/div/input")
password.send_keys("juan7890")#密碼
password.send_keys(Keys.ENTER)#打完帳密按下Enter

#----接換List----
time.sleep(5)

wait.until(lambda driver:driver.find_element("xpath","//div[@id='root']/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/ul/div/div[2]"))
member_manage = URL.find_element("xpath","//div[@id='root']/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/ul/div/div[2]")
member_manage.click()#會員管理

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","//div[@id='root']/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/ul/div[3]/div[2]"))
Tutorial_Center_Management = URL.find_element("xpath","//div[@id='root']/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/ul/div[3]/div[2]")
Tutorial_Center_Management.click()#補教課程管理

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","//div[@id='root']/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/ul/div[4]/div/div/div/a/div[2]"))
General_Curriculum_Management = URL.find_element("xpath","//div[@id='root']/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/ul/div[4]/div/div/div/a/div[2]")
General_Curriculum_Management.click()#一般課程管理

#----新增學霸個人課----
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[2]/main/div[2]/div[1]/div/div[2]/button"))
add_course = URL.find_element("xpath","/html/body/div[1]/div[2]/main/div[2]/div[1]/div/div[2]/button")
add_course.click()#新增課程

URL.switch_to.window(URL.window_handles[1])#切換到另一個分頁

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div[2]/div[2]/div/div/input"))
input_course_type = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div[2]/div[2]/div/div/input")
input_course_type.click()#選擇課程類型
for i in range(2):
    input_course_type.send_keys(Keys.DOWN)
input_course_type.send_keys(Keys.ENTER)

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[2]/div[2]/div/div/div/input"))
input_organization = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[2]/div[2]/div/div/div/input")
input_organization.send_keys("學barUAT")#輸入機構名稱
time.sleep(5)
input_organization.send_keys(Keys.DOWN)
input_organization.send_keys(Keys.ENTER)


URL.execute_script("window.scrollBy(0,500)")

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[3]/div[2]/div/div/div/input"))
choose_classroom = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[3]/div[2]/div/div/div/input")
choose_classroom.click()#選擇班級
choose_classroom.send_keys(Keys.DELETE)
choose_classroom.send_keys("學兒UAT")
choose_classroom.send_keys(Keys.DOWN)
choose_classroom.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[2]/div[2]/div/input"))
course_date = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[2]/div[2]/div/input")
course_date.send_keys("20230928")#輸入課程日期

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[3]/div[2]/div/input"))
start_time = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[3]/div[2]/div/input")
start_time.send_keys("1900")#輸入開始時間
4
URL.execute_script("window.scrollBy(0,500)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[2]/div[2]/div[2]/div/div/input"))
course_lable = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[2]/div[2]/div[2]/div/div/input")
course_lable.click()#選擇課程標籤
course_lable.send_keys(Keys.DOWN)
course_lable.send_keys(Keys.ENTER)

ActionChains(URL).move_by_offset(400,400).click().perform()#點選空白區

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[3]/div[2]/div[2]/div/div/input"))
choose_teacher = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[3]/div[2]/div[2]/div/div/input")
choose_teacher.click()#選擇老師
choose_teacher.send_keys("黃一一")
time.sleep(2)
choose_teacher.send_keys(Keys.DOWN)
choose_teacher.send_keys(Keys.ENTER)

time.sleep(2)
URL.execute_script("window.scrollBy(0,500)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[2]/div/input"))
input_course_name = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[2]/div/input")
input_course_name.click()
input_course_name.send_keys("test")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[3]/div[2]/div/textarea[1]"))
input_teach_remind = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[3]/div[2]/div/textarea[1]")
input_teach_remind.send_keys("學生不乖")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div/div[2]/button[3]"))
post = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div/div[2]/button[3]")
post.click()#發布