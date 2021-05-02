from PySide2.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox, QLabel, QVBoxLayout
from PySide2.QtGui import QGuiApplication, QIcon, QFont
from getKernelInfo import KernelVerList, KernelURL
import sys,os,time

# TODO: Fix the install Process function.
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
        setList(self,25,20)
        Button.setButton(self,"Install",400,540,self.installKernel)
        Button.setButton(self,"Exit",490,540,self.exitApp)
        aList.itemSelectionChanged.connect(selected)

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
        self.install.Installation()
        self.install.hide()

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


class InstallProcess(QWidget):
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 

        self.setWindowTitle("Kernel Installation")
        self.setFixedSize(400,120)
        self.center()   

        # create objects
        self.te = QLabel()
        # puts the Terminal output into InstallWindow
        pic = 'Installing.png'
        self.te.setPixmap(pic)

        # layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.te)
        self.setLayout(self.layout)

    def Installation(self):
        os.system("wget "+ URL + " -P ~/")
        print("done")

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QGuiApplication.primaryScreen().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

def setList(self,x,y):
    global aList
    aList = QListWidget(self)
    aList.resize(550,500)
    aList.move(x,y)
    font = QFont()
    font.setPixelSize(16)
    aList.setFont(font)

    for i in KernelVerList:
        item = QListWidgetItem()
        item.setText(str(i))
        aList.addItem(item)

def selected():
    global TheSelect, URL
    TheSelect = str([item.text() for item in aList.selectedItems()])
    TheSelect = TheSelect.strip("'['']'")
    URL = [name for name in KernelURL if TheSelect in name]
    URL = '+'.join(URL).strip("'['']'").split("+", 1)[0]

    print(URL)


def main():
    global App,window
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    
    App.exec_()
    sys.exit(0)

if __name__ == '__main__':
    main()
