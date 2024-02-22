import json

def save_data(name, email, message):
    data = {
        'name': name,
        'email': email,
        'message': message
    }
    with open('form_data.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')  # Add a new line for each entry
