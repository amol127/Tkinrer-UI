import tkinter
from tkinter  import *
import tkinter as ttk
from tkinter.ttk import Combobox
import json,requests,os
from csv import *
import shutil
from shutil import copyfile
from tkinter import filedialog,messagebox
import pyqrcode
import smtplib
from PIL import ImageTk,Image
import imghdr
from email.message import EmailMessage

window=Tk()
window.title("Skroman Production Burning Process!")
#photo = PhotoImage(file = "D:/project/icon.png")
#window.iconphoto(False, photo)

window.geometry('750x760+0+0')

#################################### Data Load And Dumbs##########################

def esp_fun():            
    global data 
    global esp_no
    global unique_id
    global pop

    try:
        if entry.get():            
            esp_no = esp_entry.get()

            ESP_NO = {"ESP_NO": str(esp_no)}
            n_data = json.dumps(ESP_NO)
            URL = "http://13.233.196.149:3000/esptrack/getautoincrement"
            r = requests.get(url=URL, data=ESP_NO)
            data = r.json()
            employee_dict = json.dumps(data)
            res_data = json.loads(employee_dict)
            main_data = res_data['result']
            esp_no = main_data['ESP_NO']
            unique_id = main_data['unique_id']
            pop = main_data['POP']
            
            data=(f"ESP_NO:{esp_no}\nUnique_Id:{unique_id}\nPOP:{pop}")

            QR()
    except:
        messagebox.showerror("Error", "Please Enter the Currect Value")

def my_delete():
    images.destroy()
    

def QR():
    global img ,qr

    j_creation = {
            "ModelNo": module.get(),
            "ESP_NO": str(esp_no),
            "unique_id": unique_id,
            "POP": pop,
            "DeviceType": module_type.get()
           }    
    
    if (len(module.get())!=0 ):

        data = json.dumps(j_creation)
        qr = pyqrcode.create(data)
        img = BitmapImage(data = qr.xbm(scale=4),background="white")
    try:
        display_code()
    except: 
        pass
    
def display_code():
        images.config(image = img)
        qrlabel.config(text=""+ data)
        qrlabel1.config(text=""+ module.get())
        qrlabel2.config(text="" + module_type.get())
        showdata.delete('1.0',END)

        showdata.insert(END, f'CLIENT: {entry.get()}\nESP_NO: {esp_no}\nMODULE: {module.get()}\nTYPE: {module_type.get()}\nUUID: {unique_id}\nPOP: {pop}\nMODE: non-Replica\nPLATE: {combobox3.get()}')        
   
def save_qr():    
    if qr is not None:

        defaultPath = 'E:/Skroman Production Burning/Skroman QR/'
        
        file_types = [('PNG', '.png')]
        file_name='C:/Espressif/frameworks/esp-idf-v4.4.4/SK/eeprom_elite_module/spiffs_dir/images.png'
        duplicate = defaultPath + unique_id + ".png"
        
        if file_name:
            qr.png(file_name, scale = 8)
            qr.png(duplicate, scale = 8)
            
qr = None
img = None




################## Combo Box ########################


sites = ["44010", "46000", "66010", "68000", "88010", "87020", "80000", "13000", "20000", "23000"]

sites2 = ["Switch Box","2 -Module","MOOD Switch"]

def callback(*args):
    selection=combobox1.get()

    if selection == "13000":
    
       module_type.set(sites2[2])
       
    elif selection == "20000":
       
        module_type.set(sites2[1])
        

    elif selection == "23000":
       
        module_type.set(sites2[1])
    else:
        
        module_type.set(sites2[0])
    

module = StringVar()
module.set("44010")

module_type = StringVar()
module_type.set("Switch Box")



################ third Combo box ###################################

color = ["Black", "White", "Gold", "Silver", "P5", "P6", "P7", "P8", "P9"]
code = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def fatch(*args):
    select=combobox3.get()
    
    if select == color[0]:
        com1.set(code[0])

    elif select == color[1]:
        com1.set(code[1])
        

    elif select == color[2]:
        com1.set(code[2])
        
    elif select == color[3]:
        com1.set(code[3])

    elif select == color[4]:
        com1.set(code[4])

    elif select == color[5]:
        com1.set(code[5])

    elif select == color[6]:
        com1.set(code[6])

    elif select == color[7]:
        com1.set(code[7])

    elif select == color[8]:
        com1.set(code[8])


################################# EEPROM CODE  ##############################################################

