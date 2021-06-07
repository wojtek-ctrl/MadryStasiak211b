import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from testy import get_test

class Ui_MainWindow2(object):
    def __init__(self, MW1):
        super().__init__()
        self.MainWindow = MW1

    def setupUi(self, MainWindow2):
        self.id = 0
        self.pytanie = get_test()
        MainWindow2.setObjectName("MainWindow")
        MainWindow2.resize(867, 673)
        MainWindow2.setStyleSheet("background-color: rgb(180, 226, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.Label_Wynik = QtWidgets.QLabel(self.centralwidget)
        self.Label_Wynik.setGeometry(QtCore.QRect(0, 80, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Wynik.setFont(font)
        self.Label_Wynik.setStyleSheet("")
        self.Label_Wynik.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Wynik.setObjectName("Label_Wynik")
        self.Label_Najlepszy_Kursant = QtWidgets.QLabel(self.centralwidget)
        self.Label_Najlepszy_Kursant.setGeometry(QtCore.QRect(180, 0, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Najlepszy_Kursant.setFont(font)
        self.Label_Najlepszy_Kursant.setAutoFillBackground(False)
        self.Label_Najlepszy_Kursant.setStyleSheet("background-color: rgb(239, 239, 239)")
        self.Label_Najlepszy_Kursant.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Najlepszy_Kursant.setObjectName("Label_Najlepszy_Kursant")
        self.Label_Panel_Kursanta = QtWidgets.QLabel(self.centralwidget)
        self.Label_Panel_Kursanta.setGeometry(QtCore.QRect(180, 40, 501, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Panel_Kursanta.setFont(font)
        self.Label_Panel_Kursanta.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Label_Panel_Kursanta.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Panel_Kursanta.setObjectName("Label_Panel_Kursanta")
        self.Label_Nr_Pytania = QtWidgets.QLabel(self.centralwidget)
        self.Label_Nr_Pytania.setGeometry(QtCore.QRect(180, 110, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.Label_Nr_Pytania.setFont(font)
        self.Label_Nr_Pytania.setStyleSheet("background-color: rgb(231, 231, 231);")
        self.Label_Nr_Pytania.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Nr_Pytania.setObjectName("Label_Nr_Pytania")
        self.Label_Biala_Ramka = QtWidgets.QLabel(self.centralwidget)
        self.Label_Biala_Ramka.setGeometry(QtCore.QRect(180, 160, 501, 441))
        self.Label_Biala_Ramka.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Label_Biala_Ramka.setText("")
        self.Label_Biala_Ramka.setObjectName("Label_Biala_Ramka")
        self.RBtn_Odp1 = QtWidgets.QRadioButton(self.centralwidget)
        self.RBtn_Odp1.setGeometry(QtCore.QRect(220, 280, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.RBtn_Odp1.setFont(font)
        self.RBtn_Odp1.setObjectName("RBtn_Odp1")
        self.RBtn_Odp2 = QtWidgets.QRadioButton(self.centralwidget)
        self.RBtn_Odp2.setGeometry(QtCore.QRect(220, 340, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.RBtn_Odp2.setFont(font)
        self.RBtn_Odp2.setObjectName("RBtn_Odp2")
        self.RBtn_Odp3 = QtWidgets.QRadioButton(self.centralwidget)
        self.RBtn_Odp3.setGeometry(QtCore.QRect(220, 400, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.RBtn_Odp3.setFont(font)
        self.RBtn_Odp3.setObjectName("RBtn_Odp3")
        self.Label_Tresc_Pytania = QtWidgets.QLabel(self.centralwidget)
        self.Label_Tresc_Pytania.setGeometry(QtCore.QRect(220, 180, 431, 91))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Label_Tresc_Pytania.setFont(font)
        self.Label_Tresc_Pytania.setStyleSheet("background-color: rgb(231, 231, 231);")
        self.Label_Tresc_Pytania.setObjectName("Label_Tresc_Pytania")
        self.Btn_Zatwierdz = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Zatwierdz.setGeometry(QtCore.QRect(220, 520, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Btn_Zatwierdz.setFont(font)
        self.Btn_Zatwierdz.setStyleSheet("background-color: rgb(80, 170, 255);")
        self.Btn_Zatwierdz.setObjectName("Btn_Zatwierdz")
        self.Btn_Przerwij_Test = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Przerwij_Test.setGeometry(QtCore.QRect(450, 520, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Btn_Przerwij_Test.setFont(font)
        self.Btn_Przerwij_Test.setStyleSheet("background-color: rgb(80, 170, 255);")
        self.Btn_Przerwij_Test.setObjectName("Btn_Przerwij_Test")
        self.Label_Kolor = QtWidgets.QLabel(self.centralwidget)
        self.Label_Kolor.setGeometry(QtCore.QRect(220, 460, 431, 51))
        self.Label_Kolor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Label_Kolor.setText("")
        self.Label_Kolor.setObjectName("Label_Kolor")
        self.Label_Kolor.setAlignment(QtCore.Qt.AlignCenter)
        MainWindow2.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 26))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)
        self.HiddedRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.HiddedRadioButton.setObjectName("HiddedRadioButton")
        self.HiddedRadioButton.setVisible(0)
        self.HiddedRadioButton.setEnabled(0)
        self.Btn_Zatwierdz.clicked.connect(self.zmiana)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)
        
        
        
    def odswiez_pytanie(self):
        pyt = self.pytanie.get_pytanie(self.id)
        odp = pyt.get_odpowiedzi()
        _translate = QtCore.QCoreApplication.translate
        self.HiddedRadioButton.setChecked(True)
        self.RBtn_Odp1.setText(_translate("MainWindow", odp[0]))
        self.RBtn_Odp2.setText(_translate("MainWindow", odp[1]))
        self.RBtn_Odp3.setText(_translate("MainWindow", odp[2]))
        self.Label_Tresc_Pytania.setText(_translate("MainWindow", pyt.get_pytanie()))
        self.Btn_Zatwierdz.setText(_translate("MainWindow", "Zatwierdz"))
        self.Label_Nr_Pytania.setText(_translate("MainWindow","Pytanie numer " +str(self.id+1)))
        self.Label_Kolor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Label_Kolor.setText(_translate("MainWindow", ""))

    def koniec_testu(self):
        _translate = QtCore.QCoreApplication.translate
        self.Label_Nr_Pytania.setText(_translate("MainWindow", "Koniec testu!"))
        self.Label_Tresc_Pytania.setText(_translate("MainWindow", "Twój wynik to: "+str(self.pytanie.get_wynik())+"/100!"))
        self.RBtn_Odp1.hide()
        self.RBtn_Odp2.hide()
        self.RBtn_Odp3.hide()
        self.Label_Kolor.hide()
        self.Btn_Przerwij_Test.setText(_translate("MainWindow", "KONIEC"))
        self.Btn_Zatwierdz.setDisabled(True)

    def zaladuj_nastepne_pytanie(self):
        self.id += 1
        if self.id >= self.pytanie.ilosc_pytan():
            self.koniec_testu()
            return 0
        self.odswiez_pytanie()
        self.Btn_Zatwierdz.setEnabled(1)

    def zmiana(self):
        if self.id >= self.pytanie.ilosc_pytan():
            return 0

        _translate = QtCore.QCoreApplication.translate

        pyt = self.pytanie.get_pytanie(self.id)
        if self.RBtn_Odp1.isChecked() == True:
            x = self.RBtn_Odp1.text()
        elif self.RBtn_Odp2.isChecked() == True:
            x = self.RBtn_Odp2.text()
        elif self.RBtn_Odp3.isChecked() == True:
            x = self.RBtn_Odp3.text()
        else:
            self.Label_Kolor.setText("Zaznacz odpowiedz !")
            return 0


        wynik = self.pytanie.sprawdz_odpowiedz(self.id, x)

        self.Label_Wynik.setText(_translate("MainWindow", "Wynik: " + str(self.pytanie.get_wynik()) + "/100"))

        if wynik == True:
            self.Label_Kolor.setStyleSheet("background-color: rgb(123, 232, 8);")
            self.Label_Kolor.setText(_translate("MainWindow", "POPRAWNA ODPOWIEDŹ!"))
        else:
            self.Label_Kolor.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.Label_Kolor.setText(_translate("MainWindow", "BŁĘDNA ODPOWIEDŹ!"))
        self.Btn_Zatwierdz.setEnabled(0)
        timer = QTimer()
        timer.singleShot(1000,self.zaladuj_nastepne_pytanie)
        
        

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow", "Egzamin Teoretyczny"))
        self.Label_Wynik.setText(_translate("MainWindow", "Wynik: " + str(self.pytanie.get_wynik()) +"/100"))
        self.Label_Najlepszy_Kursant.setText(_translate("MainWindow", "NAJLEPSZY KURSANT"))
        self.Label_Panel_Kursanta.setText(_translate("MainWindow", "PRÓBNY EGZAMIN TEORETYCZNY"))
        self.Btn_Zatwierdz.setText(_translate("MainWindow", "Zatwierdz"))
        self.Btn_Przerwij_Test.setText(_translate("MainWindow", "Przerwij test"))
        self.Btn_Przerwij_Test.clicked.connect(lambda:self.close_panel_egzaminu(MainWindow2))
        self.odswiez_pytanie()

    def close_panel_egzaminu(self,MainWindow2):
        self.MainWindow.show()
        MainWindow2.close()


