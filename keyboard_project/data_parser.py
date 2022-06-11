def modify_input_data(data):
    
    modified_data = []
    status_list = []

    for item in data:
        for i in range(6):
            status_list.append(item >> i & 1)

    button_names = [
        '0', '1', '2', '3', '4', '5',
        '8', '9', '10', '11', '12', '13',
        '16', '17', '18', '19', '20', '21',
        '24', '25', '26', '27', '28', '29']
    
    for name, status in zip(button_names, status_list):
        modified_data.append((name, status))

    return modified_data


def generate_output_data(key_data):
    output_data = []
    for item in key_data:
        index, state = item
        data = [0, 181, index, state] + [0] * 32
        output_data.append(data)
    return output_data
