from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver


def cafe24_register(driver, id, pw, name, phone, mail):
    target_url = "https://suraktantan.cafe24.com/member/agreement.html"
    driver.get(target_url)
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, ".agreeAll .ec-base-chk input").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "div.ec-base-button.gBottom button").click()
    time.sleep(1)

    driver.find_element(By.ID, "member_id").send_keys(id)
    time.sleep(0.5)
    driver.find_element(By.ID, "passwd").send_keys(pw)
    time.sleep(0.5)
    driver.find_element(By.ID, "user_passwd_confirm").send_keys(pw)
    time.sleep(0.5)
    driver.find_element(By.ID, "name").send_keys(name)
    time.sleep(0.5)
    
    phone_parts = phone.split('-')
    driver.find_element(By.ID, "mobile2").send_keys(phone_parts[1])
    time.sleep(0.5)
    driver.find_element(By.ID, "mobile3").send_keys(phone_parts[2])
    time.sleep(0.5)

    driver.find_element(By.ID, "email1").send_keys(mail)
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, "div.ec-base-button.gBottom a:nth-child(2)").click()
    time.sleep(2)

def swing2app_register(driver, id, pw, name):
    swing_url = "https://www.swing2app.co.kr/view/member_list"
    driver.get(swing_url)
    time.sleep(3)

    driver.find_element(By.XPATH, "//div[@target='#subAdminLogin']").click()
    time.sleep(1)

    driver.find_element(By.ID, "appIdSingInIdInput").send_keys('bookboostth')
    time.sleep(0.5)
    driver.find_element(By.ID, "subAdminSingInIdInput").send_keys('admin3')
    time.sleep(0.5)
    driver.find_element(By.ID, "subAdminSingInPassWordInput").send_keys('1234')
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[@class='fxt-btn-fill sub-admin-login-btn']").click()
    time.sleep(8)

    driver.find_element(By.XPATH, "//div[@class='btn btn-default app-user-create-popup-open-btn']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@class='form-control user-id']").send_keys(id)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//input[@class='form-control user-pw']").send_keys(pw)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//input[@class='form-control user-name']").send_keys(name)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[@class='btn btn-success app-user-save-btn']").click()
    time.sleep(3)

def main():
    driver = create_driver()
    try:
        test_id = "testman6"
        test_pw = "tman1004tman!!"
        test_name = "테스트맨6"
        test_phone = "010-1234-5678"
        test_mail = "testman5@test.com"

        cafe24_register(driver, test_id, test_pw, test_name, test_phone, test_mail)
        swing2app_register(driver, test_id, test_pw, test_name)

        with open("output.txt", "w") as f:
            f.write("✅ Registration successful!")

    except Exception as e:
        with open("output.txt", "w") as f:
            f.write(f"❌ Error: {str(e)}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
