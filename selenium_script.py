from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse
import time

def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")  # 디버깅 포트 추가

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(30)  # 페이지 로딩 제한 시간 설정
    return driver

def cafe24_register(driver, id, pw, name, phone, mail):
    target_url = "https://suraktantan.cafe24.com/member/agreement.html"
    
    try:
        driver.get(target_url)
        
        wait = WebDriverWait(driver, 10)
        
        # 약관 동의 체크박스 클릭
        check_element = wait.until(EC.element_to_be_clickable((By.ID, "sAgreeAllChecked")))
        driver.execute_script("arguments[0].click();", check_element)

        # 동의 후 다음 단계 진행
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ec-base-button.gBottom button")))
        next_button.click()
        
        # ID 입력
        id_field = wait.until(EC.presence_of_element_located((By.ID, "member_id")))
        id_field.clear()
        id_field.send_keys(id)

        # 비밀번호 입력
        pw_field = driver.find_element(By.ID, "passwd")
        pw_field.clear()
        pw_field.send_keys(pw)

        pw_confirm_field = driver.find_element(By.ID, "user_passwd_confirm")
        pw_confirm_field.clear()
        pw_confirm_field.send_keys(pw)

        # 이름 입력
        name_field = driver.find_element(By.ID, "name")
        name_field.clear()
        name_field.send_keys(name)

        # 전화번호 입력
        phone_number = phone.replace("-", "").replace(" ", "")
        if phone_number.startswith("010") and len(phone_number) == 11:
            driver.find_element(By.ID, "mobile2").send_keys(phone_number[3:7])
            driver.find_element(By.ID, "mobile3").send_keys(phone_number[7:])
        else:
            raise ValueError(f"Invalid phone number format: {phone}")

        # 이메일 입력
        email_field = driver.find_element(By.ID, "email1")
        email_field.clear()
        email_field.send_keys(mail)

        # 가입 버튼 클릭
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ec-base-button.gBottom a:nth-child(2)")))
        driver.execute_script("arguments[0].click();", submit_button)
        
        time.sleep(3)
    
    except Exception as e:
        print(f"❌ Error during registration: {str(e)}")
        print("📄 Page Source (Partial):", driver.page_source[:1000])  # 페이지 디버깅용 출력

def main():
    parser = argparse.ArgumentParser(description="Run Selenium script with arguments")
    parser.add_argument("--id", required=True, help="ID")
    parser.add_argument("--pw", required=True, help="Password")
    parser.add_argument("--name", required=True, help="Name")
    parser.add_argument("--phone", required=True, help="Phone Number")
    parser.add_argument("--mail", required=True, help="Email")
    args = parser.parse_args()

    driver = create_driver()
    try:
        cafe24_register(driver, args.id, args.pw, args.name, args.phone, args.mail)
    except Exception as e:
        print(f"❌ Unhandled Error: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
