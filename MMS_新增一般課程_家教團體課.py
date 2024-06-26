import undetected_chromedriver as uc
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

URL = uc.Chrome()
wait = ui.WebDriverWait(URL,10)

URL.maximize_window()
URL.get("https://oneclub.backstage-uat.oneclass.com.tw/")

def add_student_all():
    wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/button"))
    add_student = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/button")
    add_student.click()#新增成員

#----登入MMS帳密----
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/div/input"))
account = URL.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/div/input")
account.send_keys("ONE50397")#帳號

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div/input"))
password = URL.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div/input")
password.send_keys("juan7890")#密碼
password.send_keys(Keys.ENTER)#打完帳密按下Enter

#----接換List----
time.sleep(2)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[1]/div[2]"))
member_manage = URL.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[1]/div[2]")
member_manage.click()

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[2]/div[2]"))
Curroclum_Management = URL.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[2]/div[2]")
Curroclum_Management.click()

#----新增團課----
time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[3]/div/div/div/a[4]/div[2]"))
general_course = URL.find_element("xpath","/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[3]/div/div/div/a[4]/div[2]")
general_course.click()#正式課

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div/div[3]/button"))
add_general_course = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div/div[3]/button")
add_general_course.click()#新增課程

#----新增團課----
URL.switch_to.window(URL.window_handles[1])#切換到另一個分頁

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div[2]/div[2]/div/div/input"))
choose_course_type = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[1]/div[2]/div[2]/div/div/input")
for i  in range(2):
    choose_course_type.send_keys(Keys.DOWN)
choose_course_type.send_keys(Keys.ENTER)

URL.execute_script("window.scrollBy(0,500)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[1]/div/div/input"))
input_oneClub = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[1]/div/div/input")
input_oneClub.send_keys("pink002")#輸入第一個學生的OneClub

time.sleep(3)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div/div/div/input"))
input_student = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div/div/div/input")
input_student.click()#選擇第一個學生姓名
input_student.send_keys(Keys.DOWN)
input_student.send_keys(Keys.ENTER)#學生姓名:

add_student_all()#呼叫新增學員

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]/div/div/input"))
input_oneclub_2 = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]/div/div/input")
input_oneclub_2.send_keys("pink003")#輸入第二個學生的OneClub

time.sleep(3)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]/div/div/div/input"))
input_student_2 = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]/div/div/div/input")
input_student_2.click()#選擇第二個學生
input_student_2.send_keys(Keys.DOWN)
input_student_2.send_keys(Keys.ENTER)#學生姓名:

add_student_all()#呼叫新增學員

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[1]/div/div/input"))
input_oneclub_3 = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[1]/div/div/input")
input_oneclub_3.send_keys("pink004")#輸入第三個學生的OneClub

time.sleep(3)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[2]/div/div/div/input"))
input_student_3 = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[2]/div/div/div/input")
input_student_3.click()#選擇第三個學生
input_student_3.send_keys(Keys.DOWN)
input_student_3.send_keys(Keys.ENTER)#學生姓名:

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[2]/div[3]/div[2]/div/div/div/input"))
course_type = URL.find_element("xpath","//html/body/div[1]/div[3]/main/div[2]/div[2]/div[3]/div[2]/div/div/div/input")
course_type.click()#選擇課程類別
course_type.send_keys(Keys.DOWN)
course_type.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[3]/div[3]/div[2]/div/input"))
start_time = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[3]/div[3]/div[2]/div/input")
start_time.send_keys("1900")

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[3]/div[2]/div[2]/div/div/button"))
click_course_date = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[3]/div[2]/div[2]/div/div/button")
click_course_date.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[5]/div[2]/div/div/div/div[2]/div/div[2]/div/div[5]/div[3]/button"))
choose_course_date = URL.find_element("xpath","/html/body/div[5]/div[2]/div/div/div/div[2]/div/div[2]/div/div[5]/div[3]/button")
choose_course_date.click()


URL.execute_script("window.scrollBy(0,600)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[4]/div[2]/div[2]/div[2]/div/div/input"))
choose_course_lable = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[4]/div[2]/div[2]/div[2]/div/div/input")
choose_course_lable.click()#選擇課程標籤
choose_course_lable.send_keys(Keys.DOWN)
choose_course_lable.send_keys(Keys.ENTER)

lable = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[4]/div[2]/div[1]")
lable.click()

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[4]/div[3]/div[2]/div[2]/div/div/input"))
choose_teacher = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[4]/div[3]/div[2]/div[2]/div/div/input")
choose_teacher.click()
choose_teacher.send_keys("林雖運")#輸入老師(如果，要使用已排課老師，請先到教師列表排課)
choose_teacher.send_keys(Keys.DOWN)
choose_teacher.send_keys(Keys.ENTER)

time.sleep(2)
URL.execute_script("window.scrollBy(0,600)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[5]/div[2]/div[2]/div/input"))
input_course_name = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[5]/div[2]/div[2]/div/input")
input_course_name.send_keys("happy_course")#輸入課程名稱

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[5]/div[3]/div[2]/div/textarea[1]"))
teach_remind = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[5]/div[3]/div[2]/div/textarea[1]")
teach_remind.send_keys("aaaa")#輸入授課提醒

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[6]/div/div[2]/button[3]"))
post = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[6]/div/div[2]/button[3]")
post.click()#按下發布

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[3]/div/div[2]/div[2]/div/div/input"))
input_choose_student_name = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[3]/div/div[2]/div[2]/div/div/input")
input_choose_student_name.send_keys("李痕新")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[5]/table/tbody/tr[5]/td[9]/div/div/button"))
edit = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[5]/table/tbody/tr[5]/td[9]/div/div/button")
edit.click()

URL.switch_to.window(URL.window_handles[2])#切換到另一個分頁

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[9]/div/div[1]/div"))
cancel = URL.find_element("xpath","/html/body/div[1]/div[3]/main/div[2]/div[9]/div/div[1]/div")
cancel.click()

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[5]/div[3]/div/div/div[1]/div[4]/div/textarea[1]"))
cancel_reason = URL.find_element("xpath","/html/body/div[5]/div[3]/div/div/div[1]/div[4]/div/textarea[1]")
cancel_reason.send_keys("aaaa")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[5]/div[3]/div/div/div[2]/button[2]"))
confirm_cancel = URL.find_element("xpath","/html/body/div[5]/div[3]/div/div/div[2]/button[2]")
confirm_cancel.click()



