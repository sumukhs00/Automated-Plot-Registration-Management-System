from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MySQLdb
import sys
import datetime
from PyQt5.uic import loadUiType

ui,_ = loadUiType('UIdesign3.ui')


class MainApp(QMainWindow,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()
        self.dark_bluethemes()

    ########################################
    ######### tabs #################

    def Open_homepage(self):
        self.tabWidget.setCurrentIndex(0)
    def Open_emptysite(self):
        self.tabWidget.setCurrentIndex(1)
    def Open_checksite(self):
        self.tabWidget.setCurrentIndex(2)
    def Open_userlogin(self):
        self.tabWidget.setCurrentIndex(3)
    def Open_adminlogin(self):
        self.tabWidget.setCurrentIndex(4)
    def Open_adminpage(self):
        self.tabWidget.setCurrentIndex(5)
    def Open_userpage(self):
        self.tabWidget.setCurrentIndex(6)
        self.db_userpage()
    def Open_registrationpage(self):
        self.tabWidget.setCurrentIndex(7)
    def Open_newadmin(self):
        self.tabWidget.setCurrentIndex(8)
    def Open_newuser(self):
        self.tabWidget.setCurrentIndex(9)
    def Open_newsite(self):
        self.tabWidget.setCurrentIndex(10)
    def Open_allsite(self):
        self.tabWidget.setCurrentIndex(11)
    def Open_salepage(self):
        self.tabWidget.setCurrentIndex(12)
    def Open_sitesforsalepage(self):
        self.tabWidget.setCurrentIndex(13)
        self.db_siteforsalepage()
    ########## END of  tabs ###################
    def Handel_UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)

    ###########clicking buttons#####################
    def Handel_Buttons(self):
        ################ Opening homepage#################
        self.pushButton_1.clicked.connect(self.Open_homepage)
        self.pushButton_6.clicked.connect(self.Open_homepage)
        self.pushButton_21.clicked.connect(self.Open_homepage)
        self.pushButton_24.clicked.connect(self.Open_homepage)
        self.pushButton_27.clicked.connect(self.Open_homepage)
        self.pushButton_30.clicked.connect(self.Open_homepage)
        self.pushButton_10.clicked.connect(self.Open_homepage)
        self.pushButton_79.clicked.connect(self.Open_homepage)
        self.pushButton_69.clicked.connect(self.Open_homepage)
        self.pushButton_57.clicked.connect(self.Open_adminlogin)
        self.pushButton_62.clicked.connect(self.Open_adminlogin)
        self.pushButton_65.clicked.connect(self.Open_homepage)
        self.pushButton_67.clicked.connect(self.Open_adminlogin)
        self.pushButton_80.clicked.connect(self.Open_adminlogin)
        ################ Opening userlogin#################
        self.pushButton_4.clicked.connect(self.Open_userlogin)
        self.pushButton_15.clicked.connect(self.Open_userlogin)
        self.pushButton_22.clicked.connect(self.Open_userlogin)
        self.pushButton_25.clicked.connect(self.Open_userlogin)
        self.pushButton_28.clicked.connect(self.Open_userlogin)
        self.pushButton_31.clicked.connect(self.Open_userlogin)
        self.pushButton_34.clicked.connect(self.Open_userlogin)
        self.pushButton_2.clicked.connect(self.Open_userlogin)
        self.pushButton_58.clicked.connect(self.Open_userlogin)
        self.pushButton_61.clicked.connect(self.Open_userlogin)
        self.pushButton_63.clicked.connect(self.Open_userlogin)
        self.pushButton_66.clicked.connect(self.Open_userlogin)
        self.pushButton_71.clicked.connect(self.Open_userlogin)
        self.pushButton_77.clicked.connect(self.Open_userlogin)
        ################ Opening adminlogin#################
        self.pushButton_5.clicked.connect(self.Open_adminlogin)
        self.pushButton_16.clicked.connect(self.Open_adminlogin)
        self.pushButton_23.clicked.connect(self.Open_adminlogin)
        self.pushButton_26.clicked.connect(self.Open_adminlogin)
        self.pushButton_29.clicked.connect(self.Open_adminlogin)
        self.pushButton_32.clicked.connect(self.Open_adminlogin)
        self.pushButton_33.clicked.connect(self.Open_adminlogin)
        self.pushButton_35.clicked.connect(self.Open_adminlogin)
        self.pushButton_56.clicked.connect(self.Open_adminlogin)
        self.pushButton_60.clicked.connect(self.Open_adminlogin)
        self.pushButton_64.clicked.connect(self.Open_adminlogin)
        self.pushButton_68.clicked.connect(self.Open_adminlogin)
        self.pushButton_70.clicked.connect(self.Open_adminlogin)
        self.pushButton_80.clicked.connect(self.Open_adminlogin)
        ###############################################################
        self.pushButton.clicked.connect(self.Open_emptysite) #open emptysite
        self.pushButton_3.clicked.connect(self.Open_checksite) # open checksite
        self.pushButton_11.clicked.connect(self.Open_registrationpage)  # open register page
        self.pushButton_12.clicked.connect(self.Open_allsite)  # open allsites
        self.pushButton_13.clicked.connect(self.Open_newadmin)  # open addsite
        self.pushButton_14.clicked.connect(self.Open_newsite)  # open newsite
        self.pushButton_36.clicked.connect(self.Open_salepage)  # open salepage
        self.pushButton_39.clicked.connect(self.Open_newuser)  # open newuser
        self.pushButton_38.clicked.connect(self.Open_allsite)  # open allsites
        self.pushButton_40.clicked.connect(self.Open_sitesforsalepage)  # open allsites
        ################################################################
        self.pushButton_72.clicked.connect(self.Open_adminpage)
        self.pushButton_73.clicked.connect(self.Open_adminpage)
        self.pushButton_75.clicked.connect(self.Open_adminpage)
        self.pushButton_76.clicked.connect(self.Open_homepage)
        self.pushButton_78.clicked.connect(self.Open_adminpage)


        ########################Database buttons#####################
        self.pushButton_7.clicked.connect(self.db_emptysite)
        self.pushButton_49.clicked.connect(self.db_checksite)
        self.pushButton_59.clicked.connect(self.db_registersite)
        self.pushButton_18.clicked.connect(self.db_addadmin)
        self.pushButton_19.clicked.connect(self.db_adduser)
        self.pushButton_109.clicked.connect(self.db_newsite)
        self.pushButton_20.clicked.connect(self.db_allsites)
        self.pushButton_8.clicked.connect(self.db_userlogin)
        self.pushButton_9.clicked.connect(self.db_adminlogin)
        self.pushButton_37.clicked.connect(self.db_salepage)


    ###################Data Base Starts################
    def db_emptysite(self): ###### done#######
        self.db=MySQLdb.connect(host='localhost' , user='root' , password='root' , db='plotproject')
        self.cur=self.db.cursor()
        pincode=self.lineEdit.text() #providing pincode

        try:
            self.cur.execute('''call unregistered(%s)''',(pincode,))
            sData = self.cur.fetchall()

            if sData:

                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)

                for row, form in enumerate(sData):
                    for col, item in enumerate(form):
                        self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1

                    rowPos = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPos)

            else:

                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)

        except:
            self.statusBar().showMessage('Invalid pincode')
            self.statusBarClear()



    def db_checksite(self):####done#####
        self.db = MySQLdb.connect(host='localhost', user='root', password='root', db='plotproject')
        self.cur = self.db.cursor()
        siteno = self.lineEdit_2.text()  # providing siteno
        pincode = self.lineEdit_3.text()  # providing pincode
        try:
            self.cur.execute(''' 
                                SELECT siteno,username,useraddress,area,phno,date,googlelink FROM ((registeredsites  
                                natural join owner) natural join pincodes)  
                                where siteno=%s and pincode=%s
                            ''', (int(siteno),int(pincode)))
            data = self.cur.fetchall()
            print(data)

            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)
            self.statusBar().showMessage('Done')
        except:
            self.statusBar().showMessage('Invalid siteno or pincode')






    def db_userlogin(self): #####Done###########
        self.db = MySQLdb.connect(host='localhost', user='root', password='root', db='plotproject')
        self.cur = self.db.cursor()

        global aadharno;
        aadharno = self.lineEdit_4.text()
        password = self.lineEdit_6.text()

        sql='''select aadharno, password from owner'''
        self.cur.execute(sql)
        data=self.cur.fetchall()
        for row in data:
            if aadharno==row[0]and password==row[1]:
                self.statusBar().showMessage('Logged in successfully')
                self.Open_userpage()
                break
            else:
                self.statusBar().showMessage('Invalid aadhar no or password')







    def db_adminlogin(self):#########  done#########
        self.db = MySQLdb.connect(host='localhost', user='root', password='root', db='plotproject')
        self.cur = self.db.cursor()

        adminid = self.lineEdit_5.text()
        password = self.lineEdit_7.text()

        sql = ''' SELECT adminid,password FROM admin'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        print(sql)
        for row in data:
            if adminid == row[0] and password == row[1]:
                self.statusBar().showMessage('Logged in successfully')
                self.tabWidget.setCurrentIndex(5)
                break
            else:
                self.statusBar().showMessage('Invalid adminid or password')


    def db_userpage(self):######### Done#########
        self.db = MySQLdb.connect(host='localhost', user='root', password='root', db='plotproject')
        self.cur = self.db.cursor()
        print(aadharno)
        try:
            self.cur.execute('''call userpage(%s)''',(aadharno,))
            sData = self.cur.fetchall()

            if sData:

                self.tableWidget_3.setRowCount(0)
                self.tableWidget_3.insertRow(0)

                for row, form in enumerate(sData):
                    for col, item in enumerate(form):
                        self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1

                    rowPos = self.tableWidget_3.rowCount()
                    self.tableWidget_3.insertRow(rowPos)

            else:

                self.tableWidget_3.setRowCount(0)
                self.tableWidget_3.insertRow(0)

        except:
            self.statusBar().showMessage('Unable to retrieve station data')
            self.statusBarClear()





    def db_registersite(self):      #########done########
        self.db = MySQLdb.connect(host='localhost', user='root', password='root', db='plotproject')
        self.cur = self.db.cursor()

        aadharno = self.lineEdit_8.text()  # providing aadharno
        siteno = self.lineEdit_9.text()  # providing siteno
        pincode = self.lineEdit_16.text()  # providing pincode
        today_date = datetime.date.today()

        area= self.cur.execute('''
        select area from unregisteredsites
        where siteno= %s and pincode= %s''',(siteno,pincode))
        data1 = self.cur.fetchall()
        print(data1)
        siteaddress = self.cur.execute('''
               select siteaddress from unregisteredsites
               where siteno= %s and pincode= %s''', (siteno, pincode))
        data2 = self.cur.fetchall()
        print(data2) # delete from unregistred sites###
        landmark = self.cur.execute('''
                       select landmark from unregisteredsites
                       where siteno= %s and pincode= %s''', (siteno, pincode))
        data3 = self.cur.fetchall()
        print(data3)
        googlelink = self.cur.execute('''
                       select googlelink from unregisteredsites
                       where siteno= %s and pincode= %s''', (siteno, pincode))
        data4 = self.cur.fetchall()
        print(data4)
#########################################ADDING TRIGGER##########################
        try:
            self.cur.execute('''
                                   INSERT INTO registeredsites(siteno,pincode,aadharno,date,siteaddress,area,landmark,googlelink) 
                                   VALUES (%s , %s ,%s ,%s ,%s, %s,%s,%s)
                                   ''', (siteno, pincode,aadharno,today_date,data2,data1,data3,data4))
            self.db.commit()
            print("Done 1")
            self.statusBar().showMessage('Done')
            self.statusBarClear()
            self.Open_adminpage()

        except:
            self.statusBar().showMessage('Done')






    def db_allsites(self): ########Done#######
        self.db = MySQLdb.connect(host='localhost', user='root', password='root', db='plotproject')
        self.cur = self.db.cursor()

        pincode = self.lineEdit_23.text()  # providing pincode
        ###############registred sites#########
        print("registred")
        try:
            self.cur.execute('''call allsites_reg(%s)''',(pincode,))
            sData = self.cur.fetchall()

            if sData:

                self.tableWidget_4.setRowCount(0)
                self.tableWidget_4.insertRow(0)

                for row, form in enumerate(sData):
                    for col, item in enumerate(form):
                        self.tableWidget_4.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1

                    rowPos = self.tableWidget_4.rowCount()
                    self.tableWidget_4.insertRow(rowPos)

            else:

                self.tableWidget_4.setRowCount(0)
                self.tableWidget_4.insertRow(0)

        except:
            self.statusBar().showMessage('Unable to retrieve station data')
            self.statusBarClear()

        ############unregistredSites####### ########Done#############
        print("unregistred")
        try:
            self.cur.execute('''call allsites_unreg(%s)''',(pincode,))
            sData = self.cur.fetchall()

            if sData:

                self.tableWidget_9.setRowCount(0)
                self.tableWidget_9.insertRow(0)

                for row, form in enumerate(sData):
                    for col, item in enumerate(form):
                        self.tableWidget_9.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1

                    rowPos = self.tableWidget_9.rowCount()
                    self.tableWidget_9.insertRow(rowPos)

            else:

                self.tableWidget_9.setRowCount(0)
                self.tableWidget_9.insertRow(0)

        except:
            self.statusBar().showMessage('Invaild pincode')
            self.statusBarClear()




    def db_addadmin(self):   #####  Done###
        self.db = MySQLdb.connect(host='localhost', user='root', password='root', db='plotproject')
        self.cur = self.db.cursor()

        adminid = self.lineEdit_17.text()  # providing adminid
        adminname = self.lineEdit_18.text()  # providing adminname
        password = self.lineEdit_19.text()  # providing password

        try:

            self.cur.execute('''
                        INSERT INTO admin(adminid,adminname,password) 
                        VALUES (%s , %s ,%s)
                        ''', (adminid, adminname,password))
            self.db.commit()
            self.statusBar().showMessage('Done')
            self.Open_adminpage()
        except:
            self.statusBar().showMessage('ERROR')

    def db_newsite(self):   ####  done ####
        self.db = MySQLdb.connect(host='localhost', user='root', password='root', db='plotproject')
        self.cur = self.db.cursor()

        siteno = self.lineEdit_43.text()  # providing siteno
        siteaddress = self.textEdit_2.toPlainText()  # providing siteaddress
        pincode = self.lineEdit_45.text()  # providing sitepincode
        area = self.lineEdit_46.text()  # providing sitearea
        landmark=self.lineEdit_47.text()
        googlelink=self.lineEdit_48.text()
        print(siteaddress,siteno,pincode,area)
        try:
            self.cur.execute('''
                            INSERT INTO unregisteredsites(siteno,siteaddress,pincode,area,landmark,googlelink) 
                            VALUES (%s , %s ,%s ,%s,%s,%s)
                            ''', (siteno, siteaddress, pincode, area,landmark,googlelink))
            self.db.commit()
            self.statusBar().showMessage('Done')
            self.Open_adminpage()
        except:
            self.statusBar().showMessage('Error')

    def db_adduser(self): ####### Done#####
        self.db = MySQLdb.connect(host='localhost', user='root', password='root', db='plotproject')
        self.cur = self.db.cursor()

        username = self.lineEdit_20.text()  # providing name
        aadharno = self.lineEdit_21.text()  # providing aadhar
        password = self.lineEdit_22.text()  # providing password
        owneraddress = self.textEdit.toPlainText()  # providing address
        phno = self.lineEdit_24.text()  # providing phno


        try:
            self.cur.execute('''
                                            INSERT INTO owner (aadharno,password,username,useraddress,phno) 
                                            VALUES (%s,%s,%s,%s,%s)
                                            ''', (aadharno, password, username,owneraddress, int(phno)))
            self.db.commit()
            self.statusBar().showMessage('Done')
            self.Open_homepage()
        except:
            self.statusBar().showMessage('Error')



    def db_salepage(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='root', db='plotproject')
        self.cur = self.db.cursor()
        siteno = self.lineEdit_26.text()
        pincode = self.lineEdit_27.text()
        baadhar = self.lineEdit_28.text()


        try:
            self.cur.execute('''
                                            UPDATE registeredsites 
                                            set aadharno= %s  
                                            where siteno=%s and pincode=%s
                                            ''', (baadhar, siteno, pincode))
            self.db.commit()
            self.statusBar().showMessage('Done')
            self.Open_adminpage()
        except:
            self.statusBar().showMessage('Error')

    def db_siteforsalepage(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='root', db='plotproject')
        self.cur = self.db.cursor()

        try:
            self.cur.execute('''call sitesforsale()''')
            sData = self.cur.fetchall()

            if sData:

                self.tableWidget_10.setRowCount(0)
                self.tableWidget_10.insertRow(0)

                for row, form in enumerate(sData):
                    for col, item in enumerate(form):
                        self.tableWidget_10.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1

                    rowPos = self.tableWidget_10.rowCount()
                    self.tableWidget_10.insertRow(rowPos)

            else:

                self.tableWidget_10.setRowCount(0)
                self.tableWidget_10.insertRow(0)

        except:
            self.statusBar().showMessage('Unable to retrieve station data')
            self.statusBarClear()



    #######################THEMES#########
    def dark_bluethemes(self):
        style=open('themes/default.css','r')
        style=style.read()
        self.setStyleSheet(style)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
