import time
import pyautogui
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QThread
from pynput.keyboard import Listener


class Ui_MainWindow(object):
    def setupUi(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        main_window.resize(480, 200)
        main_window.setMaximumSize(640, 280)
        main_window.setMinimumSize(480, 200)
        font = QtGui.QFont()
        font.setPointSize(10)
        main_window.setFont(font)
        main_window.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_start_delay = QtWidgets.QHBoxLayout()
        self.horizontalLayout_start_delay.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout_start_delay.setObjectName("horizontalLayout_start_delay")
        self.label_start_delay = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_start_delay.sizePolicy().hasHeightForWidth())
        self.label_start_delay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_start_delay.setFont(font)
        self.label_start_delay.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_start_delay.setObjectName("label_start_delay")
        self.horizontalLayout_start_delay.addWidget(self.label_start_delay)
        self.lineEdit_start_delay = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_start_delay.sizePolicy().hasHeightForWidth())
        self.lineEdit_start_delay.setSizePolicy(sizePolicy)
        self.lineEdit_start_delay.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_start_delay.setFont(font)
        self.lineEdit_start_delay.setObjectName("lineEdit_start_delay")
        self.horizontalLayout_start_delay.addWidget(self.lineEdit_start_delay)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_start_delay.addWidget(self.frame)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_start_delay.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_start_delay)
        self.horizontalLayout_click1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_click1.setObjectName("horizontalLayout_click1")
        self.label_click1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_click1.sizePolicy().hasHeightForWidth())
        self.label_click1.setSizePolicy(sizePolicy)
        self.label_click1.setMinimumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_click1.setFont(font)
        self.label_click1.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_click1.setScaledContents(False)
        self.label_click1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_click1.setObjectName("label_click1")
        self.horizontalLayout_click1.addWidget(self.label_click1)
        self.label__end_delay_1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label__end_delay_1.sizePolicy().hasHeightForWidth())
        self.label__end_delay_1.setSizePolicy(sizePolicy)
        self.label__end_delay_1.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label__end_delay_1.setFont(font)
        self.label__end_delay_1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label__end_delay_1.setObjectName("label__end_delay_1")
        self.horizontalLayout_click1.addWidget(self.label__end_delay_1)
        self.lineEdit_end_delay1 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_end_delay1.sizePolicy().hasHeightForWidth())
        self.lineEdit_end_delay1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_end_delay1.setFont(font)
        self.lineEdit_end_delay1.setObjectName("lineEdit_end_delay1")
        self.horizontalLayout_click1.addWidget(self.lineEdit_end_delay1)
        self.verticalLayout.addLayout(self.horizontalLayout_click1)
        self.horizontalLayout_click2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_click2.setObjectName("horizontalLayout_click2")
        self.label_click2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_click2.sizePolicy().hasHeightForWidth())
        self.label_click2.setSizePolicy(sizePolicy)
        self.label_click2.setMinimumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_click2.setFont(font)
        self.label_click2.setScaledContents(False)
        self.label_click2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_click2.setObjectName("label_click2")
        self.horizontalLayout_click2.addWidget(self.label_click2)
        self.label_end_delay2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_end_delay2.sizePolicy().hasHeightForWidth())
        self.label_end_delay2.setSizePolicy(sizePolicy)
        self.label_end_delay2.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_end_delay2.setFont(font)
        self.label_end_delay2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_end_delay2.setObjectName("label_end_delay2")
        self.horizontalLayout_click2.addWidget(self.label_end_delay2)
        self.lineEdit_end_delay_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_end_delay_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_end_delay_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_end_delay_2.setFont(font)
        self.lineEdit_end_delay_2.setObjectName("lineEdit_end_delay_2")
        self.horizontalLayout_click2.addWidget(self.lineEdit_end_delay_2)
        self.verticalLayout.addLayout(self.horizontalLayout_click2)
        self.horizontalLayout_click3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_click3.setObjectName("horizontalLayout_click3")
        self.label_click3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_click3.sizePolicy().hasHeightForWidth())
        self.label_click3.setSizePolicy(sizePolicy)
        self.label_click3.setMinimumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_click3.setFont(font)
        self.label_click3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_click3.setObjectName("label_click3")
        self.horizontalLayout_click3.addWidget(self.label_click3)
        self.label_end_delay3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_end_delay3.sizePolicy().hasHeightForWidth())
        self.label_end_delay3.setSizePolicy(sizePolicy)
        self.label_end_delay3.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_end_delay3.setFont(font)
        self.label_end_delay3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_end_delay3.setObjectName("label_end_delay3")
        self.horizontalLayout_click3.addWidget(self.label_end_delay3)
        self.lineEdit_end_delay_3 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_end_delay_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_end_delay_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_end_delay_3.setFont(font)
        self.lineEdit_end_delay_3.setObjectName("lineEdit_end_delay_3")
        self.horizontalLayout_click3.addWidget(self.lineEdit_end_delay_3)
        self.verticalLayout.addLayout(self.horizontalLayout_click3)
        self.horizontalLayout_start_stop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_start_stop.setObjectName("horizontalLayout_start_stop")
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_stop.sizePolicy().hasHeightForWidth())
        self.pushButton_stop.setSizePolicy(sizePolicy)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout_start_stop.addWidget(self.pushButton_stop)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        self.pushButton_start.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_start_stop.addWidget(self.pushButton_start)
        self.verticalLayout.addLayout(self.horizontalLayout_start_stop)
        main_window.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(change_setup)
        self.pushButton_start.clicked.connect(start_script)
        self.pushButton_stop.clicked.connect(stop_script)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Clicker by retrotunes"))
        self.label_start_delay.setText(_translate("MainWindow", "Start delay (seconds)"))
        self.lineEdit_start_delay.setText(_translate("MainWindow", "5"))
        self.pushButton.setText(_translate("MainWindow", "Set up"))
        self.label_click1.setText(_translate("MainWindow", "Click 1 (not set)"))
        self.label__end_delay_1.setText(_translate("MainWindow", "End delay (seconds)"))
        self.lineEdit_end_delay1.setText(_translate("MainWindow", "5"))
        self.label_click2.setText(_translate("MainWindow", "Click 2 (not set)"))
        self.label_end_delay2.setText(_translate("MainWindow", "End delay (seconds)"))
        self.lineEdit_end_delay_2.setText(_translate("MainWindow", "5"))
        self.label_click3.setText(_translate("MainWindow", "Click 3 (not set)"))
        self.label_end_delay3.setText(_translate("MainWindow", "End delay (minutes)"))
        self.lineEdit_end_delay_3.setText(_translate("MainWindow", "180"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys

    setup = False
    ready = False
    click1_pos = 0
    click2_pos = 0
    click3_pos = 0


    class Worker(QThread):
        isRunning = True

        def __init__(self):
            QThread.__init__(self)

        def sleep(self, time_left):
            while time_left > 0 and self.isRunning:
                time_left = time_left-1
                time.sleep(1)
            return

        def run(self):
            while self.isRunning:
                self.sleep(int(ui.lineEdit_start_delay.text()))
                pyautogui.click(click1_pos)
                self.sleep(int(ui.lineEdit_end_delay1.text()))
                pyautogui.click(click2_pos)
                self.sleep(int(ui.lineEdit_end_delay_2.text()))
                pyautogui.click(click3_pos)
                self.sleep(int(ui.lineEdit_end_delay_3.text())*60)
            self.exit()


    THREAD = Worker()


    def start_script():
        if ready:
            ui.pushButton_start.setEnabled(False)
            ui.pushButton_stop.setEnabled(True)
            ui.pushButton.setEnabled(False)
            THREAD.start()
            THREAD.isRunning = True


    def stop_script():
        if ready:
            ui.pushButton_start.setEnabled(True)
            ui.pushButton_stop.setEnabled(False)
            ui.pushButton.setEnabled(True)
            THREAD.isRunning = False


    def change_setup():
        global setup, ready, click1_pos, click2_pos, click3_pos

        if not setup:
            click1_pos = 0
            click2_pos = 0
            click3_pos = 0
            ui.label_click1.setText(f'Click 1 (press 1)')
            ui.label_click2.setText(f'Click 2 (press 2)')
            ui.label_click3.setText(f'Click 3 (press 3)')
            ui.pushButton.setText('Done')
            setup = True
            ready = False
        else:
            ui.pushButton.setText('Set up')
            if click1_pos != 0 and click2_pos != 0 and click3_pos != 0:
                ready = True
            setup = False

        if ready:
            ui.pushButton_start.setEnabled(True)
        else:
            ui.pushButton_start.setEnabled(False)


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    def on_press(key):
        global setup, click1_pos, click2_pos, click3_pos
        if setup:
            if hasattr(key, 'char'):
                if key.char == '1':
                    click1_pos = pyautogui.position()
                    ui.label_click1.setText(f'Click 1 ({click1_pos[0]}x{click1_pos[1]})')
                if key.char == '2':
                    click2_pos = pyautogui.position()
                    ui.label_click2.setText(f'Click 2 ({click2_pos[0]}x{click2_pos[1]})')
                if key.char == '3':
                    click3_pos = pyautogui.position()
                    ui.label_click3.setText(f'Click 3 ({click3_pos[0]}x{click3_pos[1]})')


    listener = Listener(on_press=on_press)
    listener.start()

    sys.exit(app.exec())
