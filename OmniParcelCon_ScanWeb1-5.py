from selenium import webdriver
from ast import Pass, Return, Try
from cgitb import text
from copy import copy
from multiprocessing.connection import wait
from pydoc import html, visiblename
import pyperclip
from requests import options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException ,WebDriverException ,NoAlertPresentException
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import array



# chrome_option = Options()

cpylist = []

# driver = webdriver.Chrome(executable_path="C:/Users/NISHITA-PC/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()

# driver.get("https://op-web1.omniparcel.com")
# driver.get("https://op-web2.omniparcel.com")
# driver.get("https://op-web3.omniparcel.com")
# driver.get("https://op-web4.omniparcel.com")
driver.get("https://op-web5.omniparcel.com")
# driver.get("https://op-print1.omniparcel.com")
# driver.get("https://op-print2.omniparcel.com")
    # driver.get("https://op-test1.omniparcel.com")


#--------------- Login ---------------
driver.find_element_by_id("UserName").send_keys("vikas@omniparcel.com")
driver.find_element_by_id("Password").send_keys("Vikas@123")
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)


#________________________________________________________________________________________________________________________
# # --------------- Switch Site  for test.omniparcel.com -----------------
# driver.find_element_by_xpath("//span[@class='user-info']").click()
# time.sleep(0.5)
# driver.find_element_by_xpath("//a[normalize-space()='Switch Site']").click()
# time.sleep(2)
# driver.find_element_by_id("Search").send_keys("omni test")
# time.sleep(2)
# driver.find_element_by_css_selector("#div_changesite_list > table > tbody > tr:nth-child(2) > td:nth-child(2) > a").click()
# time.sleep(2)
#________________________________________________________________________________________________________________________


#--------------- Switch Site for Omni Test login user  ---------------
def switchuser():
    switchsite = driver.find_element_by_id("search-switch-site")
    switchsite.send_keys("OMNI TEST")
    time.sleep(1)
    driver.find_element_by_xpath("//a[.='OMNI TEST (Omni Parcel Master Account) -1281029']").click()

switchuser()

for i in range(4):

    actname = 'Omni Test,'
    aflog = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/a/span[1]/small")
    aftlogname = aflog.text
    print ("\n\n====================\n", aftlogname)
    print ("====================\n")

    if actname == aftlogname:
        print("\n\n====================\nSwitched User Successfully\n====================\n")
        break
    else: 
        print("\n\n====================\nUser CAN NOT Switched Try Again\n====================\n")
        switchuser()

if actname != aftlogname:
    print("\n\n====================\nRun Script Again\n====================\n")    
    driver.quit()
    # else:
    #     driver.quit()

#--------------- Select Country ---------------
driver.find_element_by_xpath("//select[@id='Destination_CountryCode']").click()
time.sleep(0.5)
# driver.find_element_by_xpath("//select[@id='Destination_CountryCode']").send_keys(Keys.ENTER)
# time.sleep(0.5)
driver.find_element_by_css_selector("#Destination_CountryCode > option:nth-child(1)").click()
time.sleep(0.5)
driver.find_element_by_id("Destination_Name").send_keys("test")
time.sleep(1)
driver.find_element_by_id("Destination_Name").send_keys(Keys.ENTER)
time.sleep(0.5)


#--------------- Fill Data for Outbound & Export >> Receiver Data -----------------
driver.find_element_by_id("stock_length_1").send_keys("1")
time.sleep(0.5)
driver.find_element_by_id("stock_width_1").send_keys("1")
time.sleep(0.5)
driver.find_element_by_id("stock_height_1").send_keys("1")
time.sleep(0.5)
driver.find_element_by_id("stock_kg_1").send_keys("1")
time.sleep(0.5)


#---------- Fill Data for Outbound & Export >> Packges ----------
driver.find_element_by_xpath("//div[@id='collapse_Commodities']//h4[@class='panel-title']").click()
time.sleep(0.5)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/table/tbody/tr/td[3]/input").send_keys("NZ01123")
time.sleep(0.5)
driver.find_element_by_xpath("//input[@id='commo_kg_0']").send_keys(Keys.CONTROL + "a") 
time.sleep(0.5)
driver.find_element_by_xpath("//input[@id='commo_kg_0']").send_keys("10")
time.sleep(0.5)
driver.find_element_by_xpath("//input[@id='commo_units_0']").send_keys("5")
time.sleep(0.5)
driver.find_element_by_xpath("//input[@id='commo_price_0']").send_keys("100")
time.sleep(0.5)
# Click on calculate Freight button

driver.find_element_by_id("btncalculate").click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, 400);")



driver.find_element_by_xpath("//tbody[@id='tblrates-body']/tr[1]//span[@class='glyphicon glyphicon-paperclip']").click()
time.sleep(1)
driver.refresh()
time.sleep(5)


def vnnote() : 
    try:
            connotenumber = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/a")
            print ("\n\n====================\nCONNOTE NO.(0) IS :-  " + connotenumber.text)
            print ("====================\n")
            cpylist.append(connotenumber.text)
            # pyperclip.copy(connotenumber.text)
            print ("\n\n====================\n", cpylist)
            print ("====================\n")
            return True
    except :
            # print ("\n\n*-*-*-*-*-*-*-\n\n  CONNOTE NOT VISIBLE \n")
            return False
