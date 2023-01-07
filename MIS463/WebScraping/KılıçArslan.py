from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from csv import writer
from selenium.webdriver.common.keys import Keys

def ScrollDown():
    
    last_height = driver.execute_script("return document.body.scrollHeight")


    while True:
    

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        sleep(0.55)
    
        new_height = driver.execute_script("return document.body.scrollHeight")
    
        if new_height == last_height:
    
            break
    
        last_height = new_height


url="https://kilicbaran.github.io/boun-course-planner/"

s=Service("C:/Users/VICTUS/Downloads/chromedriver_win32/chromedriver.exe")
options =  webdriver.ChromeOptions()
options.add_argument("--enable-javascript")
options.add_argument("--headless");
driver= webdriver.Chrome(service=s,options=options)
driver.get(url)
driver.maximize_window()
i=0

try:
    text    = WebDriverWait(driver, 0.55).until(EC.presence_of_element_located((By.ID,"app")))
    buttons = WebDriverWait(driver, 0.55).until(EC.presence_of_all_elements_located((By.TAG_NAME,"button")))

    with open('lessons_code.csv','w',newline='') as f:
        thewriter = writer(f)
        header =["Lesson Code","Lesson Name","Teacher Name","Lesson Date","Lesson Hours","Lesson Credit"]
        thewriter.writerow(header)
    

    for button in buttons:
        
        WebDriverWait(driver, 0.55).until(EC.presence_of_element_located((By.ID,"app")))
        WebDriverWait(driver, 0.55).until(EC.presence_of_element_located((By.CLASS_NAME,"mt-4")))  
        buttons2 = WebDriverWait(driver, 0.55).until(EC.presence_of_all_elements_located((By.TAG_NAME,"button")))
        buttons2[i].click()
        i=i+1
        
    
        ScrollDown()
        
        divs = text.find_elements(By.CSS_SELECTOR,"#app > main > div.flex.flex-col.md\:flex-row.grow.md\:overflow-hidden > div.w-full.md\:w-7\/12.p-2.flex.flex-col.grow.h-full > div.mt-4.md\:overflow-y-auto.overflow-x-hidden.flex.flex-col.md\:min-h-0.shrink.shadow.rounded-lg.bg-white.dark\:bg-zinc-800.divide-y.dark\:divide-zinc-500 > div")
        for div in divs:
            with open('lessons_code.csv','a',encoding='utf8',newline='') as f:
                thewriter = writer(f)
                
                lesson_code = div.find_element(By.CSS_SELECTOR,".text-lg.font-medium.mr-3").text
                print(lesson_code)
                lesson_name = div.find_element(By.CSS_SELECTOR,".text-sm.break-all").text
                print(lesson_name)
                
                tags=div.find_elements(By.CLASS_NAME,"mr-2")
                credit_number= tags[0].text
                print(credit_number)
                if len(tags)>2:
                    teacher_name = tags[2].text
                else:
                    teacher_name=""
                    print(teacher_name)
                    
                
                if len(tags)>3:
                    lesson_days = tags[3].text
                    print(lesson_days)
                else:
                    lesson_days=""
                if len(tags)>4:
                    lesson_hours = tags[4].text
                    print(lesson_hours)
                else:
                    lesson_hours=""
                
                
                row = [lesson_code,lesson_name,teacher_name,lesson_days,lesson_hours,credit_number]
                thewriter.writerow(row)
                
                
        inputs=text.find_element(By.CSS_SELECTOR,"#app > main > div.flex.flex-col.md\:flex-row.grow.md\:overflow-hidden > div.w-full.md\:w-7\/12.p-2.flex.flex-col.grow.h-full > div.grow-0.shrink-0.relative.w-full.shadow.rounded-lg.overflow-hidden > input").send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        
        

        
            
    
    
except TimeoutException:
   print("Loading took too much time!")