def eeprom_new(): 
    os.system('start cmd /k "sh eeprom_elite_module.sh"')

def elite_new():
    print("ELITE NEW SERVICE INVOKED!")
    
    if esp_entry.get() and entry.get():
        entry.delete('0',END)
        esp_entry.delete('0',END)
        
        try:
                
            os.remove('C:/Espressif/frameworks/esp-idf-v4.4.4/SK/eeprom_elite_module/spiffs_dir/cert/AmazonRootCA1.pem')
            os.remove('C:/Espressif/frameworks/esp-idf-v4.4.4/SK/eeprom_elite_module/spiffs_dir/cert/certificate.pem.crt')
            os.remove('C:/Espressif/frameworks/esp-idf-v4.4.4/SK/eeprom_elite_module/spiffs_dir/cert/private.pem.key')

        except:
            massege.showerror("ERROR","Folder is Not Empty")
           
        getModule = combobox1.get()
        
        if getModule == "44010":
            os.system('start cmd /k "sh build_elite_44010.sh"')

        elif getModule == "46000":
            os.system('start cmd /k "sh build_elite_46000.sh"')

        elif getModule == "66010":
            os.system('start cmd /k "sh build_elite_66010.sh"')

        elif getModule == "68000":
            os.system('start cmd /k "sh build_elite_68000.sh"')

        elif getModule == "88010":
            os.system('start cmd /k "sh build_elite_88010.sh"')

        elif getModule == "87020":
            os.system('start cmd /k "sh build_elite_87020.sh"')

        elif getModule == "80000":
            os.system('start cmd /k "sh build_elite_80000.sh"')

        elif getModule == "13000":
            os.system('start cmd /k "sh build_elite_13000.sh"')

        elif getModule == "20000":
            os.system('start cmd /k "sh build_elite_20000.sh"')

        elif getModule == "23000":
            os.system('start cmd /k "sh build_elite_23000.sh"')
    

#########################  Burning Process ###############################

def slide():
    print("SLIDE NEW SERVICE INVOKED!")
    
    if esp_entry.get() and entry.get():
        entry.delete('0',END)
        esp_entry.delete('0',END)
        
        try:
                
            os.remove('C:/Espressif/frameworks/esp-idf-v4.4.4/SK/eeprom_elite_module/spiffs_dir/cert/AmazonRootCA1.pem')
            os.remove('C:/Espressif/frameworks/esp-idf-v4.4.4/SK/eeprom_elite_module/spiffs_dir/cert/certificate.pem.crt')
            os.remove('C:/Espressif/frameworks/esp-idf-v4.4.4/SK/eeprom_elite_module/spiffs_dir/cert/private.pem.key')
   
        except:
            massege.showerror("ERROR","Folder is Not Empty")
           
        getModule = combobox1.get()
        
        if getModule == "44010":
            os.system('start cmd /k "sh build_slide_44010.sh"')

        elif getModule == "46000":
            os.system('start cmd /k "sh build_slide_46000.sh"')

        elif getModule == "66010":
            os.system('start cmd /k "sh build_slide_66010.sh"')

        elif getModule == "68000":
            os.system('start cmd /k "sh build_slide_68000.sh"')

        elif getModule == "88010":
            os.system('start cmd /k "sh build_slide_88010.sh"')

        elif getModule == "87020":
            os.system('start cmd /k "sh build_slide_87020.sh"')

        elif getModule == "80000":
            os.system('start cmd /k "sh build_slide_80000.sh"')

        elif getModule == "13000":
            os.system('start cmd /k "sh build_slide_13000.sh"')

        elif getModule == "20000":
            os.system('start cmd /k "sh build_slide_20000.sh"')

        elif getModule == "23000":
            os.system('start cmd /k "sh build_slide_23000.sh"')


