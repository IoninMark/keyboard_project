import hid
import time
from PyQt5.QtCore import QObject, pyqtSignal


class USBPort(QObject):

    def __init__(self, data):
        QObject.__init__(self)
        self.data_to_write = data
    
    myFinished = False
    finished = pyqtSignal()
    data = pyqtSignal(list)
    vendor_id = 1523
    product_id = 1029


    def read(self):
        """Long-running task."""
        for _ in range(10):
            try:
                self.h = hid.device()
                self.h.open(self.vendor_id, self.product_id)  # X-Keys VendorID/ProductID
            except IOError as ex:
                self.h.close()
                print(ex)
                print("Connection error!")
                continue
            else:
                break
        else:
            self.close()
            

        print("Manufacturer: %s" % self.h.get_manufacturer_string())
        print("Product: %s" % self.h.get_product_string())

        # enable non-blocking mode
        self.h.set_nonblocking(1)

        try:
            while not self.myFinished:
                if self.data_to_write['data']:
                    for item in self.data_to_write['data']:
                        self.h.write(item)
                        time.sleep(0.05)
                    self.data_to_write['data'] = False
                else:
                    d = self.h.read(33)
                    if d:
                        self.data.emit(d[2:6:])
            self.h.close()

        except IOError as ex:
            self.h.close()
            print(ex)
            print("Reading error!")
            print("You probably don't have the hard-coded device.")


    def write(self, data):
        print(data)
        print(self.h.write(data))


    def close(self):
        self.myFinished = True
        self.finished.emit()
        self.h.close()
    