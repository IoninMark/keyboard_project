import hid
from PyQt5.QtCore import QObject, pyqtSignal, QMutex


class USBPort(QObject):

    myFinished = False
    finished = pyqtSignal()
    data = pyqtSignal(list)
    vendor_id = 1523
    product_id = 1029
    # vendor_id = 5426
    # product_id = 107
    lock = QMutex()

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

        # enable blocking mode
        self.h.set_nonblocking(0)

        try:
            while not self.myFinished:
                self.doRead()
            self.h.close()

        except IOError as ex:
            self.h.close()
            print(ex)
            print("Reading error!")

    def doRead(self):
        try:
            self.lock.lock()
            d = self.h.read(33, 100)
            if d:
                self.data.emit(d[2:6:])
        finally:
            self.lock.unlock()

    def write(self, data):
        try:
            self.lock.lock()
            for item in data:
                self.h.write(item)
        finally:
            self.lock.unlock()

    def close(self):
        self.myFinished = True
        self.finished.emit()
        # self.h.close()