def elite_old():
    print("ELITE OLD SERVICE INVOKED!")

    if esp_entry.get() and entry.get():
        entry.delete('0',END)      
        esp_entry.delete('0',END)
        
        try:
                
            os.remove('C:/Espressif/frameworks/esp-idf-v4.4.4/SK/eeprom_elite_module/spiffs_dir/cert/AmazonRootCA1.pem')
            os.remove('C:/Espressif/frameworks/esp-idf-v4.4.4/SK/eeprom_elite_module/spiffs_dir/cert/certificate.pem.crt')
            os.remove('C:/Espressif/frameworks/esp-idf-v4.4.4/SK/eeprom_elite_module/spiffs_dir/cert/private.pem.key')

            
        except:
            massege.showerror("ERROR","Folder is Not Empty")
           
        getModule = combobox1.get()
        
        if getModule == "44010":
            os.system('start cmd /k "sh build_elite_old_44010.sh"')

        elif getModule == "46000":
            os.system('start cmd /k "sh build_elite_old_46000.sh"')

        elif getModule == "66010":
            os.system('start cmd /k "sh build_elite_old_66010.sh"')

        elif getModule == "68000":
            os.system('start cmd /k "sh build_elite_old_68000.sh"')

        elif getModule == "88010":
            os.system('start cmd /k "sh build_elite_old_88010.sh"')

        elif getModule == "87020":
            os.system('start cmd /k "sh build_elite_old_87020.sh"')

        elif getModule == "80000":
            os.system('start cmd /k "sh build_elite_old_80000.sh"')            


def email():    
    try:
        esp_no=esp_entry.get()
        
        msg = EmailMessage()
        msg['Subject'] = f"Skroman Device (ESP_NO:{esp_no},Unique_Id:{unique_id},POP:{pop},Module:{module.get()},Module Name:{module_type.get()},no-replica,{com.get()})".replace('\n','').replace('\n','')
        
        msg['From'] = 'skromanproductionlogs'
        msg['To'] =  'skromanproductionlogs@gmail.com'

        with open('C:/Espressif/frameworks/esp-idf-v4.4.4/SK/eeprom_elite_module/spiffs_dir/images.png',"rb") as f:
            file_data = f.read()
            #print("file send",file_data)
            filetype = imghdr.what(f.name)
            file_name = f.name
            #print("File name is",file_name)
            msg.add_attachment(file_data, maintype="image", subtype=filetype, filename=file_name)
            

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
                server.login("skromanproductionlogs@gmail.com","rxpxoybstpcpkpyb")
                server.send_message(msg)
                os.remove(file_name)
        messagebox.showinfo("Information", f"Successfully Get")
    except:
        messagebox.showerror("Error", f"Email Not send")

##############################################################################################

def browes_1():
    try:
        
        files = filedialog.askopenfilenames(initialdir = "E:/Skroman Production Burning/Skroman Clients", title = 'Choose a File')
        
        for file in files:
            shutil.copy(file,'C:/Espressif/frameworks/esp-idf-v4.4.4/SK/eeprom_elite_module/spiffs_dir/cert')
                    
        if files:
            file=files[0]
            filename=os.path.basename(file)
            foldername= os.path.basename(os.path.dirname(file))
            
            client.set(foldername)

            clientName = foldername
            
    except :
        messagebox.showerror("Error", "Error: Certificate Not Selected Yet!")
        
        
############################ txt file create    ###################
def txtfile():    
    try:
        esp_no=esp_entry.get()
        file_path = os.path.join("C:/Espressif/frameworks/esp-idf-v4.4.4/SK/eeprom_elite_module/spiffs_dir/info", "device_info.txt")
        with open (file_path,'w') as file:
            file.write(f"V1!\n{module.get()}!\n{esp_no}!\n{unique_id}!\n{pop}!\nnon_replica!\n{com1.get()}!\n{entry.get()}!")
        list=[esp_no,unique_id,pop,module.get(),module_type.get(),combobox3.get(),"non-replica"]
    except:
        messagebox.showerror("showerror"," txt file not save")
        
    try:
        esp_no=esp_entry.get()
        file_path2=os.path.join('C:/Espressif/frameworks/esp-idf-v4.4.4','data.csv')
        with open('data.csv','a',newline='') as file:
            Writer=writer(file)
            if file.tell()==0:
                Writer.writerow(["ESP NO","Unique ID","POP","Module","Module Type","plate","Type"])
            Writer.writerow(list)
            #messagebox.showinfo("information","CSV save")
    except:
        messagebox.showerror("showerror","CSV file not save")
        




####################################################################################################
mainframe=Frame(window, width=2000,height=2000,bg="#ADD8E6")
mainframe.place(x=0,y=0)

titlelabel=Label(window,text="SKROMAN PRODUCTION BURNING CONSOLE",bg="#FF7722",width=65,font=("times",15,'bold'))
titlelabel.place(x=0,y=0)

###############################    All  Frame   ############################################## 

frame1=Frame(mainframe,bg="white", width=660,height=290,)
frame1.place(x=40,y=90)

