import os


print("Welcome, Choose your option : ")
x = input(" [1] Switch to 3.5' LCD Monitor \n [2] Switch to HDMI port \n >> ")


os.system("sudo chmod -R 755 LCD-show")
os.chdir("LCD-show/")

if int(x) == 1:
    os.system("sudo ./LCD35-show")
        
elif int(x) == 2:
    os.system("sudo ./LCD-hdmi")
   
    
        
    

