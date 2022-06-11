from PyQt5.QtCore import QObject, pyqtSignal, QThread
from keyboard_project.port_module import USBPort
from keyboard_project.data_parser import modify_input_data, generate_output_data


class Communication(QObject):

    leds_updated = pyqtSignal()
    keys_updated = pyqtSignal(list)


    def get_data(self, data):
        
        modified_data = modify_input_data(data)
        self.keys_updated.emit(modified_data)

    def read_usb(self):
        self.input_thread = QThread()
        self.usb_port = USBPort()
        self.usb_port.moveToThread(self.input_thread)
        self.input_thread.started.connect(self.usb_port.read)
        # self.usb_port.finished.connect(self.usb_port.close)
        self.input_thread.finished.connect(self.input_thread.deleteLater)
        self.usb_port.data.connect(self.get_data)
        self.input_thread.start()
 

    def write_usb_data(self, key_obj):
        data = generate_output_data(key_obj)
        self.usb_port.write(data)