time.sleep(1)



print ("\n\n====================================================================================================================")
print ("-------------------------------- Click on reprint & manifests --------------------------------")
print ("====================================================================================================================\n\n")

time.sleep(0.2)
driver.find_element_by_xpath("//a[normalize-space()='Reprint & Manifests']").click()
time.sleep(2)

# Copy ConNote number in above popup 
cnnumber = False
if vnnote() is True:
    cnnumber = True
    print ("\n\n====================\n Number copy successfully \n====================\n")
else :
    cnnumber = False
    print ("\n\n====================\n Try again \n====================\n ")


#---------- Select Carrier from Dropdown ----------
# select FGMail
fgmail = driver.find_element_by_xpath("//select[@id='filter']")
fgmail.click()
time.sleep(1)
fgmail.send_keys("FGMail")
time.sleep(1)
fgmail.send_keys(Keys.ENTER)
time.sleep(1)


if cnnumber is True:
        print ("\n\n====================\n Number Already Copied Successfully--[1] \n====================\n")      
else:
        printconnot1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/form[2]/div/div/table/tbody/tr[1]/td[2]")
        print ("\n\n====================\nCONNOTE NO.(2) IS :-  " + printconnot1.text)
        print ("\n====================\n\n")
        time.sleep(0.5)
        # pyperclip.copy(printconnot1.text)
        cpylist.append(printconnot1.text)
        print ("\n\n====================\n", cpylist)
        print ("====================\n")
      
#---------- Select First one data in Reprint&Manifests List ----------
driver.find_element_by_css_selector("[value="+cpylist[0]+"]").click()
time.sleep(1)
# Scroll down to bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.find_element_by_xpath("//button[@id='btnsendmanifest']").click()
time.sleep(5)



print ("\n\n====================================================================================================================")
print ("---------- Click on Adminstration >> Shipment Report (We directly get shipment link here) ----------")
print ("====================================================================================================================\n\n")

#---------- Click on Adminstration Select Shipment Report (We directly get shipment link here) ----------
def shipmntlink():
    # driver.get("http://op-web1.omniparcel.com/ShipmentReport")
    # driver.get("http://op-web2.omniparcel.com/ShipmentReport")
    # driver.get("http://op-web3.omniparcel.com/ShipmentReport")
    # driver.get("http://op-web4.omniparcel.com/ShipmentReport")
    driver.get("http://op-web5.omniparcel.com/ShipmentReport")
    # driver.get("https://op-print1.omniparcel.com/ShipmentReport")
    # driver.get("https://op-print2.omniparcel.com/ShipmentReport")

shipmntlink()    
time.sleep(3)
driver.find_element_by_xpath("//input[@id='ConnoteNumber']").send_keys(cpylist[0])
time.sleep(2)
driver.find_element_by_xpath("//input[@id='Search']").click()
time.sleep(0.5)
 
#---------- Scrolling page ----------
driver.execute_script("window.scrollTo(0, 500);")
time.sleep(1)

#---------- Find where carrier number display and copy or store in array ----------
carriertrackno = driver.find_element_by_xpath("//div[@id='myModal']//div[1]/table[@class='table table-bordered table-condensed col-md-12']//td[3]")
copycarriernumber = carriertrackno.text
# pyperclip.copy(copycarriernumber)
cpylist.append(carriertrackno.text)
print ("\n\n====================\n", cpylist)
print ("====================\n\n")
print ("\n\n====================\n Carrier Tracking Number is :-  " + copycarriernumber)
print ("====================\n")
time.sleep(1)

driver.execute_script("window.scrollTo(0, 300);")
time.sleep(1)

#---------- Find where carrier number display and copy or store in array ----------
SManifestNo = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[4]/div/div[5]/table/tbody/tr/td[1]")
copySManifestNo = SManifestNo.text
# pyperclip.copy(copycarriernumber)
cpylist.append(SManifestNo.text)
print ("\n\n====================\n", cpylist)
print ("====================\n\n")
print ("\n\n====================\n Manifest Number is :-  " + copySManifestNo)
print ("====================\n")
time.sleep(1)



#---------- Click on Export >> Check Scan ----------
driver.find_element_by_xpath("//a[.='Exports']").click()
time.sleep(1)
driver.find_element_by_xpath("//a[.='Check/Receipt Scan']").click()
time.sleep(1)
print ("\n\n====================\n", cpylist)
print ("====================\n\n")
driver.find_element_by_xpath("//input[@id='barcode']").send_keys(cpylist[1])
time.sleep(2)
driver.find_element_by_xpath("//button[@id='btnsubmit']").click()
time.sleep(1)
# Display MSG in Terminal which one is seen in page
resulscan = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/form/div[8]/div/div")
barcodescan = resulscan.text
print ("\n\n====================\n" + barcodescan)
print ("====================\n\n")
time.sleep(10)



