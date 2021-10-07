import sys
import threading

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, \
    QFileDialog, QMessageBox
import subprocess
file_name = " "
pcd_name = " "
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def add_open(self):
        FileOpen = QFileDialog.getOpenFileName(self, 'Open file', './')
        self.label1.setText(FileOpen[0])
        global file_name
        _file_name = FileOpen[0].split('/')[-1].split('.')[0]
        file_name = _file_name
        self.file_directory = FileOpen[0]
        print("input: "+file_name+" and "+self.file_directory)

    def map_add_open(self):
        FileOpen = QFileDialog.getOpenFileName(self, 'Open file', './')
        self.label2.setText(FileOpen[0])
        global pcd_name
        pcd_name = FileOpen[0]
        print("pcd file set to : "+ pcd_name)

    def map_sh(self):
        global file_name
        if(file_name == " "):
            QMessageBox.question(self, 'Message', "bag 파일을 입력해주세요.", QMessageBox.Yes)
        else:
            subprocess.call('./example.sh '+self.file_directory+' '+file_name, shell=True)

    def view_sh(self):
        global pcd_name
        if(pcd_name == " "):
            QMessageBox.question(self, 'Message', "pcd 파일을 입력해주세요.", QMessageBox.Yes)
        else:
            print("map view")
            subprocess.call('./example.sh '+pcd_name, shell=True)
    def map_thread(self):
        mapping = threading.Thread(target=self.map_sh, args=())
        mapping.start()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.label1 = QLabel(' ', self)
        self.label2 = QLabel(' ', self)

        btn1 = QPushButton('bag 파일 불러오기', self)
        btn1.clicked.connect(self.add_open)
        btn2 = QPushButton('지도 제작하기', self)
        btn2.clicked.connect(self.map_thread)
        btn3= QPushButton('지도 불러오기', self)
        btn3.clicked.connect(self.map_add_open)
        btn4= QPushButton('지도 확인하기', self)
        btn4.clicked.connect(self.view_sh)

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 1, 0)
        grid.addWidget(btn4, 1, 1)
        grid.addWidget(self.label1, 2, 0)
        grid.addWidget(self.label2, 3, 0)

        self.setWindowTitle('Interface')
        self.resize(300, 100)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()

    sys.exit(app.exec_())
