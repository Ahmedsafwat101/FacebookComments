import pyautogui
import time

# Write any comment you need  
comments = ["#FreePalestine","‎‏#savesheikhjarrah #ŞeyhJarrahmahallesinkurtarın #SalvailquartierediSheikhJarrah #RettedasViertelSheikhJarrah #sauvezlequartierdesheikhjarra","#GazaUnderAttack","#Israel_uses_phosphorus_bombs#SaveGaza#GazaUnderAttack#Gaza_Under_Attack#Palestine","#Save_GAZA","#Palestinian","#GazaUnderAttack #Gaza #israelusesphosphorusbombs #Palestine ","#GazaUnderAttack #Gaza #israelusesphosphorusbombs #Palestine #FreePalestine #savesheikhjarrah","# this time will give you 5 seconds to put your cursor on the write place for writing comments"]  
time.sleep(5)

#numberOfComments can be any number 
numberOfComments = 100

for i in range(numberOfComments):
    pyautogui.typewrite(comments[i%len(comments)])
    pyautogui.typewrite('\n')
    #this time will give you normal delay to not show that you are using a script 
    time.sleep(15)

