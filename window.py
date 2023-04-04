# Import the necessary modules
import sys
from time import sleep
import traceback
from PySide6 import *
from qt_material import apply_stylesheet
import psutil
from progress_bar import CircualProgressBar
import datetime
import platform

# Import the UI interface
from ui_interface import *

class WorkerSignals(QObject):
    """Defines the signals available from a running worker thread."""
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

class Worker(QRunnable):
    """Worker thread"""
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress


    @Slot()
    
    def run(self):
        """Initialise the runner function with passed args, kwargs."""    
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()
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

# type: ignore clicked
        self.run = True
        self.ui.close_btn.clicked.connect(self.close_app)
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
        self.cpu_usage_bar = CircualProgressBar()
        self.ui.cpu_usage_layout.addWidget(self.cpu_usage_bar)
        self.ram_usage_bar = CircualProgressBar()
        self.ui.ram_usage_layout.addWidget(self.ram_usage_bar)
        self.battery_charge_bar = CircualProgressBar()
        self.ui.battery_charge_percentage.addWidget(self.battery_charge_bar)
        self.threadpool = QThreadPool()
        self.show()
        self.systemInfo()
        self.processes()
        self.storage()
        self.psutil_thread()



            
        
    def psutil_thread(self):
        """Run worker threads"""
        self.cpuWorker = Worker(self.cpu)
        self.cpuWorker.signals.result.connect(self.print_output)
        self.cpuWorker.signals.finished.connect(self.thread_complete)
        self.cpuWorker.signals.progress.connect(self.progress_fn)
        self.threadpool.start(self.cpuWorker)
        ramWorker = Worker(self.ram)
        ramWorker.signals.result.connect(self.print_output)
        ramWorker.signals.finished.connect(self.thread_complete)
        ramWorker.signals.progress.connect(self.progress_fn)
        self.threadpool.start(ramWorker)
        batteryWorker = Worker(self.battery)
        batteryWorker.signals.result.connect(self.print_output)
        batteryWorker.signals.finished.connect(self.thread_complete)
        batteryWorker.signals.progress.connect(self.progress_fn)
        self.threadpool.start(batteryWorker)
        sensorsWorker = Worker(self.sensor)
        sensorsWorker.signals.result.connect(self.print_output)
        sensorsWorker.signals.finished.connect(self.thread_complete)
        sensorsWorker.signals.progress.connect(self.progress_fn)
        self.threadpool.start(sensorsWorker)
        networkWorker = Worker(self.network)
        networkWorker.signals.result.connect(self.print_output)
        networkWorker.signals.finished.connect(self.thread_complete)
        networkWorker.signals.progress.connect(self.progress_fn)
        self.threadpool.start(networkWorker)

    def close_app(self):
        self.run = False
        self.threadpool.waitForDone()
        print("Application closed") 
        self.close()
        print("Application closed2")


    def print_output(self, s):
        """Output of the thread
        :param s: str"""
        print(s)

    def thread_complete(self):
        """Thread complete function"""
        print("THREAD COMPLETE!")

    def progress_fn(self, n):
        """Update the progress bar
        :param n: int"""
        print("%d%% done" % n)

    def applyButtonStyle(self, button):
        """Apply button style
        :param button: QPushButton
        """
        for btn in self.ui.menu_frame.findChildren(QPushButton):
                btn.setStyleSheet("border-bottom: none;")
        button.setStyleSheet("border-bottom: 3px solid;")
        return

    def slideLeftMenu(self):
        """Slide left menu"""
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
        """Maximize and restore the window"""
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


    def mousePressEvent(self, event):
        """Mouse press event
        :param event: QMouseEvent"""
        self.clickPosition = event.globalPos()

    # Function to move the window
    def moveWindow(self, event):
        """Move the window
        :param event: QMouseEvent"""
        if self.isMaximized() == False:
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

    def cpu(self, progress_callback):
        """CPU usage
        :param progress_callback: function"""
        while self.run:
            cpu = psutil.cpu_percent()
            self.ui.cpu_usage.setText(str(cpu) + "%")
            self.ui.cpu_count.setText(str(psutil.cpu_count()))
            self.ui.cpu_core.setText(str(psutil.cpu_count(logical=False)))
            self.cpu_usage_bar.setValue(cpu)
            if not self.run:
                break
            sleep(1)
 



    def ram(self, progress_callback):
        """RAM usage
        :param progress_callback: function"""
        while self.run:
            ram = psutil.virtual_memory()
            self.ui.ram_total.setText(str(round(int(ram.total) / (1024.0 **3), 2)) + "GB")
            self.ui.ram_avibile.setText(str(round(int(ram.available) / (1024.0 **3), 2)) + "GB")
            self.ui.ram_used.setText(str(round(int(ram.used) / (1024.0 **3), 2)) + "GB")
            self.ui.ram_free.setText(str(round(int(ram.free) / (1024.0 **3), 2)) + "GB")
            self.ui.ram_usage.setText(str(round(int(ram.percent), 2)) + "%")
            self.ram_usage_bar.setValue(ram.percent)
            if not self.run:
                break
            sleep(1)

    def battery(self, progress_callback):
        """Battery status
        :param progress_callback: function"""
        while self.run:
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
            self.battery_charge_bar.setValue(round(battery.percent, 2))
            if not self.run:
                break
            sleep(1)
        
    def systemInfo(self):
        """System information"""
        self.ui.system_name.setText(platform.system())
        self.ui.system_version.setText(platform.version())
        self.ui.system_machine.setText(platform.machine())
        self.ui.system_time.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
        self.ui.system_date.setText(datetime.datetime.now().strftime("%I:%M:%S %p"))
        self.ui.system_processor.setText(platform.processor())
        self.ui.system_platform.setText(platform.platform())

    def processes(self):
        """Processes"""
        for process in psutil.pids():
            rowPosition = self.ui.process_table.rowCount()
            self.ui.process_table.insertRow(rowPosition)
            try:
                p = psutil.Process(process)
                self.ui.process_table.setItem(rowPosition, 0, QTableWidgetItem(str(p.pid)))
                self.ui.process_table.setItem(rowPosition, 1, QTableWidgetItem(p.name()))
                self.ui.process_table.setItem(rowPosition, 2, QTableWidgetItem(str(round(float(p.cpu_percent()), 2))))
                self.ui.process_table.setItem(rowPosition, 3, QTableWidgetItem(str(round(float(p.memory_percent()), 2))))
                self.ui.process_table.setItem(rowPosition, 4, QTableWidgetItem(str(p.status())))
                self.ui.process_table.setItem(rowPosition, 5, QTableWidgetItem(str(p.username())))
                self.ui.process_table.setItem(rowPosition, 6, QTableWidgetItem(str(datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S"))))
            
            except:
                pass
        self.ui.suspend_btn.clicked.connect(lambda: self.suspend())
        self.ui.resume_btn.clicked.connect(lambda: self.resume())
        self.ui.terminate_btn.clicked.connect(lambda: self.terminate())
        self.ui.kill_btn.clicked.connect(lambda: self.kill())
        self.ui.search_process.textChanged.connect(lambda: self.findName())

    def findName(self):
        """Find process by name"""
        name = self.ui.search_process.text().lower()
        for row in range(self.ui.process_table.rowCount()):
            item = self.ui.process_table.item(row, 1)
            self.ui.process_table.setRowHidden(row, name not in item.text().lower())
        

    def suspend(self):
        """Suspend process"""
        try:
            pid = int(self.ui.process_table.selectedItems()[0].text())
            row = self.ui.process_table.selectedIndexes()[0].row()
            p = psutil.Process(pid)
            p.suspend()
            self.ui.process_table.setItem(row, 4, QTableWidgetItem(str(p.status())))
        except Exception as e:
            print(e)

    def resume(self):
        """Resume process"""
        try:
            pid = int(self.ui.process_table.selectedItems()[0].text())
            row = self.ui.process_table.selectedIndexes()[0].row()
            p = psutil.Process(pid)
            p.resume()
            self.ui.process_table.setItem(row, 4, QTableWidgetItem(str(p.status())))
        except Exception as e:
            print(e)

    def terminate(self):
        """Terminate process"""
        try:
            pid = int(self.ui.process_table.selectedItems()[0].text())
            row = self.ui.process_table.selectedIndexes()[0].row()
            p = psutil.Process(pid)
            p.terminate()
            self.ui.process_table.removeRow(row)
        except Exception as e:
            print(e)   

    def kill(self):
        """Kill process"""
        try:
            pid = int(self.ui.process_table.selectedItems()[0].text())
            row = self.ui.process_table.selectedIndexes()[0].row()
            p = psutil.Process(pid)
            p.kill()
            self.ui.process_table.removeRow(row)
        except Exception as e:
            print(e) 

    def storage(self):
        """Storage information"""
        for partition in psutil.disk_partitions():
            rowPosition = self.ui.storage_table.rowCount()
            self.ui.storage_table.insertRow(rowPosition)
            try:
                self.ui.storage_table.setItem(rowPosition, 0, QTableWidgetItem(partition.device))
                self.ui.storage_table.setItem(rowPosition, 1, QTableWidgetItem(partition.mountpoint))
                self.ui.storage_table.setItem(rowPosition, 2, QTableWidgetItem(partition.fstype))
                self.ui.storage_table.setItem(rowPosition, 3, QTableWidgetItem(str(psutil.disk_usage(partition.mountpoint).percent)))
                self.ui.storage_table.setItem(rowPosition, 4, QTableWidgetItem(str(round(float(psutil.disk_usage(partition.mountpoint).total)/(1024**3), 2))))
                self.ui.storage_table.setItem(rowPosition, 5, QTableWidgetItem(str(round(float(psutil.disk_usage(partition.mountpoint).used)/(1024**3), 2))))
                self.ui.storage_table.setItem(rowPosition, 6, QTableWidgetItem(str(round(float(psutil.disk_usage(partition.mountpoint).free)/(1024**3), 2))))
            except:
                pass

    def sensor(self, progress_callback):
        """Sensors
        @param progress_callback: callback to report progress"""
        while self.run:
            if platform.system() != "Windows":
                self.ui.sensor_table.setRowCount(0)
                for sensor in psutil.sensors_temperatures():
                    rowPosition = self.ui.sensor_table.rowCount()
                    self.ui.sensor_table.insertRow(rowPosition)
                    try:
                        self.ui.sensor_table.setItem(rowPosition, 0, QTableWidgetItem(sensor))
                        self.ui.sensor_table.setItem(rowPosition, 1, QTableWidgetItem(str(psutil.sensors_temperatures()[sensor][0].current)))
                        self.ui.sensor_table.setItem(rowPosition, 2, QTableWidgetItem(str(psutil.sensors_temperatures()[sensor][0].high)))
                        self.ui.sensor_table.setItem(rowPosition, 3, QTableWidgetItem(str(psutil.sensors_temperatures()[sensor][0].critical)))
                    except:
                        pass
            else:
                self.ui.sensor_table.deleteLater()
                self.ui.sensor_label.setText("Sensors are not supported on Windows")
                self.ui.sensor_label.resize(500, 700)
                self.ui.sensor_label.setStyleSheet("font-size: 20px;")
            if not self.run:
                break
            for i in range(5):
                if not self.run:
                    break
                sleep(1)


    def network(self, progress_callback):
        """Network information
        @param progress_callback: callback to report progress"""
        while self.run:
            self.ui.networkAddressesTable.setRowCount(0)
            self.ui.networtkStatsTable.setRowCount(0)
            self.ui.networkConnectionsTable.setRowCount(0)
            self.ui.networkIOTable.setRowCount(0)
            for netStat in psutil.net_if_stats():
                stat = psutil.net_if_stats()
                rowPosition = self.ui.networtkStatsTable.rowCount()
                self.ui.networtkStatsTable.insertRow(rowPosition)
                try:
                    self.ui.networtkStatsTable.setItem(rowPosition, 0, QTableWidgetItem(netStat))
                    self.ui.networtkStatsTable.setItem(rowPosition, 1, QTableWidgetItem(str(stat[netStat].isup)))
                    self.ui.networtkStatsTable.setItem(rowPosition, 2, QTableWidgetItem(str(stat[netStat].duplex)))
                    self.ui.networtkStatsTable.setItem(rowPosition, 3, QTableWidgetItem(str(stat[netStat].speed)))
                    self.ui.networtkStatsTable.setItem(rowPosition, 4, QTableWidgetItem(str(stat[netStat].mtu)))
                except:
                    pass
            for netStat in psutil.net_io_counters(pernic=True):
                stat = psutil.net_io_counters(pernic=True)
                rowPosition = self.ui.networkIOTable.rowCount()
                self.ui.networkIOTable.insertRow(rowPosition)
                try:
                    self.ui.networkIOTable.setItem(rowPosition, 0, QTableWidgetItem(netStat))
                    self.ui.networkIOTable.setItem(rowPosition, 1, QTableWidgetItem(str(stat[netStat].bytes_sent)))
                    self.ui.networkIOTable.setItem(rowPosition, 2, QTableWidgetItem(str(stat[netStat].bytes_recv)))
                    self.ui.networkIOTable.setItem(rowPosition, 3, QTableWidgetItem(str(stat[netStat].packets_sent)))
                    self.ui.networkIOTable.setItem(rowPosition, 4, QTableWidgetItem(str(stat[netStat].packets_recv)))
                    self.ui.networkIOTable.setItem(rowPosition, 5, QTableWidgetItem(str(stat[netStat].errin)))
                    self.ui.networkIOTable.setItem(rowPosition, 6, QTableWidgetItem(str(stat[netStat].errout)))
                    self.ui.networkIOTable.setItem(rowPosition, 7, QTableWidgetItem(str(stat[netStat].dropin)))
                    self.ui.networkIOTable.setItem(rowPosition, 8, QTableWidgetItem(str(stat[netStat].dropout)))
                except:
                    pass
            for netStat in psutil.net_connections():
                stat = psutil.net_connections()
                rowPosition = self.ui.networkConnectionsTable.rowCount()
                self.ui.networkConnectionsTable.insertRow(rowPosition)
                try:
                    self.ui.networkConnectionsTable.setItem(rowPosition, 0, QTableWidgetItem(str(netStat.fd)))
                    self.ui.networkConnectionsTable.setItem(rowPosition, 1, QTableWidgetItem(str(netStat.family)))
                    self.ui.networkConnectionsTable.setItem(rowPosition, 2, QTableWidgetItem(str(netStat.type)))
                    self.ui.networkConnectionsTable.setItem(rowPosition, 3, QTableWidgetItem(str(netStat.laddr)))
                    self.ui.networkConnectionsTable.setItem(rowPosition, 4, QTableWidgetItem(str(netStat.raddr)))
                    self.ui.networkConnectionsTable.setItem(rowPosition, 5, QTableWidgetItem(str(netStat.status)))
                    self.ui.networkConnectionsTable.setItem(rowPosition, 6, QTableWidgetItem(str(netStat.pid)))
                except:
                    pass
            for netStat in psutil.net_if_addrs():
                stat = psutil.net_if_addrs()
                for s in stat[netStat]:
                    rowPosition = self.ui.networkAddressesTable.rowCount()
                    self.ui.networkAddressesTable.insertRow(rowPosition)
                    try:
                        self.ui.networkAddressesTable.setItem(rowPosition, 0, QTableWidgetItem(str(netStat)))
                        self.ui.networkAddressesTable.setItem(rowPosition, 1, QTableWidgetItem(str(s.family)))
                        self.ui.networkAddressesTable.setItem(rowPosition, 2, QTableWidgetItem(str(s.address)))
                        self.ui.networkAddressesTable.setItem(rowPosition, 3, QTableWidgetItem(str(s.netmask)))
                        self.ui.networkAddressesTable.setItem(rowPosition, 4, QTableWidgetItem(str(s.broadcast)))
                        self.ui.networkAddressesTable.setItem(rowPosition, 5, QTableWidgetItem(str(s.ptp)))
                    except:
                        pass
            for i in range(10):
                if not self.run:
                    break
                sleep(1)
            