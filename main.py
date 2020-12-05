import sys
from PyQt5 import *
from PyQt5.QtWidgets import QAction,QDialog, QTableWidget, QTableWidgetItem, QLineEdit, QRadioButton, QLabel,QMenuBar,QMessageBox, QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QMainWindow, QTextEdit, QCheckBox, QFileDialog, QInputDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import QFileInfo
from PyQt5 import QtGui, QtWidgets, QtPrintSupport

import csv
import os


class Form(QWidget):

    def __init__(self):

        super().__init__()
        self.setGeometry(50, 50, 500, 500)
        self.Glayout = QGridLayout()
        self.getItems()
        self.setLayout(self.Glayout)
        self.setWindowTitle("Soru Bankası")
        self.tabloPath=""
        self.yenisorueklesayfa=YeniSoruEkle()
        self.sorusecsayfa=SoruSec()


    def getItems(self):
        self.menubar = QMenuBar(self)

        actionFile = self.menubar.addMenu("işlem")
        soruekle=QAction(self)
        soruekle.triggered.connect(self.soruEkleSayfasinaGec)
        soruekle.setText("soru ekle")
        soruSec=QAction(self)
        soruSec.setText("soru seç")
        soruSec.triggered.connect(self.soruSecSayfasinaGec)

        actionFile.addAction(soruekle)
        actionFile.addAction(soruSec)
        
        actionFile.addSeparator()

        self.menubar.show()
    def soruEkleSayfasinaGec(self):
        self.yenisorueklesayfa.show()
        form1.close()

    def soruSecSayfasinaGec(self):

        self.sorusecsayfa.show()
        form1.close()
            
        

class YeniSoruEkle(QWidget):

    def __init__(self):

        super().__init__()
        self.setGeometry(50, 50, 500, 500)
        self.Glayout = QGridLayout()
        self.getItems()
        self.setLayout(self.Glayout)
        self.setWindowTitle("Yeni Soru Ekle")
        self.dogriCevap = ""

    def getItems(self):
        sorulbl = QLabel()
        sorulbl.setText("Soru:")

        dogrusıklbl = QLabel()
        dogrusıklbl.setText("Doğru şık")

        birincisık = QRadioButton()
        birincisık.setText("1.")
        birincisık.clicked.connect(self.birincisik_Clicked)

        ikincisık = QRadioButton()
        ikincisık.setText("2.")
        ikincisık.clicked.connect(self.ikincisik_Clicked)

        ücüncüsık = QRadioButton()
        ücüncüsık.setText("3.")
        ücüncüsık.clicked.connect(self.ucuncusik_Clicked)

        dördüncüsık = QRadioButton()
        dördüncüsık.setText("4.")
        dördüncüsık.clicked.connect(self.dorduncusik_Clicked)

        besincisık = QRadioButton()
        besincisık.setText("5.")
        besincisık.clicked.connect(self.besinicisik_Clicked)

        self.soruMetin = QTextEdit()

        self.cevap1 = QLineEdit()
        self.cevap2 = QLineEdit()
        self.cevap3 = QLineEdit()
        self.cevap4 = QLineEdit()
        self.cevap5 = QLineEdit()

        soruBankasınaEklebtn = QPushButton()
        soruBankasınaEklebtn.setText("Soru bankasına ekle")
        soruBankasınaEklebtn.clicked.connect(self.soruBankasinaEklebtn_Clicked)

        basliklar = ['soru', '1.seçenek', '2.seçenek',
                     '3.seçenek', '4.seçenek', '5.seçenek', 'cevap']
        self.tablo = QTableWidget(self)
        self.tablo.setColumnCount(7)

        self.tablo.setHorizontalHeaderLabels(basliklar)

        soruBankasınıExcelOlarakKaydetbtn = QPushButton()
        soruBankasınıExcelOlarakKaydetbtn.setText(
            "soru bankasını excel olarak kaydet")
        soruBankasınıExcelOlarakKaydetbtn.clicked.connect(
            self.soruBankasiniExcelOlarakKaydet_Clicked)
        self.Glayout.addWidget(sorulbl, 0, 0)
        self.Glayout.addWidget(self.soruMetin, 0, 2)
        self.Glayout.addWidget(dogrusıklbl, 1, 1)
        self.Glayout.addWidget(birincisık, 2, 1)
        self.Glayout.addWidget(ikincisık, 3, 1)
        self.Glayout.addWidget(ücüncüsık, 4, 1)
        self.Glayout.addWidget(dördüncüsık, 5, 1)
        self.Glayout.addWidget(besincisık, 6, 1)

        self.Glayout.addWidget(self.cevap1, 2, 2)
        self.Glayout.addWidget(self.cevap2, 3, 2)
        self.Glayout.addWidget(self.cevap3, 4, 2)
        self.Glayout.addWidget(self.cevap4, 5, 2)
        self.Glayout.addWidget(self.cevap5, 6, 2)
        self.Glayout.addWidget(soruBankasınaEklebtn, 7, 2)
        self.Glayout.addWidget(self.tablo, 0, 3)
        self.Glayout.addWidget(soruBankasınıExcelOlarakKaydetbtn, 1, 3)

    def soruBankasiniExcelOlarakKaydet_Clicked(self):

        path = QFileDialog.getSaveFileName(
            self, 'Save xls', os.getenv('HOME'), 'XLS(*.xls)')

        if path[0] != '':

            with open(path[0], 'w') as csv_file:

                writer = csv.writer(csv_file, dialect='excel')
                for row in range(self.tablo.rowCount()):

                    row_data = []
                    for column in range(self.tablo.columnCount()):
                        item = self.tablo.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)

    def birincisik_Clicked(self):

        self.dogriCevap = "1."

    def ikincisik_Clicked(self):

        self.dogriCevap = "2."

    def ucuncusik_Clicked(self):

        self.dogriCevap = "3."

    def dorduncusik_Clicked(self):

        self.dogriCevap = "4."

    def besinicisik_Clicked(self):

        self.dogriCevap = "5."

    def soruBankasinaEklebtn_Clicked(self):

        self.soruMetini = self.soruMetin.toPlainText()

        self.birinci = self.cevap1.text()
        self.ikinci = self.cevap2.text()
        self.ucuncu = self.cevap3.text()
        self.dorduncu = self.cevap4.text()
        self.besinci = self.cevap5.text()

        elemanlar = [self.soruMetini, self.birinci, self.ikinci,
                     self.ucuncu, self.dorduncu, self.besinci, self.dogriCevap]

        self.satirSayisi = self.tablo.rowCount()
        self.tablo.insertRow(self.satirSayisi)
        self.Item1 = QTableWidgetItem(elemanlar[0])
        self.Item2 = QTableWidgetItem(elemanlar[1])
        self.Item3 = QTableWidgetItem(elemanlar[2])
        self.Item4 = QTableWidgetItem(elemanlar[3])
        self.Item5 = QTableWidgetItem(elemanlar[4])
        self.Item6 = QTableWidgetItem(elemanlar[5])
        self.Item7 = QTableWidgetItem(elemanlar[6])

        self.tablo.setItem(self.satirSayisi, 0, self.Item1)
        self.tablo.setItem(self.satirSayisi, 1, self.Item2)
        self.tablo.setItem(self.satirSayisi, 2, self.Item3)
        self.tablo.setItem(self.satirSayisi, 3, self.Item4)
        self.tablo.setItem(self.satirSayisi, 4, self.Item5)
        self.tablo.setItem(self.satirSayisi, 5, self.Item6)
        self.tablo.setItem(self.satirSayisi, 6, self.Item7)


