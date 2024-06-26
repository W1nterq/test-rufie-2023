#тут будут 3 класса, для каждого окна
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTime, QTimer

from final_win import *

from instr import *

class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.set_ui()
        #self.connects()

    def set_appear(self):
        self.setStyleSheet('font-size:24px; margin:10px')
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)

    def test_1(self):
        self.time = self.time.addSecs(-1)
        self.timer_label.setText(self.time.toString('mm:ss'))
        if self.time.second() == 0:
            self.timer.stop()
            self.timer_label.setText('этап 1 закончен')

    def start_timer_1(self): #запускаем таймер 1
        self.timer = QTimer()
        self.time = QTime(0,0,15)
        self.timer.start(1000) #1000 милисекунд = раз в 1 нормальную секунду
        self.timer.timeout.connect(self.test_1)       #запускается метод test

    def test_2(self): #обновить таймер с приседаниями
        self.time = self.time.addSecs(-1)
        self.timer_label.setText('осталось присесть ' + self.time.toString('ss') + " раз")
        if self.time.second() == 0:
            self.timer.stop()
            self.timer_label.setText('хватит приседать')

    def start_timer_2(self): #запускаем таймер на приседания
        self.timer = QTimer()
        self.time = QTime(0,0,45)
        self.timer.start(1500) #1500 милисекунд = каждую 1.5 нормальную секунду
        self.timer.timeout.connect(self.test_2)       #запускается метод test

    def test_3(self): #будет запускаться раз в секунду
        self.time = self.time.addSecs(-1)
        self.timer_label.setText(self.time.toString('mm:ss'))

        if self.time.second() >= 45: self.timer_label.setStyleSheet('color:green')
        elif self.time.second() >= 15: self.timer_label.setStyleSheet('color:black')
        else: self.timer_label.setStyleSheet('color:green')

        if self.time.second() == 0:
            self.timer.stop()
            self.timer_label.setText('тест закончен, переходите к результатам')

    def start_timer_3(self): #запускаем таймер 3
        self.timer = QTimer()
        self.time = QTime(0,1,0)
        self.timer.start(1000) #1000 милисекунд = раз в 1 нормальную секунду
        self.timer.timeout.connect(self.test_3) 

    def show_final_win(self):
        self.win = FinalWin(age = int(self.age_input.text()),
                            p1 = int(self.puls1_input.text()),
                            p2 = int(self.puls2_input.text()),
                            p3 = int(self.puls3_input.text()))
        self.win.show()
        self.hide()

    def set_ui(self):
        self.timer_label = QLabel('00:00:15')

        fio_label = QLabel(txt_name)
        fio_input = QLineEdit()
        age_label = QLabel(txt_hintage)
        self.age_input = QLineEdit()
        instr1 = QLabel(txt_test1)
        start1_btn = QPushButton(txt_starttest1)

        #тут функция чтобы запустить отчет таймера
        start1_btn.clicked.connect(self.start_timer_1) 

        self.puls1_input = QLineEdit()
        instr2 = QLabel(txt_test2)
        start2_btn = QPushButton(txt_starttest2)
        start2_btn.clicked.connect(self.start_timer_2)

        instr3 = QLabel(txt_test3)
        start3_btn = QPushButton(txt_starttest3)
        start3_btn.clicked.connect(self.start_timer_3)

        self.puls2_input = QLineEdit()
        self.puls3_input = QLineEdit()

        final_btn = QPushButton(txt_sendresults)
        final_btn.clicked.connect(self.show_final_win)

        line1 = QVBoxLayout()
        line2 = QVBoxLayout()
        line3 = QVBoxLayout()
        line4 = QHBoxLayout()

        line = QVBoxLayout()
        line.addWidget(self.timer_label)
        line.addWidget(fio_label)
        line.addWidget(fio_input)
        line.addWidget(age_label)
        line.addWidget(self.age_input)
        line.addLayout(line4)

        line1.addWidget(instr1)
        line1.addWidget(start1_btn)
        line1.addWidget(self.puls1_input)
        line4.addLayout(line1)

        line2.addWidget(instr2)
        line2.addWidget(start2_btn)
        line4.addLayout(line2)

        line3.addWidget(instr3)
        line3.addWidget(start3_btn)
        line3.addWidget(QLabel('Впишите пульс после приседаний'))
        line3.addWidget(self.puls2_input)
        line3.addWidget(QLabel('Впишите пульс после отдыха'))
        line3.addWidget(self.puls3_input)
        line4.addLayout(line3)

        line.addWidget(final_btn)
        self.setLayout(line)