# Description: Main file for the program

# Import the necessary modules
import sys
import os   
from PySide6 import *
from qt_material import apply_stylesheet
import psutil
from progress_bar import CircualProgressBar
import datetime
import platform
# Import the UI interface
from ui_interface import *


# Create the main window
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("icons/10010006041543238906.svg"))
        self.setWindowTitle("PSUTIL Manager")
        QSizeGrip(self.ui.size_grip)

        
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.minimize_btn.clicked.connect(self.showMinimized)
        self.ui.restor_btn.clicked.connect(lambda: self.maximize_restore())
        self.ui.cpu_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cpu_page))
        self.ui.battery_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.battery_page))
        self.ui.system_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.system_page))
        self.ui.activities_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.activities_page))
        self.ui.storage_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.storage_page))
        self.ui.networks_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.networks_page))
        self.ui.sensors_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sensors_page))
        self.ui.header_frame.mouseMoveEvent = self.moveWindow
        self.ui.menu_btn.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.cpu_btn.clicked.connect(lambda: self.applyButtonStyle(self.ui.cpu_btn))
        self.ui.battery_btn.clicked.connect(lambda: self.applyButtonStyle(self.ui.battery_btn))
        self.ui.system_btn.clicked.connect(lambda: self.applyButtonStyle(self.ui.system_btn))
        self.ui.activities_btn.clicked.connect(lambda: self.applyButtonStyle(self.ui.activities_btn))
        self.ui.storage_btn.clicked.connect(lambda: self.applyButtonStyle(self.ui.storage_btn))
        self.ui.networks_btn.clicked.connect(lambda: self.applyButtonStyle(self.ui.networks_btn))
        self.ui.sensors_btn.clicked.connect(lambda: self.applyButtonStyle(self.ui.sensors_btn))

        self.cpu()
        self.ram()
        self.battery()
        self.systemInfo()
        self.show()

    def applyButtonStyle(self, button):
        for btn in self.ui.menu_frame.findChildren(QPushButton):
                btn.setStyleSheet("border-bottom: none;")
        button.setStyleSheet("border-bottom: 3px solid;")
        return

    def slideLeftMenu(self):
        width = self.ui.left_menu_frame.width()
        if width == 39:
            newWidth = 150
        else:
            newWidth = 39
        self.animation = QPropertyAnimation(self.ui.left_menu_frame, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    # Function to maximize and restore the window
    def maximize_restore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    # Function to move the window
    def moveWindow(self, event):
        if self.isMaximized() == False:
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

    def cpu(self):
        cpu = psutil.cpu_percent()
        self.ui.cpu_usage.setText(str(cpu) + "%")
        self.ui.cpu_count.setText(str(psutil.cpu_count()))
        self.ui.cpu_core.setText(str(psutil.cpu_count(logical=False)))
        self.cpu_usage_bar = CircualProgressBar()
        self.cpu_usage_bar.value = cpu
        self.ui.cpu_usage_layout.addWidget(self.cpu_usage_bar)

    def ram(self):
        ram = psutil.virtual_memory()
        print(ram)
        self.ui.ram_total.setText(str(round(int(ram.total) / (1024.0 **3), 2)) + "GB")
        self.ui.ram_avibile.setText(str(round(int(ram.available) / (1024.0 **3), 2)) + "GB")
        self.ui.ram_used.setText(str(round(int(ram.used) / (1024.0 **3), 2)) + "GB")
        self.ui.ram_free.setText(str(round(int(ram.free) / (1024.0 **3), 2)) + "GB")
        self.ui.ram_usage.setText(str(round(int(ram.percent), 2)) + "%")
        self.ram_usage_bar = CircualProgressBar()
        self.ram_usage_bar.value = int(ram.percent)
        self.ui.ram_usage_layout.addWidget(self.ram_usage_bar)

    def battery(self):
        battery = psutil.sensors_battery()
        if not hasattr(psutil, "sensors_battery"):
            self.ui.battery_status.setText("Not supported")
            return
        if battery is None:
            self.ui.battery_status.setText("Not available")
            return
        if battery.power_plugged:
            self.ui.battery_charge.setText(str(round(battery.percent, 2)) + "%")
            self.ui.battery_time.setText("Charging")
            if battery.percent == 100:
                self.ui.battery_status.setText("Fully charged")
            else:
                self.ui.battery_status.setText("Charging")
            self.ui.battery_plugged.setText("Yes")
        else:
            self.ui.battery_plugged.setText("No")
            self.ui.battery_status.setText("Discharging")
            self.ui.battery_charge.setText(str(round(battery.percent, 2)) + "%")
            minutes = battery.secsleft/60
            hours = minutes/60
            minutes = minutes % 60
            self.ui.battery_time.setText(str(int(hours)) + " hours " + str(int(minutes)) + " minutes")
        self.battery_charge_bar = CircualProgressBar()
        self.battery_charge_bar.value = round(battery.percent, 2)
        self.ui.battery_charge_percentage.addWidget(self.battery_charge_bar)
        
    def systemInfo(self):
        self.ui.system_name.setText(platform.system())
        self.ui.system_version.setText(platform.version())
        self.ui.system_machine.setText(platform.machine())
        self.ui.system_time.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
        self.ui.system_date.setText(datetime.datetime.now().strftime("%I:%M:%S %p"))
        self.ui.system_processor.setText(platform.processor())
        self.ui.system_platform.setText(platform.platform())

# Run the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
