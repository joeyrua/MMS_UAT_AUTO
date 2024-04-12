import undetected_chromedriver as uc
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
URL = uc.Chrome()
wait = ui.WebDriverWait(URL,10)
action = ActionChains(URL)
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

time.sleep(5)


#----新增會員----
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div/button[2]"))
add_member = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[1]/div/button[2]")
add_member.click()#新增會員

time.sleep(3)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div/div/label[2]/span[1]/input"))
radiobutton2 = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div/div/label[2]/span[1]/input")
radiobutton2.click()#選擇資料來源:手動輸入

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[3]/div[2]/div/div/div/input"))
input_onclub_id = URL.find_element("xpath","/html/body/div/div[2]/main/div[3]/div[2]/div/div/div/input")
input_onclub_id.send_keys("pink005")#輸入oneclub_id:pink005

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[3]/div[3]/div/div/div/input"))
input_name = URL.find_element("xpath","/html/body/div/div[2]/main/div[3]/div[3]/div/div/div/input")
input_name.send_keys("✖林山立")#輸入姓名

URL.execute_script("window.scrollBy(0,500)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[3]/div[6]/div/div/div/div/input"))
press_choose_Counsellor = URL.find_element("xpath","/html/body/div/div[2]/main/div[3]/div[6]/div/div/div/div/input")
press_choose_Counsellor.send_keys("阮小昱")#輸入輔導老師
press_choose_Counsellor.send_keys(Keys.DOWN)
press_choose_Counsellor.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[2]/div/div[2]/div/input"))
input_phone_number = URL.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[2]/div/div[2]/div/input")
input_phone_number.send_keys("0933456789")#輸入電話號碼:0933456789

URL.execute_script("window.scrollBy(0,500)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[3]/div/div/div/input"))
input_email = URL.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[3]/div/div/div/input")
input_email.send_keys("juan123@gmail.com")#輸入電子信箱:juan123@gmail.com

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[4]/div/div/div[2]/div[1]/div/div/input"))
press_choose_city = URL.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[4]/div/div/div[2]/div[1]/div/div/input")
press_choose_city.click()#按下選擇縣市

for i in range(2):
    press_choose_city.send_keys(Keys.DOWN)
press_choose_city.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[4]/div/div/div[2]/div[2]/div/div/input"))
input_district = URL.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[4]/div/div/div[2]/div[2]/div/div/input")
input_district.click()#按下選擇區域

for i in range(2):
    input_district.send_keys(Keys.DOWN)
input_district.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[4]/div/div/div[3]/div/input"))
input_address = URL.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[4]/div/div/div[3]/div/input")
input_address.send_keys("aaaa")#輸入地址:aaaa

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[5]/div/div/label/span[1]/input"))
same_connection_address = URL.find_element("xpath","/html/body/div/div[2]/main/div[4]/div[5]/div/div/label/span[1]/input")
same_connection_address.click()#相同聯絡地址

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[6]/button[2]"))
save_button = URL.find_element("xpath","/html/body/div/div[2]/main/div[6]/button[2]")
save_button.click()#儲存

wait.until(lambda driver:driver.find_element("xpath","/html/body/div[2]/div[3]/div/div/div[2]/button"))
finish_button = URL.find_element("xpath","/html/body/div[2]/div[3]/div/div/div[2]/button")
finish_button.click()#按下完成


#----建立學生----
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/table/tbody/tr[1]/td[9]/button"))
edit_student = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/table/tbody/tr[1]/td[9]/button")
edit_student.click()#點擊編輯

URL.switch_to.window(URL.window_handles[1])#切換到另一個分頁

time.sleep(5)
URL.execute_script("window.scrollBy(0,1000)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[1]/div/button"))
add_member = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[1]/div/button")
add_member.click()#新增成員

time.sleep(2)
wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[2]/div/div/input"))
input_student1 = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[2]/div[2]/div/div/input")
input_student1.send_keys("✖黃清山")#輸入學生姓名

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[2]/div/div/div/input"))
school = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[3]/div[2]/div/div/div/input")
school.click()#選擇學制

for i in range(2):
    school.send_keys(Keys.DOWN)#選擇小學(ID=2);幼稚園ID=1,國中ID=3,高中ID=4
school.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[2]/div/div/div/input"))
grade = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[4]/div[2]/div/div/div/input")
grade.click()#選擇年級

for i in range(3):
    grade.send_keys(Keys.DOWN)#選擇年級:3年級(ID=3);其他年級一此類推
grade.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[1]/div/div/input"))
school_city = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[1]/div/div/input")
school_city.click()#選擇學校縣市

for i in range(3):
    school_city.send_keys(Keys.DOWN)#選擇學校縣市:新北市(ID:3)
school_city.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[2]/div/div/input"))
school_dis = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[2]/div/div/input")
school_dis.click()#選擇學校區域

for i in range(3):
    school_dis.send_keys(Keys.DOWN)#選擇學校區域:板橋區(ID:3)
school_dis.send_keys(Keys.ENTER)

URL.execute_script("window.scrollBy(0,500)")

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[3]/div/div/input"))
school_name = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[5]/div[2]/div[3]/div/div/input")
school_name.click()#選擇學校名稱

for i in range (2):
    school_name.send_keys(Keys.DOWN)#學校名稱:市立信義國小(ID:2)
school_name.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div[2]/div[1]/div/div/input"))
send_address_city = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div[2]/div[1]/div/div/input")
send_address_city.click()#寄送縣市

for i in range(3):
    send_address_city.send_keys(Keys.DOWN)#寄送縣市:新北市(ID:3)
send_address_city.send_keys(Keys.ENTER)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div[2]/div[2]/div/div/input"))
send_address_dis = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div[2]/div[2]/div/div/input")
send_address_dis.click()#寄送區域

for i in range(3):
    send_address_dis.send_keys(Keys.DOWN)
send_address_dis.send_keys(Keys.ENTER)#寄送區域:板橋區(ID:3)

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div[2]/div[3]/div/input"))
send_address = URL.find_element("xpath","/html/body/div/div[2]/main/div[2]/div[6]/div[2]/div[3]/div/input")
send_address.send_keys("aaaa")#輸入地址:aaaa

wait.until(lambda driver:driver.find_element("xpath","/html/body/div/div[2]/main/div[5]/button[2]"))
add_button = URL.find_element("xpath","/html/body/div/div[2]/main/div[5]/button[2]")
add_button.click()









