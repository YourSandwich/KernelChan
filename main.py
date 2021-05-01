from PySide2.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox, QTextBrowser, QVBoxLayout
from PySide2.QtGui import QGuiApplication, QIcon, QFont
from getKernelInfo import KernelVerList, KernelURL
import sys,os

# TODO: Fix the install Process function.
# TODO: Implement when ListItem selected and install pressed, to parse the array and download the right Kernel with wget or curl from the Archive
# TODO: Implement resizable Windows
# TODO: Clean the code.

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
        centerPoint = QGuiApplication.primaryScreen().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def setIcon(self):
        appIcon = QIcon('icon.png')
        self.setWindowIcon(appIcon)

    def installKernel(self):
        self.install = InstallProcess()
        self.install.show()

    ## Application Quit Popup
    def exitApp(self):
        askUser = QMessageBox.question(self, "Quit", "Are you Sure?", QMessageBox.Yes | QMessageBox.No)

        if askUser == QMessageBox.Yes:
            App.quit()
        elif askUser == QMessageBox.No:
            pass

## Making an Button
class Button(QPushButton):
    def setButton(self, name, x, y,function):
        button = QPushButton(name,self)
        button.move(x,y)

        button.clicked.connect(function)

## Making a List
class List(QListWidget):
        def setList(self,x,y):
            global aList

            self.aList = QListWidget(self)
            self.aList.resize(550,500)
            self.aList.move(x,y)
            aList = self.aList
            ## Taking the output from getKernelInfo and put it in the List
                       
        def addItem(self):
            for i in KernelVerList:
                self.item = QListWidgetItem(i, aList)
                font = QFont()
                font.setPixelSize(16)
                self.item.setFont(font)


class InstallProcess(QWidget):
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 

        self.setWindowTitle("Kernel Installation")
        self.setFixedSize(400,300)
        self.center()

        def Installation():
                DeList = List()
                print(DeList.item)

        #!!! WARNING this function is wrong it waits for the Terminal to finish then it display the output.
        #!!! If you put yes in it, the Program will freeze, there needs to be a better way to implement this.
        # Output into InstallProcess Windows -> QTextBrowser
        def letsgo():
            output = os.popen("echo 'The Place where all the Terminal work is gonna be done.'").read()
            return output
        Stream = letsgo()

        # create objects
        self.te = QTextBrowser()
        # puts the Terminal output into InstallWindow
        self.te.setHtml(Stream)

        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.te)
        self.setLayout(layout)      

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QGuiApplication.primaryScreen().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

def main():
    global App,window,DeList
    App = QApplication(sys.argv)
    window = Window()
    DeList = List()
    window.show()
    
    DeList.addItem()

    App.exec_()
    sys.exit(0)

main()
