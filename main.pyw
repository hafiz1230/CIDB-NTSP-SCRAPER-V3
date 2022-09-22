#Created by Hafiz Zulkepli 21-09-2022
import sys
import pandas as pd
from userInterface import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from functools import partial
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from selenium import webdriver
from selenium.webdriver.chrome.service import Service # Similar thing for firefox also!
from subprocess import CREATE_NO_WINDOW
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from csv import writer
import xlsxwriter
import os
import shutil
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import time
from time import mktime
from PIL import Image


class ScrapeWorker(QObject):
    finished=pyqtSignal()
    progress=pyqtSignal(str)
    progress2=pyqtSignal(list)
    progress3=pyqtSignal(list)
    progress4=pyqtSignal(str)

    def start_scrape(self,ic,dirName,month):
        self.current_date=date.today()
        self.dirName=dirName
        self.ic_num_list=ic
        self.months_add=month
        image_row=1
        image_col_cidb=0
        image_col_ntsp=1

        persons=0
        persons_cidb=0
        persons_ntsp=0
        cidb_name_expired=[]
        cidb_date_expired=[]
        ntsp_name_expired=[]
        ntsp_date_expired=[]
        completed=0
        length_list=len(self.ic_num_list)

        cidb_name_expired_month=[]
        cidb_date_expired_month=[]
        ntsp_name_expired_month=[]
        ntsp_date_expired_month=[]


        workbook = xlsxwriter.Workbook(self.dirName +"\Excel File"+"\image.xlsx")
        worksheet = workbook.add_worksheet()
        worksheet.set_default_row(135)
        worksheet.set_column('A:B',38)
        worksheet.write('A1', 'CIDB')
        worksheet.write('B1', 'NTSP')

        csv_title=["Name","NTSP","NTSP Validity","CIDB","CIDB Validity","IC/Passport"]

        with open(self.dirName+"\Excel File"+"\data.csv", 'a',newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(csv_title)
            f_object.close()  

        for i in self.ic_num_list:
            row_check=1
            self.progress4.emit(f"Scraping {i}")

            image_num=str(image_row)
            WINDOW_SIZE = "1295,832"
            options=Options()
            options.headless=True
            options.add_argument("--window-size=%s" % WINDOW_SIZE)
            chrome_service = Service(ChromeDriverManager().install())
            chrome_service.creationflags = CREATE_NO_WINDOW

            driver = webdriver.Chrome(service=chrome_service,options=options)
            browser=webdriver.Chrome(service=chrome_service,options=options)

            driver.get('https://cims.cidb.gov.my/pbsearch/Forms/Transactions/search.aspx?opt=N')
            browser.get("http://online.niosh.com.my/ntsp/ntspdb.nsf/$$ViewTemplate%20for%20semak_appl?OpenForm&key="+i)

            driver.implicitly_wait(10)
            browser.implicitly_wait(10)
            driver.find_element(By.XPATH, "//*[@id='ContentPlaceHolder1_txtsearch']").send_keys(i)
            driver.find_element(By.ID, "ContentPlaceHolder1_cmd").click()

            try:
            
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='form1']/div[5]/div[2]/div[6]/div/div[2]/div/div"))
                )
            
                cidb_name_list=driver.find_elements(By.XPATH, "//*[@id='form1']/div[5]/div[2]/div[6]/div/div[2]/div/div/div[5]/div[5]/div[1]")
                cidb_num_list=driver.find_elements(By.XPATH, "//*[@id='form1']/div[5]/div[2]/div[6]/div/div[2]/div/div/div[5]/div[8]/div[1]")
                cidb_valid_list=driver.find_elements(By.XPATH, "//*[@id='form1']/div[5]/div[2]/div[6]/div/div[2]/div/div/div[5]/div[5]/div[3]")
                cidb_name=cidb_name_list[0].text
                cidb_num=cidb_num_list[0].text
                cidb_valid=cidb_valid_list[0].text
                persons_cidb+=1
                
                self.current_date=date.today()
                format_cidb_date=time.strptime(cidb_valid,"%d/%m/%Y")
                
                format_cidb_date= datetime.fromtimestamp(mktime(format_cidb_date))
                
                format_cidb_date=format_cidb_date.date()
                append_months = date.today() + relativedelta(months=+self.months_add)
                
                if format_cidb_date<= self.current_date:
                    cidb_name_expired.append(cidb_name)
                    cidb_date_expired.append(cidb_valid)

                if format_cidb_date<= append_months:
                    cidb_name_expired_month.append(cidb_name)
                    cidb_date_expired_month.append(cidb_valid)
                
            except:
                cidb_valid="Doesn't Exist"
                cidb_name="Doesn't Exist"
                cidb_num="Doesn't Exist"

        ### ----   NTSP   ----  ###

            try:
                main = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/form/table[2]/tbody/tr/td[1]/table/tbody/tr[1]/th[2]/b/font"))  ##FInd Tarikh Kursus
                )

                ntsp_name_list=browser.find_elements(By.XPATH, "/html/body/form/table[1]/tbody/tr[1]/td[2]/b/font")
                ntsp_name=ntsp_name_list[0].text    
                


                while True:

                    row_check+=1


                    row1="/html/body/form/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td[4]/font"
                    row2="/html/body/form/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td[5]/font"
                    check_column1=row1[:55]+str(row_check)+row1[56:]
                    check_column2=row2[:55]+str(row_check)+row2[56:]

                    try:
                        ntsp_num_list=browser.find_elements(By.XPATH, check_column1)   #ntsp_num
                        ntsp_valid_list=browser.find_elements(By.XPATH, check_column2)   #ntsp_validity
                        ntsp_num=ntsp_num_list[0].text
                        ntsp_valid=ntsp_valid_list[0].text
                        
                    except:
                        break
                

                persons_ntsp+=1

                self.current_date=date.today()
                format_ntsp_date=time.strptime(ntsp_valid,"%d/%m/%Y")
                format_ntsp_date= datetime.fromtimestamp(mktime(format_ntsp_date))
                format_ntsp_date=format_ntsp_date.date()
                append_months = date.today() + relativedelta(months=+self.months_add)

                if format_ntsp_date<= self.current_date:
                    ntsp_name_expired.append(ntsp_name)
                    ntsp_date_expired.append(ntsp_valid)

                if format_ntsp_date<= append_months:
                    ntsp_name_expired_month.append(ntsp_name)
                    ntsp_date_expired_month.append(ntsp_valid)

                

            except:
                ntsp_name="Doesn't Exist"
                ntsp_num="Doesn't Exist"
                ntsp_valid="Doesn't Exist"

        ###  ---   NTSP  --- #####


        
            if cidb_name!="Doesn't Exist":
                name=cidb_name

            elif ntsp_name!="Doesn't Exist":
                name=ntsp_name

            elif cidb_name and ntsp_name=="Doesn't Exist":
                name="ic/passport is "+i
            
            else:
                name="Error"

            ic_list="["+i+"]"

            info=[name,ntsp_num,ntsp_valid,cidb_num,cidb_valid,ic_list]
            info_list1=[i,name,ntsp_num,ntsp_valid,cidb_num,cidb_valid]
            self.progress2.emit(info_list1)

            with open(self.dirName+"\Excel File"+"\data.csv", 'a',newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(info)
                f_object.close()  

            imagename_cidb=self.dirName+"\Screenshot Images"+"\cidb"+image_num+".png"
            driver.save_screenshot(imagename_cidb)
            crop_cidb= Image.open(imagename_cidb)
            left1 = 119
            right1=737
            top1 = 265
            bottom1 = 646
            im1 = crop_cidb.crop((left1, top1, right1, bottom1))
            im1.save(imagename_cidb)
            worksheet.insert_image(image_row,image_col_cidb,imagename_cidb,{'x_scale': 0.44, 'y_scale': 0.44})


            imagename_ntsp=self.dirName+"\Screenshot Images"+"\\ntsp"+image_num+".png"
            browser.save_screenshot(imagename_ntsp)
            crop_ntsp= Image.open(imagename_ntsp)
            left2 = 0
            right2=618
            top2 = 24
            bottom2 = 405
            im2 = crop_ntsp.crop((left2, top2, right2, bottom2))
            im2.save(imagename_ntsp)
            worksheet.insert_image(image_row,image_col_ntsp,imagename_ntsp,{'x_scale': 0.44, 'y_scale': 0.44})

            image_row+=1
            persons+=1
            driver.quit()
            browser.quit()

            completed+=1
            percent_scrape=(completed/length_list)*100

            self.progress.emit(str(percent_scrape))

        workbook.close()

        report_list=[]

        line1=f"Report Date: {self.current_date}"
        report_list.append(line1)

        line2=f'{persons} persons are inserted. {persons_cidb} persons have CIDB and {persons_ntsp} persons have NTSP.'
        report_list.append(line2)

        for index1 in range(len(cidb_name_expired)):
            line3=f"{cidb_name_expired[index1]}'s CIDB is already expired on {cidb_date_expired[index1]}"
            report_list.append(line3)

        for index2 in range(len(ntsp_name_expired)):
            line4=f"{ntsp_name_expired[index2]}'s NTSP is already expired on {ntsp_date_expired[index2]}"
            report_list.append(line4)

        for index3 in range(len(cidb_name_expired_month)):
            line5=f"{cidb_name_expired_month[index3]}'s CIDB validty is on {cidb_date_expired_month[index3]} and will be expired in {self.months_add} months time."
            report_list.append(line5)

        for index4 in range(len(ntsp_name_expired_month)):
            line6=f"{ntsp_name_expired_month[index4]}'s NTSP validity is on {ntsp_date_expired_month[index4]} and will be expired in {self.months_add} months time."
            report_list.append(line6)


        self.progress3.emit(report_list)
        read_file = pd.read_csv (self.dirName+"\Excel File"+"\data.csv")
        read_file.to_excel (self.dirName+"\Excel File"+"\data.xlsx", index = None, header=True)
        os.remove(self.dirName+"\Excel File"+"\data.csv")

        with open(self.dirName+"\Scraping Report.txt","a") as file:

            file.write('\n'.join(report_list))
            file.close()
        self.progress4.emit("Finished")


class MyForm(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.scrape_list=[]

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.progressBar.setHidden(True)
        self.ui.current_scrape.setHidden(True)
        self.ui.create_dir.returnPressed.connect(self.create_folder)
        self.ui.month_dur.returnPressed.connect(self.month_duration)
        self.current_date=date.today()
        self.ic_num_list=[]
        self.ui.ic.returnPressed.connect(self.ic_enter)
        self.ui.start_button.clicked.connect(self.initiate_scrape)
        self.ui.update_button.clicked.connect(self.update_list)
        self.ui.clear_button.clicked.connect(self.clear_list)
        self.ui.finish_button.clicked.connect(QCoreApplication.instance().quit)

    def month_duration(self):
        try:
            self.ui.month_text.setStyleSheet("color:lightgreen;\n")
            self.months_add=int(self.ui.month_dur.text())
            self.ui.month_text.setText(f"{self.months_add} months is added")
        except:
            self.ui.month_text.setStyleSheet("color:rgb(255, 159, 128);\n")
            self.ui.month_text.setText("Please enter months in digit")
            return

    def scrapeResult(self, msg):
        msg_dec=int(float(msg))
        self.ui.progressBar.setValue(msg_dec)

    def scrapeResult2(self, msg2):
        self.scrape_list=msg2
        self.ui.scrape_data.addItem(f"IC/Passport: {self.scrape_list[0]}")
        self.ui.scrape_data.addItem(f"Name:  {self.scrape_list[1]}")
        self.ui.scrape_data.addItem(f"NTSP No. {self.scrape_list[2]}")
        self.ui.scrape_data.addItem(f"NTSP Validity: {self.scrape_list[3]}")
        self.ui.scrape_data.addItem(f"CIDB No.:  {self.scrape_list[4]}")
        self.ui.scrape_data.addItem(f"CIDB Validity:  {self.scrape_list[5]}")
        self.ui.scrape_data.addItem("")
        self.scrape_list=[]        
        

    def scrapeResult3(self, msg3):
        for i in range(len(msg3)):
            self.ui.listWidget.addItem(f"{msg3[i]}\n")
    
    def scrapeResult4(self,msg4):
        self.ui.current_scrape.setStyleSheet("color:lightgreen")
        self.ui.current_scrape.setText(msg4)
    
    
    def initiate_scrape(self):

        if self.ic_num_list and self.dirName and self.months_add is not None:
            self.ui.start_button.setEnabled(False)
            self.ui.start_button.setStyleSheet("background-color: 	rgb(255, 159, 128); color: black")
            self.ui.progressBar.setHidden(False)
            self.ui.current_scrape.setHidden(False)

            self.ui.update_button.setEnabled(False)
            self.ui.update_button.setStyleSheet("background-color: 	rgb(255, 159, 128); color: black")
            
            self.ui.clear_button.setEnabled(False)
            self.ui.clear_button.setStyleSheet("background-color: 	rgb(255, 159, 128); color: black")
            
            self.ui.create_dir.setEnabled(False)

        
            self.ui.month_dur.setEnabled(False)

            
            self.ui.ic.setEnabled(False)
        
        
            self.thread = QThread()
            self.worker = ScrapeWorker()
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(partial(self.worker.start_scrape,self.ic_num_list,self.dirName,self.months_add))
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.progress.connect(self.scrapeResult)
            self.worker.progress2.connect(self.scrapeResult2)
            self.worker.progress3.connect(self.scrapeResult3)
            self.worker.progress4.connect(self.scrapeResult4)

            self.thread.start()
        
        else:
        
            self.ui.current_scrape.setHidden(False)
            self.ui.current_scrape.setStyleSheet("color:rgb(255, 159, 128)")
            self.ui.current_scrape.setText("Please fill in everything first")
            return



            


    def clear_list(self):
        self.ui.ic_table.setStyleSheet("color:lightgreen")
        row=0
        self.ic_num_list=[]
        for x in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.setItem(row,0,QTableWidgetItem(""))
            row += 1
        
        self.ui.tableWidget.setRowCount(0)
        self.ui.ic_table.setText("All IC/ Passport are deleted")


    def update_list(self):
        self.ui.ic_table.setStyleSheet("color:lightgreen")
        row=0
        self.ic_num_list=[]
        for x in range(self.ui.tableWidget.rowCount()):

            self.ic_num= self.ui.tableWidget.item(row, 0).text()
            self.ic_num_list.append(self.ic_num)
            row += 1

        self.ui.ic_table.setText("All IC/ Passport are updated")

    def create_folder(self):
        self.dirName=str(self.ui.create_dir.text())

        try:
            os.mkdir(self.dirName)
            self.ui.dir_text.setStyleSheet("color:lightgreen;\n"
"background-color: rgba(255, 255, 255,0)")
            self.ui.dir_text.setText(f"Directory {self.dirName} created") 

        except FileExistsError:
            try:
                shutil.rmtree(self.dirName)
                os.mkdir(self.dirName)

            except:

                self.ui.dir_text.setStyleSheet("color:rgb(255, 159, 128);\n"
"background-color: rgba(255, 255, 255,0)")
                self.ui.dir_text.setText("Folder or file is currently opened. Please close the file and run again")

                
                return
            
            self.ui.dir_text.setStyleSheet("color:lightgreen;\n"
"background-color: rgba(255, 255, 255,0)")
            self.ui.dir_text.setText(f"Directory {self.dirName} already exists. The folder is overwrite")


        os.mkdir(self.dirName+"\Excel File")
        os.mkdir(self.dirName+"\Screenshot Images")
        


    def ic_enter(self):
        
        
        self.ui.ic_text.setStyleSheet("color:lightgreen")
        self.ic_num= self.ui.ic.text()
        self.ui.ic.clear()
        self.ui.ic_text.setText(f"{self.ic_num} is added")

        self.ic_num_list.append(self.ic_num)

        self.ui.tableWidget.setRowCount(len(self.ic_num_list))

        row_index=0
        for i in self.ic_num_list:
            self.ui.tableWidget.setItem(row_index,0,QTableWidgetItem(i))
            row_index +=1

        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    myapp = MyForm()
    myapp.show() 
    sys.exit(app.exec_())
