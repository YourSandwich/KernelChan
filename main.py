from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from getKernelInfo import KernelVerList
import sys,os

## Creating the MainWindow
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KernelChan")
        self.setFixedSize(600,600)

        self.center()
        self.setIcon()
        List.setList(self,25,20)
        Button.setButton(self,"Install",400,540,self.installKernel)
        Button.setButton(self,"Exit",490,540,self.exitApp)

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def setIcon(self):
        appIcon = QIcon('icon.png')
        self.setWindowIcon(appIcon)


    def installKernel(self):
        self.install = InstallProcess()
        self.install.show()
        
        global InstallOutput
        InstallOutput = print("lol")

    ## Application Quit Popup
    def exitApp(self):
        askUser = QMessageBox.question(self, "Quit", "Are you Sure?", QMessageBox.Yes | QMessageBox.No)

        if askUser == QMessageBox.Yes:
            App.quit()
        elif askUser == QMessageBox.No:
            pass

## Window after Install Button was pressed
class InstallProcess(QWidget):
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 

        self.setWindowTitle("Kernel Installation")
        self.setFixedSize(400,300)
        self.center()

        # create objects
        self.te = QTextBrowser()
        self.te.setHtml("InstallOutput")

        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.te)
        self.setLayout(layout)      

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

## Making an Button
class Button(QPushButton):
    def setButton(self, name, x, y,function):
        button = QPushButton(name,self)
        button.move(x,y)

        button.clicked.connect(function)

## Making a List
class List(QListWidget):
        def setList(self,x,y):
            self.aList = QListWidget(self)
            self.aList.resize(550,500)
            self.aList.move(x,y)

            ## Taking the output from getKernelInfo and put it in the List
            for i in KernelVerList:
                item = QListWidgetItem(i, self.aList)

                font = QFont()
                font.setPixelSize(16)
                item.setFont(font)


App = QApplication(sys.argv)
window = Window()
window.show()

App.exec_()
sys.exit(0)
