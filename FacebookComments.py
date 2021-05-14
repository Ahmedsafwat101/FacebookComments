import pyautogui
import time

# Write any comment you need  
comments = ["#FreePalestine","#SalvailquartierediSheikhJarrah #RettedasViertelSheikhJarrah ","#GazaUnderAttack","#Israel_uses_phosphorus_bombs"," #SaveGaza"," #Palestine","#Save_GAZA",
"#ŞeyhJarrah_mahallesini_kurtar","#Siehe_SheikhJarrah_Nachbarschaft","#Sauver_le_quartier_de_SheikhJarrah","#Salva_el_barrio_de_SheikhJarrah","#Salva_il_quartiere_di_SheikhJarrah"]  
time.sleep(5)

#numberOfComments can be any number 
numberOfComments = 100

for i in range(numberOfComments):
    pyautogui.typewrite(comments[i%len(comments)])
    pyautogui.typewrite('\n')
    #this time will give you normal delay to not show that you are using a script 
    time.sleep(60)

