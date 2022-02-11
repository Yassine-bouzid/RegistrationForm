

from PyQt5 import QtCore, QtGui, QtWidgets
import re

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1144, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 722, 541))
        self.tableWidget.setAccessibleName("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(6,150)
        

     

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)        
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(740, 20, 371, 531))
        self.label.setStyleSheet("background-color:white\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.test_info=True### that may be changes
        self.pushButton.setEnabled(self.test_info)####      enabled it when all info becomes True
        self.pushButton.setGeometry(QtCore.QRect(871, 505, 131, 41))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_nom = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nom.setGeometry(QtCore.QRect(897, 50, 121, 27))
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        self.lineEdit_prenom = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_prenom.setGeometry(QtCore.QRect(880, 105, 181, 27))
        self.lineEdit_prenom.setObjectName("lineEdit_prenom")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(940, 160, 125, 28))
        self.dateEdit.setMaximumDate(QtCore.QDate(2002, 12, 31))
        self.dateEdit.setMinimumDate(QtCore.QDate(1930, 1, 14))
        self.dateEdit.setDate(QtCore.QDate(2001, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat("yyyy/MM/dd")
        self.lineEdit_2eme = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2eme.setGeometry(QtCore.QRect(960, 260, 51, 27))
        self.lineEdit_2eme.setObjectName("lineEdit_2eme")
        ##############################
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(917, 210, 171, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.miad = QtWidgets.QComboBox(self.centralwidget)
        self.miad.setGeometry(QtCore.QRect(900, 390, 171, 27))
        self.miad.setObjectName("miad_box")
        self.miad.addItem("")
        self.miad.addItem("")
        self.miad.addItem("")
        #self.miad.removeItem(1)######    how    #########################

        self.msir = QtWidgets.QComboBox(self.centralwidget)
        self.msir.setGeometry(QtCore.QRect(900, 418, 171, 27))
        self.msir.setObjectName("msir_box")
        self.msir.addItem("")
        self.msir.addItem("")
        self.msir.addItem("")

        self.msia = QtWidgets.QComboBox(self.centralwidget)
        self.msia.setGeometry(QtCore.QRect(900, 448, 171, 27))
        self.msia.setObjectName("msia_box")
        self.msia.addItem("")
        self.msia.addItem("")
        self.msia.addItem("")

        self.lineEdit_3eme = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3eme.setGeometry(QtCore.QRect(960, 310, 51, 27))
        self.lineEdit_3eme.setObjectName("lineEdit_3eme")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(848, 53, 41, 19))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(798, 108, 61, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(776, 163, 161, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(752, 213, 161, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(778, 263, 171, 19))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(777, 313, 171, 19))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(790, 360, 271, 20))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(840, 395, 79, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(840, 453, 79, 19))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(840, 423, 79, 19))
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1015, 264, 79, 19))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1015, 314, 79, 19))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(800, 80, 301, 20))
        self.label_14.setStyleSheet("font: 9pt \"DejaVu Sans\";\n"
"color:red\n"
"")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(800, 130, 301, 20))
        self.label_15.setStyleSheet("font: 9pt \"DejaVu Sans\";\n"
"color:red\n"
"")
        self.label_15.setObjectName("label_15")

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(800, 475, 301, 20))
        self.label_16.setStyleSheet("font: 9pt \"DejaVu Sans\";\n"
"color:red\n"
"")
        self.label_16.setObjectName("label_16")
        self.label_16.setStyleSheet("color:red;font:9pt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1144, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #item = self.tableWidget.verticalHeaderItem(0)
        #item.setText(_translate("MainWindow", "1"))



################# FIXEE ######
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Prenom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date .N"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Diplome"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Moy 2LMI"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Moy 3LMI"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Choix .M"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Moy .G"))
##################  FIXEE #######
       
        

        ################################################################################# table
        self.pushButton.setText(_translate("MainWindow", "submit"))
        self.pushButton.clicked.connect(self.check_all)
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))

        self.miad.setItemText(0, _translate("MainWindow", "MIAD"))
        self.miad.setItemText(1, _translate("MainWindow", "MSIR"))
        self.miad.setItemText(2, _translate("MainWindow", "MSIA"))

        self.msir.setItemText(0, _translate("MainWindow", "MIAD"))
        self.msir.setItemText(1, _translate("MainWindow", "MSIR"))
        self.msir.setItemText(2, _translate("MainWindow", "MSIA"))

        self.msia.setItemText(0, _translate("MainWindow", "MIAD"))
        self.msia.setItemText(1, _translate("MainWindow", "MSIR"))
        self.msia.setItemText(2, _translate("MainWindow", "MSIA"))


        self.label_2.setText(_translate("MainWindow", "nom"))
        self.label_3.setText(_translate("MainWindow", "prenom"))
        self.label_4.setText(_translate("MainWindow", "Date de naissance"))
        self.label_5.setText(_translate("MainWindow", "Intitule de diplome"))
        self.label_6.setText(_translate("MainWindow", "Moyenne 2eme anne"))
        self.label_7.setText(_translate("MainWindow", "Moyenne 3eme anne"))
        self.label_8.setText(_translate("MainWindow", "Choisir en fonction de la priorité :"))

        self.label_9.setText(_translate("MainWindow", "1"))
        self.label_10.setText(_translate("MainWindow", "3"))
        self.label_11.setText(_translate("MainWindow", "2"))

        self.label_12.setText(_translate("MainWindow", "/20"))
        self.label_13.setText(_translate("MainWindow", "/20"))
        self.nom_error= ""####
        self.label_14.setText(_translate("MainWindow",self.nom_error))
        self.prenom_error= ""####
        self.label_15.setText(_translate("MainWindow",self.prenom_error))
        self.label_16.setText(_translate("MainWindow",""))


        

              


         
    def check_all(self):
        
        n=0
       ## check the name 
        resault_nom=re.fullmatch(r'[A-Za-z ]{1,}',self.lineEdit_nom.text()) 

        if not resault_nom:
             self.label_14.setText("nom contains alphabet only(A-Z and a-z)")
        else:
             self.label_14.setText("")
             self.Nom=self.lineEdit_nom.text()
             print(self.Nom)
             
             
  
              
              
        resault_prenom=re.fullmatch(r'[A-Za-z ]{1,}',self.lineEdit_prenom.text()) 

       ## check the familyname
        if not resault_prenom:
             self.label_15.setText("prenom contains alphabet only(A-Z and a-z)")
        else:
             self.label_15.setText("")
             self.Prenom=self.lineEdit_prenom.text()
             print(self.Prenom)
    
      ## check for moyene
        resault_moy2=re.fullmatch(r'[0-1]?[0-9]?|20',self.lineEdit_2eme.text())
        resault_moy3=re.fullmatch(r'[0-1]?[0-9]?|20',self.lineEdit_3eme.text())

        if not resault_moy2:
                self.label_6.setStyleSheet("color:red")
                self.label_12.setStyleSheet("color:red")
                
        else:
                self.label_6.setStyleSheet("color:black")
                self.label_12.setStyleSheet("color:black")
                self.Moy2=self.lineEdit_2eme.text()
                print(self.Moy2)
                

        if not resault_moy3:
                self.label_7.setStyleSheet("color:red")
                self.label_13.setStyleSheet("color:red")
                
        else:
                self.label_7.setStyleSheet("color:black")
                self.label_13.setStyleSheet("color:black")
                self.Moy3=self.lineEdit_3eme.text()
                print(self.Moy3)
                
                self.Diplome=self.comboBox.currentText()
                print("Diplome"+self.Diplome)
                
        self.Choix1=self.miad.currentText()
        self.Choix2=self.msir.currentText()
        self.Choix3=self.msia.currentText()   
        self.choixBool=True
        if self.Choix1.__eq__(self.Choix2) or self.Choix1.__eq__(self.Choix3):
                self.choixBool=False
                self.label_16.setText("each major shoud have diferent periority")  
        if self.Choix2.__eq__(self.Choix1) or self.Choix2.__eq__(self.Choix3):  
                self.choixBool=False
                self.label_16.setText("each major shoud have diferent periority")
        if  self.Choix3.__eq__(self.Choix1) or self.Choix3.__eq__(self.Choix2):  
                self.choixBool=False
                self.label_16.setText("each major shoud have diferent periority")                  
        
        
        if resault_moy3 and resault_moy2 and resault_prenom and resault_nom and self.choixBool:
                self.tableWidget.insertRow(0)
                self.tableWidget.setItem(0 , 3,QtWidgets.QTableWidgetItem(self.Diplome))
                self.tableWidget.setItem(0 , 4,QtWidgets.QTableWidgetItem(self.Moy2))
                self.tableWidget.setItem(0 , 1,QtWidgets.QTableWidgetItem(self.Prenom))
                self.tableWidget.setItem(0 , 2,QtWidgets.QTableWidgetItem(self.dateEdit.text())) 
                self.tableWidget.setItem(0 , 0,QtWidgets.QTableWidgetItem(self.Nom))
                self.tableWidget.setItem(0 , 5,QtWidgets.QTableWidgetItem(self.Moy3))
                self.tableWidget.setItem(0 , 6,QtWidgets.QTableWidgetItem("1."+self.Choix1+"\n"+"2."+self.Choix2+"\n"+"3."+self.Choix3))
                self.tableWidget.setItem(0 , 7,QtWidgets.QTableWidgetItem(str((float(self.Moy2)+float(self.Moy3))/2)))
                self.tableWidget.insertRow(0)
                self.label_16.setText("")

                                      
     

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
