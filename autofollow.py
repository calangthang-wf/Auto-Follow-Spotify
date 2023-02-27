from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
import threading
import sys
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
from colorama import init, AnsiToWin32



init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

print(Fore.MAGENTA + """
    #                           #######                                        #####                                     
   # #   #    # #####  ####     #        ####  #      #       ####  #    #    #     # #####   ####  ##### # ###### #   # 
  #   #  #    #   #   #    #    #       #    # #      #      #    # #    #    #       #    # #    #   #   # #       # #  
 #     # #    #   #   #    #    #####   #    # #      #      #    # #    #     #####  #    # #    #   #   # #####    #   
 ####### #    #   #   #    #    #       #    # #      #      #    # # ## #          # #####  #    #   #   # #        #   
 #     # #    #   #   #    #    #       #    # #      #      #    # ##  ##    #     # #      #    #   #   # #        #   
 #     #  ####    #    ####     #        ####  ###### ######  ####  #    #     #####  #       ####    #   # #        #
                                                                                
                                                                                Make by CaLangThang
                                                                                Help: t.me/it_is_daijobu                                                                                              
""")
print(Style.RESET_ALL)


admin = Fore.CYAN + "System: "
err = Fore.RED + "System Error: "
warn = Fore.YELLOW + "System Warn: "

print(admin, Fore.WHITE + "Your profile URL: ") 
profile = input(Fore.GREEN + "==> ")  # get profile url

def autoComment():

    # if you want to create a new txt file containing the list of accounts, use this line
    #filename = input('Ente file name: ')   # format filename.txt 

    with open("account.txt", 'r') as f:  # open spotify account list | format gmail:password
            lines = f.readlines()
            rangeLines = len(lines)
    for acc in range(rangeLines):
        
        #call webdrive and add proxy
        with open("proxy.txt", "r") as f:
            linesPr = f.readlines()
            proxy = random.choice(linesPr)
        
        url = profile
        
        driver = webdriver.Chrome() 
        
        data = str(lines[acc])
            
            #get data form text file   
            
        print("*  *  *  *  *  *  *  *  *  *  *  *")

        count = acc + 1
        print(admin, Fore.BLUE + "Action Count: ", Fore.BLUE + str(count))
        print(Style.RESET_ALL)
        
        # import account
        def getGmail():
            if data is None:
                print(err, Fore.RED + " Can't get email from data!\n \tPlease check the input data again! ")
                print(Style.RESET_ALL)
            else:
                gmail = data.split(":")[0]
                print(admin, Fore.GREEN + "Get Email Successfully!")
                print(Style.RESET_ALL)
            return gmail

        def getPassword():
            if data is None:
                print(err, Fore.RED + " Can't get password from data!\n \tPlease check the input data again! ")
                print(Style.RESET_ALL)
            else:
                get_password = data.split(":")[1]
                password = get_password.split(" ")[0]
                print(admin, Fore.GREEN + "Get Password Successfully!")
                print(Style.RESET_ALL)
            return password

        mail = getGmail()
        pwd = getPassword() 

        #main code
        driver.get(url)
        
        time.sleep(2)

        def main():
                #login
            def login():
                elem = driver.find_element(By.ID, 'login-username')  # get username form from login form
                elem.send_keys(mail)
                time.sleep(1)
                elempass = driver.find_element(By.ID, 'login-password') # get password form from login form
                elempass.send_keys(pwd)
                time.sleep(2)
                driver.find_element(By.CSS_SELECTOR, "#composerInput").click()
                print(admin, Fore.GREEN + "Login: Successfully!")
                print(Style.RESET_ALL)
                time.sleep(2)
            login()

            def follow():
                try:
                    driver.get(profile)
                    time.sleep(5)
                    driver.find_element(By.CSS_SELECTOR, '#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > section > div > div.BL__GuO2JsHMR6RgNfwY > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.os-host-scrollbar-vertical-hidden.os-host-transition > div.os-padding > div > div > div > div > button.idI9vydtCzXVhU1BaKLw').click()
                    print(admin, Fore.GREEN + "Follow: Successfully!")
                    print(Style.RESET_ALL)
                    time.sleep(2)
                except:
                    print(err, Fore.RED + "Can't Follow, Try Again!")
                    print(err, Fore.RED + "Please check your profile link again!")
                    print(err, Fore.RED + "Failed: " + Fore.BLUE + str(count))
                    print(Style.RESET_ALL)
                    print("*  *  *  *  *  *  *  *  *  *  *  *")
            follow()
        main()

        driver.close()



# run multithread
num_threads = int(input("Enter number of threads: "))
threads = []

for i in range(num_threads):
    t = threading.Thread(target=autoComment)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()