frame2=Frame(frame1,width=314,height=273 ,bg="white",relief=GROOVE,highlightbackground="black", highlightthickness=1 )
frame2.place(x=10,y=10)

frame3=Frame(window, width=660,height=280)
frame3.place(x=40,y=400)

frame4=Frame(frame3,width=640,height=85,bg="white",relief=GROOVE,highlightbackground="black", highlightthickness=1)
frame4.place(x=10,y=70)
#########################################################

showdata=Text(frame1,width=30,height=14,font=('bold',13),relief=GROOVE,highlightbackground="black", highlightthickness=1)
showdata.place(x=370,y=10)
var=StringVar()

images = Label(frame2,textvariable=var, bg = "white")
images.place(x = 25,y = 0)

qrlabel=Label(frame1, text="",bg="white") 
qrlabel1=Label(frame1, text="",bg="white")
qrlabel2=Label(frame1, text="",bg="white")
qrlabel3=Label(frame1, text="",bg="white")


#################################################################################

comboboxlbl=Label(frame3,text="MODULE",font=('bold',13))
comboboxlbl.place(x=288,y=5)

combobox1=Combobox(frame3,textvariable=module,values=sites,width=20,height=2,font=('bold',12))
combobox1.bind('<<ComboboxSelected>>',callback)
combobox1.place(x=220,y=35)

combobox2=Combobox(frame3,textvariable=module_type,value=module_type ,width=20,height=2,font=('bold',12))
combobox2.bind('<<ComboboxSelected>>',callback)

plate=Label(frame3,text="PLATE",font=('bold',13))
plate.place(x=510,y=5)
com=StringVar()
com.set("Black")
combobox3=Combobox(frame3 ,textvariable=com ,values=color,width=20,height=2,font=('bold',12))
combobox3.bind('<<ComboboxSelected>>',fatch)
combobox3.place(x=440,y=35)

com1=StringVar()
com1.set("1")

code_com=Combobox(frame3,value=code)
code_com.bind('<<ComboboxSelected>>',fatch)
#code_com.place()
###########################################################

esplbl=Label(frame3,text="ESP NO ",font=('bold',13))
esplbl.place(x=70,y=5)

esp_entry=ttk.Entry(frame3,width=21,font=("bold",12),relief=GROOVE,border=2)
esp_entry.place(x=10,y=35)

################### Ulopad Document File Button ##########################

l1=Label(frame4,text="CLIENT CERT",bg="white",font=('bold',13))
l1.place(x=80,y=5)

button1=Button(frame4,text="BROWSE",width=25,relief=GROOVE,bg="#FF9933",font=("times",14),command=browes_1)
button1.place(x=20,y=35,height=33)

l2=Label(frame4,text="CLIENT NAME",bg="white",font=('bold',13))
l2.place(x=390,y=5)

client=StringVar()

entry=Entry(frame4,textvariable=client,font=("times",14,"bold"),width=30,relief=GROOVE,highlightbackground="black", highlightthickness=1)
entry.place(x=310,y=35,height=33)

###########################################################################


get_data = Button(frame3, text = "GET DATA", width = 17, border = 2, relief = GROOVE, bg = "#ADD8E6", font = ("times", 14), command = lambda:[esp_fun(),save_qr(),txtfile(),email()])
get_data.place(x = 10, y = 170)

eepromb = Button(frame3, text = "EEPROM - NEW", width = 17, border = 2, relief = GROOVE, bg = "#ADD8E6", font = ("times", 14), command = eeprom_new)
eepromb.place(x = 242, y = 170)

Burning = Button(frame3,text = "ELITE - NEW", width = 17, border = 2, relief = GROOVE, bg = "#ADD8E6", font = ("times", 14), command = elite_new)
Burning.place(x = 470, y = 170)

dummy_1 = Button(frame3, text = "ELITE - OLD", width = 17, border = 2, relief = GROOVE, bg = "#ADD8E6", font = ("times", 14), command = elite_old)
dummy_1.place(x = 10, y = 225)

dummy_2 = Button(frame3, text = "SLIDE SERIES", width = 17, border = 2, relief = GROOVE, bg = "#ADD8E6", font = ("times", 14),command = slide)
dummy_2.place(x = 242, y = 225)

dummy_3 = Button(frame3, text = "OTA", width = 17, border = 2, relief = GROOVE, bg = "#ADD8E6", font = ("times", 14))
dummy_3.place(x = 470, y = 225)

window.mainloop()
