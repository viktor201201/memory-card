from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QWidget, QRadioButton, QLabel, QPushButton, QGroupBox, QButtonGroup
from random import shuffle, randint

app = QApplication([])
win = QWidget()
win.resize(300, 200)
win.setWindowTitle('Memory Card')
label1 = QLabel('вопрос')
label2 = QLabel('a')
label3 = QLabel('d')
rbtn1 = QRadioButton('вар. 1')
rbtn2 = QRadioButton('вар. 2')
rbtn3 = QRadioButton('вар. 3')
rbtn4 = QRadioButton('вар. 4')
answers = [rbtn1, rbtn2, rbtn3, rbtn4]
pbtn = QPushButton('Ответить')
gbox1 = QGroupBox('Варианты')
gbox2 = QGroupBox('Результат теста')
hl = QHBoxLayout()
vl1 = QVBoxLayout()
vl2 = QVBoxLayout()
vl3 = QVBoxLayout()
wvl = QVBoxLayout()
whl1 = QHBoxLayout()
whl2 = QHBoxLayout()
whl3 = QHBoxLayout()

rgr = QButtonGroup()
rgr.addButton(rbtn1)
rgr.addButton(rbtn2)
rgr.addButton(rbtn3)
rgr.addButton(rbtn4)

vl1.addWidget(rbtn1)
vl1.addWidget(rbtn2)
vl2.addWidget(rbtn3)
vl2.addWidget(rbtn4)
vl3.addWidget(label2)
vl3.addWidget(label3, alignment=Qt.AlignHCenter)
hl.addLayout(vl1)
hl.addLayout(vl2)
gbox1.setLayout(hl)
gbox2.setLayout(vl3)
whl1.addWidget(label1, alignment=Qt.AlignCenter)
whl2.addWidget(gbox1)
whl2.addWidget(gbox2)
whl3.addStretch(1)
whl3.addWidget(pbtn, stretch=2)
whl3.addStretch(1)
gbox2.hide()
wvl.addLayout(whl1, stretch=2)
wvl.addLayout(whl2, stretch=8)
wvl.addLayout(whl3, stretch=2)
wvl.setSpacing(12)
win.setLayout(wvl)

win.q = 0
win.ra = 0

def sq():
    pbtn.setText('Ответить')
    gbox1.show()
    gbox2.hide()

def sr():
    pbtn.setText('Следующий вопрос')
    rgr.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    rgr.setExclusive(True)
    gbox1.hide()
    gbox2.show()

class Question():
    def __init__(self, question, ra, wr1, wr2, wr3):
        self.question = question
        self.ra = ra
        self.wr1 = wr1
        self.wr2 = wr2
        self.wr3 = wr3

def ask(question):
    shuffle(answers)
    label1.setText(question.question)
    answers[0].setText(question.ra)
    answers[1].setText(question.wr1)
    answers[2].setText(question.wr2)
    answers[3].setText(question.wr3)
    label3.setText(question.ra)
    sq()

def ca():
    if answers[0].isChecked():
        label2.setText('Правильно!')
        win.ra += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            label2.setText('Неправильно :(')
    print(f'Всего вопросов: {win.q} \nПравильных ответов: {win.ra} \nРейнтинг: {win.ra / win.q * 100}')
    sr()

def next_q():
    win.q += 1
    cur_q = randint(0, len(ql)-1)
    a = ql[cur_q]
    ask(a)

def pushbtn():
    if pbtn.text() == 'Ответить':
        ca()
    elif pbtn.text() == 'Следующий вопрос':
        next_q()

ql = []
ql.append(
    Question('Какой язык самый простой', 'Английский', 'Португальский', 'Немецкий', 'Китайский')
)
ql.append(
    Question('Какой язык сложный?', 'Китайский', 'Русский', 'Немецкий', 'Казахский' )
)
ql.append(
    Question('Какая страна мира  является самой населённой?', 'Китай', 'Япония', 'Россия', 'Индия')
)
ql.append(
    Question('Самая многонациональная страна мира', 'Индия', 'Россия', 'США', 'Германия')
)
ql.append(
    Question('Какие народы относят к восточным славянам?', 'Русские, украинцы, белорусы', 'Болгары, Сербы, Хорвата, Македонцы', 'Поляки, Чехи, Словаки', ' ')
)
ql.append(
    Question('Какую религию исповедуют большинство славян?', 'Христианство', 'Буддизм', 'Иудаизм', 'Ислам')
)
next_q()

pbtn.clicked.connect(pushbtn)
win.show()
app.exec_()
