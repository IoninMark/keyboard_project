from keyboard_project.keyboard import Keyboard, Key


def create_keyboard():

    vendor_id = 1523
    product_id = 1029
    keyboard = Keyboard(vendor_id, product_id)

    key_names = [
        '0', '1', '2', '3', '4', '5',
        '8', '9', '10', '11', '12', '13',
        '16', '17', '18', '19', '20', '21',
        '24', '25', '26', '27', '28', '29']
    
    for key_name in key_names:
       
        key = Key(key_name)
        index = int(key_name)
        key.set_blue_led_index(index)
        key.set_red_led_index(index + 32)
        keyboard.add_key(key)

    return keyboard