class SoruSec(QWidget):

    def __init__(self):

        super().__init__()
        self.setGeometry(50, 50, 500, 500)
        self.Glayout = QGridLayout()
        self.getItems()
        self.setLayout(self.Glayout)
        self.setWindowTitle("Soru bankasından soru Seç")

    def getItems(self):
        self.tablo = QTableWidget(self)
        basliklar = ['soru', '1.seçenek', '2.seçenek',
                     '3.seçenek', '4.seçenek', '5.seçenek', 'cevap']
        self.tablo.setColumnCount(7)

        self.tablo.setHorizontalHeaderLabels(basliklar)

        yazdırılacakSoruDosyasiniSecbtn = QPushButton()
        yazdırılacakSoruDosyasiniSecbtn.setText(
            "yazdırılacak soru bankasına ait dosyayı seç")
        yazdırılacakSoruDosyasiniSecbtn.clicked.connect(
            self.dosyayiSec_Clicked)

        yazdırbtn = QPushButton()
        yazdırbtn.setText("yazdır")
        yazdırbtn.clicked.connect(self.yazdirbtn_Clicked)

        self.Glayout.addWidget(self.tablo, 1, 1, 1, 2)
        self.Glayout.addWidget(yazdırılacakSoruDosyasiniSecbtn, 2, 1)
        self.Glayout.addWidget(yazdırbtn, 2, 2)

  

    def yazdirbtn_Clicked(self):

        dialog = QtPrintSupport.QPrintDialog()
        
        dialog.exec_()
        self.pdfYazdirEkrani()
    
            

    def dosyayiSec_Clicked(self):

        self.check_change = False
        path = QFileDialog.getOpenFileName(
            self, 'Open xls', os.getenv('HOME'), 'XLS(*.xls)')
        self.tabloPath=path    
        if path[0] != '':
            with open(path[0], newline='') as csv_file:
                self.tablo.setRowCount(0)
                self.tablo.setColumnCount(7)
                my_file = csv.reader(csv_file, delimiter=',', quotechar='|')
                for row_data in my_file:
                    row = self.tablo.rowCount()
                    self.tablo.insertRow(row)
                    if len(row_data) > 7:
                        self.tablo.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.tablo.setItem(row, column, item)
        self.check_change = True




app = QApplication(sys.argv)

form1 =Form()
form1.show()

sys.exit(app.exec_())

