from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from csv import writer


def ScrollDown():
    
    last_height = driver.execute_script("return document.body.scrollHeight")


    while True:
    

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        sleep(0.55)
    
        new_height = driver.execute_script("return document.body.scrollHeight")
    
        if new_height == last_height:
    
            break
    
        last_height = new_height


url="https://www.bouncim.com/login"
url_sitemap="https://www.bouncim.com/sitemap.xml"


s=Service("C:/Users/VICTUS/Downloads/chromedriver_win32/chromedriver.exe")
options =  webdriver.ChromeOptions()
options.add_argument("--enable-javascript")
options.add_argument("--headless");
driver= webdriver.Chrome(service=s,options=options)
driver.get(url)
driver.maximize_window()

username="******"
password="******"

password = driver.find_element(By.ID,"signup_password").send_keys(password)
username = driver.find_element(By.ID,"signup_email").send_keys(username)


sleep(1)


button = driver.find_element(By.CSS_SELECTOR,"#signup > div.ant-row.ant-form-item > div > div > div > button").click()

sleep(2)

url_list=[]
driver.get(url_sitemap)
all_spans = driver.find_elements(By.CSS_SELECTOR,".folder > div.opened > div:nth-child(1) > span:nth-child(2)")
for allspan in all_spans:
    if(allspan.text.startswith("https://bouncim.com/teachers/show/")):
        url_list = url_list + [allspan.text]
        
with open('students_final2.csv','w',newline='') as f:
    thewriter = writer(f)
    header =["Username","Lesson Name","Teacher Name","Text","Point"]
    thewriter.writerow(header)


for url in url_list:
    driver.get(str(url))
     
 
    ScrollDown()
            
    try:
     
        text= WebDriverWait(driver, 0.55).until(EC.presence_of_element_located((By.ID,"__next")))
        negative_comments = text.find_elements(By.CSS_SELECTOR,".styles-sc-wupr5u-1.ekSSki")
        positive_comments = text.find_elements(By.CSS_SELECTOR,".styles-sc-wupr5u-1.dFUEec")
        neutral_comments  = text.find_elements(By.CSS_SELECTOR,".styles-sc-wupr5u-1.bbhscl")
   
        with open('students_final2.csv','a',encoding='utf8',newline='') as f:
            thewriter = writer(f)
          
            for comment in negative_comments:
               
                tags=comment.find_elements(By.TAG_NAME,"a")
                username=tags[0].text
                lesson_name=tags[1].text
                teacher_name=tags[2].text
                text = comment.find_element(By.CSS_SELECTOR,".styles__Body-sc-wupr5u-4.hqkPzk").text
                text = text.replace('\n', ' ').replace('\r', '')
                point=0
                         
                row = [username,lesson_name,teacher_name,text,point]
                thewriter.writerow(row)
                    
            
            for comment in positive_comments:
                
                tags=comment.find_elements(By.TAG_NAME,"a")
                username=tags[0].text
                lesson_name=tags[1].text
                teacher_name=tags[2].text
                text = comment.find_element(By.CSS_SELECTOR,".styles__Body-sc-wupr5u-4.hqkPzk").text
                text = text.replace('\n', ' ').replace('\r', '')
                point=1
                
                row = [username,lesson_name,teacher_name,text,point]
                thewriter.writerow(row)
            
            for comment in neutral_comments:
                
                tags=comment.find_elements(By.TAG_NAME,"a")
                username=tags[0].text            
                lesson_name=tags[1].text            
                teacher_name=tags[2].text            
                text = comment.find_element(By.CSS_SELECTOR,".styles__Body-sc-wupr5u-4.hqkPzk").text
                text = text.replace('\n', ' ').replace('\r', '')
                point=0.5
                
                row = [username,lesson_name,teacher_name,text,point]
                thewriter.writerow(row)
        
        
    except TimeoutException:
        print("Loading took too much time!")
