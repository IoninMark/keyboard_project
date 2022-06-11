from collections import OrderedDict


class Key:

    def __init__(self, name) -> None:

        self.name = name
        self.key_status = 0
        self.red_led_status = 0
        self.blue_led_status = 0
        self.blue_led_index = 0
        self.red_led_index = 0

    def get_name(self):
        return self.name

    def set_key_status(self, pressed):
        self.key_status = pressed

    def get_key_status(self):
        return self.key_status

    def set_red_led_status(self, light):
        self.red_led_status = light

    def get_red_led_status(self):
        return self.red_led_status

    def set_blue_led_status(self, light):
        self.blue_led_status = light

    def get_blue_led_status(self):
        return self.blue_led_status

    def set_blue_led_index(self, index):
        self.blue_led_index = index

    def get_blue_led_index(self):
        return self.blue_led_index

    def set_red_led_index(self, index):
        self.red_led_index = index

    def get_red_led_index(self):
        return self.red_led_index


class Keyboard:

    keys = OrderedDict({})

    def __init__(self, vendor_id, product_id) -> None:
        self.vendor_id = vendor_id
        self.product_id = product_id

    def add_key(self, key):
        self.keys[key.get_name()] = key

    def set_keys_status(self, keys_status_list: list):
        for status in keys_status_list:
            key_name, state = status
            self.keys.get(key_name).set_key_status(state)

    def set_leds_status(self, leds_status_list: list):
        for status in leds_status_list:
            key_name, state = status
            self.keys.get(key_name).set_led_status(state)
