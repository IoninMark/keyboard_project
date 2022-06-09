def modify_input_data(data):
    
    modified_data = []
    status_str = ''

    for item in data:
        bin_item = format(item, '08b')[:1:-1]
        status_str += bin_item

    button_names = [
        '0', '1', '2', '3', '4', '5',
        '8', '9', '10', '11', '12', '13',
        '16', '17', '18', '19', '20', '21',
        '24', '25', '26', '27', '28', '29']
    
    
    for name, status in zip(button_names, status_str):
        modified_data.append((name, int(status)))

    return modified_data


def generate_output_data(key_data):
    output_data = []
    for item in key_data:
        index, state = item
        data = [0, 181, index, state] + [0] * 32
        output_data.append(data)
    return output_data
