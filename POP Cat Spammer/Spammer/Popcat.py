from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")


print("")
print("__________             _________         __                           ")
print("\______   \____ ______ \_   ___ \_____ _/  |_                         ")                        
print(" |     ___/  _ \\\\____ \/    \  \/\__  \\\\   __\                        ")      
print(" |    |  (  <_> )  |_> >     \____/ __ \|  |                          ")
print(" |____|   \____/|   __/ \______  (____  /__|                          ")
print("                |__|           \/     \/                              ")
print("                  _________                                           ")
print("                 /   _____/__________    _____   _____   ___________  ")
print("                 \_____  \\\\____ \__  \  /     \ /     \_/ __ \_  __ \ ")
print("                 /        \  |_> > __ \|  Y Y  \  Y Y  \  ___/|  | \/ ")
print("                /_______  /   __(____  /__|_|  /__|_|  /\___  >__|    ")
print("                        \/|__|       \/      \/      \/     \/        ") 

    

print("")
print("")
print("by Plunder")
time.sleep(3)
driver.get("https://popcat.click/")
pop = driver.find_element_by_id('app')

while True:
    pop.click()



       