print ("\n\n====================================================================================================================")
print ("---------------------------------------- Click on Export >> Consolidate to MAWB ----------------------------------------")
print ("====================================================================================================================\n\n")

# --------------- Select Consolidate to MAWB ---------------
driver.find_element_by_xpath("//a[.='Exports']").click()
time.sleep(1)
driver.find_element_by_xpath("//a[.='Consolidate MAWB']").click()
time.sleep(5)

#Select Hub
selhub = driver.find_element_by_xpath("//select[@id='ConsolidationHubId']")
time.sleep(0.3)
selhub.click()
time.sleep(0.3)
selhub.send_keys("TEST")
time.sleep(0.3)
selhub.send_keys(Keys.ENTER)
time.sleep(1)

# Select manifest number which we store above array
print ("\n\n====================\n", cpylist)
print ("====================\n\n")


#------------- Select first entry in test hub list -------------
xy = driver.find_element_by_css_selector("[data-manifest="+cpylist[2]+"][name='selected']")
time.sleep(1)
xy.click()

time.sleep(1)

# Scroll down to bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

#click on assign MAWB & Send Button
driver.find_element_by_xpath("//button[@id='btnmwab']").click()
time.sleep(2)

#fill MAWB allocate and send
driver.find_element_by_id("OriginCountry").send_keys("Australia")
time.sleep(0.5)
driver.find_element_by_id("PortOfDischargeId").send_keys("Sydney")
time.sleep(0.5)
driver.find_element_by_id("OriginAgent").send_keys("Sydn")
time.sleep(1)

def selcntname():
    selcun = Select (driver.find_element_by_id ("DestinationCountry"))
    selport = selcun.select_by_visible_text ('NEW ZEALAND')
    time.sleep(1)
    
    sel = Select (driver.find_element_by_id ("PortOfLadingId"))
    selport1 = sel.select_by_visible_text ('AUCKLAND > AKL')
    time.sleep(1)
    

selcntname()

driver.find_element_by_id("DestinationAgent").send_keys("AUCKLAND > AKL > Seko")
time.sleep(1)
driver.find_element_by_id("VesselNumber").send_keys("123456")
time.sleep(1)

stmawb = "444"
driver.find_element_by_id("ThreeMAWB").send_keys(stmawb)
cpylist.append(stmawb)
time.sleep(0.3)
stmawb1 = "98755423"
driver.find_element_by_id("EightMAWB").send_keys(stmawb1)
cpylist.append(stmawb1)
time.sleep(0.5)

#select Date    
import datetime
NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
Current_Date_Formatted = NextDay_Date.strftime ("%d-%b-%Y %H:%M") # format the date to ddmmyyyy
print ('Current Date: ' + str(Current_Date_Formatted))
driver.find_element_by_id("ETA").send_keys(str(Current_Date_Formatted))
time.sleep(1)
driver.find_element_by_id("consolidateButton").click()
time.sleep(1)
# Alert msg accept
def acceptalert():
    obj = driver.switch_to.alert
    #Retrieve the message on the Alert window
    msg = obj.text
    print("Alert shows following message: \n\n" + msg)
    #use the accept() method to accept the alert
    obj.accept()
    return True
#alert msg accept is saw then hit otherwise ignore    
if acceptalert() is True:
    print ("\n\n=======\n Pass \n=======\n\n")
else:
    print ("\n\n=======\n Fail \n=======\n\n")    
time.sleep(7)

# # after hit button genarate successfully msg print in Terminal or Output display
# def msgdsp():
    # dispmsg = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]")

# #successfully msg which line print overthere we print in out system terminal or output display    
# if msgdsp() is visiblename(dispmsg):
#     print("\n\nMsg Displayed :-\n\n", msgdsp().dispmsg.text)
# else:
#     print ("\n\n=======\n Done \n=======\n\n")
# time.sleep(10)


print ("\n\n====================================================================================================================")
print ("---------------------------------------- Click on Import >> Customs Release Check ----------------------------------------")
print ("====================================================================================================================\n\n")

time.sleep(1)
importmenu = driver.find_element_by_css_selector(".nav > li:nth-of-type(4) > .dropdown-toggle")
time.sleep(0.5)
importmenu.click()
time.sleep(0.5)
Customs = driver.find_element_by_xpath("//a[normalize-space()='Customs Release Check']")
Customs.click()
time.sleep(0.5)
#Select MAWB in Dropdown
print ("\n\n====================\n", cpylist)
print ("====================\n\n")
driver.find_element_by_xpath("//span[.='Select']").click()
time.sleep(1)
enmawb = driver.find_element_by_xpath("//div[@class='chosen-search']/input[1]")
enmawb.send_keys(cpylist[3]+cpylist[4])
time.sleep(0.5)
enmawb.send_keys(Keys.ENTER)
time.sleep(0.5)
driver.find_element_by_xpath("//input[@id='barcode']").send_keys(cpylist[1])
time.sleep(0.5)
driver.find_element_by_id("btnsubmit").click()
time.sleep(1)


mawbresul = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/form/div[4]/div/div")
mawbresul1 = mawbresul.text
print ("\n\n====================\n" + mawbresul1)
print ("====================\n\n")