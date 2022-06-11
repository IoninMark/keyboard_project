from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QMenu
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui
from keyboard_project.communication_module import Communication
from keyboard_project.keyboard_creator import create_keyboard


class Button(QPushButton):

    led_modified = pyqtSignal(list)

    def __init__(self, key_obj):

        self.key_obj = key_obj
        self.name = key_obj.get_name()

        super().__init__(self.name)

        menu_titles = ['Red', 'Blue', 'Turn Off']
        menu = QMenu()
        menu.triggered.connect(lambda x: self.set_led(x.text()))

        self.setMenu(menu)
        self.add_menu(menu_titles, menu)

    def add_menu(self, data, menu_obj):
        for element in data:
            action = menu_obj.addAction(element)
            action.setIconVisibleInMenu(False)

    def set_led(self, menu_title):

        if menu_title == 'Red':
            print(f"{self.name} turned red!")
            self.key_obj.set_red_led_status(1)
            self.key_obj.set_blue_led_status(0)

        elif menu_title == 'Blue':
            print(f"{self.name} turned blue!")
            self.key_obj.set_blue_led_status(1)
            self.key_obj.set_red_led_status(0)

        else:
            print(f"{self.name} turned off!")
            self.key_obj.set_red_led_status(0)
            self.key_obj.set_blue_led_status(0)

        self.led_modified.emit([
            (self.key_obj.get_red_led_index(), self.key_obj.get_red_led_status()),
            (self.key_obj.get_blue_led_index(), self.key_obj.get_blue_led_status())
            ])


class MyWindow(QWidget):

    started = True

    def __init__(self, app):
        super().__init__()

        self.app = app
        self.communication = Communication()
        self.keyboard = create_keyboard()
        self.init_ui()

    def init_ui(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.buttons_list = []

        keys_list = self.keyboard.keys.values()
        x = 0
        y = 0

        for key in keys_list:
            button = Button(key)
            button.led_modified.connect(
                lambda led_state: self.communication.write_usb_data(led_state))
            self.buttons_list.append(button)
            self.grid.addWidget(button, x % 6, y // 6)
            x += 1
            y += 1

        self.move(300, 150)
        self.setWindowTitle('X-keys XK-24')

        self.communication.read_usb()
        self.communication.keys_updated.connect(self.set_buttons_state)
        self.show()

    def set_buttons_state(self, data):

        self.keyboard.set_keys_status(data)
        for button in self.buttons_list:
            if (button.isFlat() != bool(button.key_obj.get_key_status())):
                button.setFlat(button.key_obj.key_status)

    def closeEvent(self, e: QtGui.QCloseEvent):
        e.accept()
        self.communication.usb_port.close()
        # self.communication.input_thread.exec()
        # self.app.exit()
