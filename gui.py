from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300) #position/size of window (xpos, ypos, width, height), starts from top left and moves the top left corner of that window
        self.setWindowTitle("GUI") #sets window title for top bar
        self.initUI()
        
    def initUI(self):
        self.btnRedLED = QtWidgets.QPushButton(self)
        self.btnRedLED.setText("Red - OFF")
        self.btnRedLED.move(10, 10)
        
        self.btnRedLED.clicked.connect(self.clickedRed)
        
        self.btnGreenLED = QtWidgets.QPushButton(self)
        self.btnGreenLED.setText("Green - OFF")
        self.btnGreenLED.move(10, 60)
        
        self.btnGreenLED.clicked.connect(self.clickedGreen)
        
        self.btnBlueLED = QtWidgets.QPushButton(self)
        self.btnBlueLED.setText("Blue - OFF")
        self.btnBlueLED.move(10, 110)
        
        self.btnBlueLED.clicked.connect(self.clickedBlue)
        
        self.btnExit = QtWidgets.QPushButton(self)
        self.btnExit.setText("Reset")
        self.btnExit.move(180, 250)
        
        self.btnExit.clicked.connect(self.clickedExit)
        
    def clickedRed(self):
        self.btnRedLED.setText("Red - ON")
        self.btnGreenLED.setText("Green - OFF")
        self.btnBlueLED.setText("Blue - OFF")
        
        self.updateRed()
        
    def clickedGreen(self):
        self.btnRedLED.setText("Red - OFF")
        self.btnGreenLED.setText("Green - ON")
        self.btnBlueLED.setText("Blue - OFF")
        
        self.updateGreen()
        
    def clickedBlue(self):
        self.btnRedLED.setText("Red - OFF")
        self.btnGreenLED.setText("Green - OFF")
        self.btnBlueLED.setText("Blue - ON")
        
        self.updateBlue()
        
    def updateRed(self):
        GPIO.output(7, GPIO.HIGH) #turns on Red LED
        GPIO.output(11, GPIO.LOW) #turns off Green LED
        GPIO.output(37, GPIO.LOW) #turns off Blue LED
        
    def updateGreen(self):
        GPIO.output(7, GPIO.LOW) #turns off Red LED
        GPIO.output(11, GPIO.HIGH) #turns on Green LED
        GPIO.output(37, GPIO.LOW) #turns off Blue LED
        
    def updateBlue(self):
        GPIO.output(7, GPIO.LOW) #turns off Red LED
        GPIO.output(11, GPIO.LOW) #turns off Green LED
        GPIO.output(37, GPIO.HIGH) #turns on Blue LED
        
    def clickedExit(self):
        GPIO.output(7, GPIO.LOW) #turns off Red LED
        GPIO.output(11, GPIO.LOW) #turns off Green LED
        GPIO.output(37, GPIO.LOW) #turns off Blue LED
        
        self.btnExit.setText("Exit")
        self.btnExit.clicked.connect(self.close) #closes the application when clicked
        
def window():
    app = QApplication(sys.argv) #config setup for our application, also based on OS using
    win = MyWindow() #creates the window to show in our application
    
    win.show() #shows window
    sys.exit(app.exec_()) #makes sure it will exit when needed
    
window()