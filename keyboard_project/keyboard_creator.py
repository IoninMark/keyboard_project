from keyboard_project.keyboard import Keyboard, Key


def create_keyboard():

    vendor_id = 1523
    product_id = 1029
    keyboard = Keyboard(vendor_id, product_id)

    # key_names = [
    #     '0', '1', '2', '3', '4', '5',
    #     '8', '9', '10', '11', '12', '13',
    #     '16', '17', '18', '19', '20', '21',
    #     '24', '25', '26', '27', '28', '29']
    
    # for key_name in key_names:
       
    #     key = Key(key_name)
    #     index = int(key_name)
    #     key.set_blue_led_index(index)
    #     key.set_red_led_index(index + 32)
    #     keyboard.add_key(key)

    key_0 = Key('0')
    key_0.set_blue_led_index(0)
    key_0.set_red_led_index(32)
    keyboard.add_key(key_0)

    key_1 = Key('1')
    key_1.set_blue_led_index(1)
    key_1.set_red_led_index(33)
    keyboard.add_key(key_1)

    key_2 = Key('2')
    key_2.set_blue_led_index(2)
    key_2.set_red_led_index(34)
    keyboard.add_key(key_2)

    key_3 = Key('3')
    key_3.set_blue_led_index(3)
    key_3.set_red_led_index(35)
    keyboard.add_key(key_3)

    key_4 = Key('4')
    key_4.set_blue_led_index(4)
    key_4.set_red_led_index(36)
    keyboard.add_key(key_4)

    key_5 = Key('5')
    key_5.set_blue_led_index(5)
    key_5.set_red_led_index(37)
    keyboard.add_key(key_5)

    key_8 = Key('8')
    key_8.set_blue_led_index(8)
    key_8.set_red_led_index(40)
    keyboard.add_key(key_8)

    key_9 = Key('9')
    key_9.set_blue_led_index(9)
    key_9.set_red_led_index(41)
    keyboard.add_key(key_9)

    key_10 = Key('10')
    key_10.set_blue_led_index(10)
    key_10.set_red_led_index(42)
    keyboard.add_key(key_10)

    key_11 = Key('11')
    key_11.set_blue_led_index(11)
    key_11.set_red_led_index(43)
    keyboard.add_key(key_11)

    key_12 = Key('12')
    key_12.set_blue_led_index(12)
    key_12.set_red_led_index(44)
    keyboard.add_key(key_12)

    key_13 = Key('13')
    key_13.set_blue_led_index(13)
    key_13.set_red_led_index(45)
    keyboard.add_key(key_13)

    key_16 = Key('16')
    key_16.set_blue_led_index(16)
    key_16.set_red_led_index(48)
    keyboard.add_key(key_16)

    key_17 = Key('17')
    key_17.set_blue_led_index(17)
    key_17.set_red_led_index(49)
    keyboard.add_key(key_17)

    key_18 = Key('18')
    key_18.set_blue_led_index(18)
    key_18.set_red_led_index(50)
    keyboard.add_key(key_18)

    key_19 = Key('19')
    key_19.set_blue_led_index(19)
    key_19.set_red_led_index(51)
    keyboard.add_key(key_19)

    key_20 = Key('20')
    key_20.set_blue_led_index(20)
    key_20.set_red_led_index(52)
    keyboard.add_key(key_20)

    key_21 = Key('21')
    key_21.set_blue_led_index(21)
    key_21.set_red_led_index(53)
    keyboard.add_key(key_21)

    key_24 = Key('24')
    key_24.set_blue_led_index(24)
    key_24.set_red_led_index(56)
    keyboard.add_key(key_24)

    key_25 = Key('25')
    key_25.set_blue_led_index(25)
    key_25.set_red_led_index(57)
    keyboard.add_key(key_25)

    key_26 = Key('26')
    key_26.set_blue_led_index(26)
    key_26.set_red_led_index(58)
    keyboard.add_key(key_26)

    key_27 = Key('27')
    key_27.set_blue_led_index(27)
    key_27.set_red_led_index(59)
    keyboard.add_key(key_27)

    key_28 = Key('28')
    key_28.set_blue_led_index(28)
    key_28.set_red_led_index(60)
    keyboard.add_key(key_28)

    key_29 = Key('29')
    key_29.set_blue_led_index(29)
    key_29.set_red_led_index(61)
    keyboard.add_key(key_29)

    return keyboard

# k = create_keyboard()
# print(k.keys.values())
