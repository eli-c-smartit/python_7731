

def generate_resources():    
    return ['pic1.jpg','pic2.jpg','pic3.jpg']

def check_user_name(user_name):
    return len(user_name > 5) 

def check_user_password(password):
    return len(password > 8) 
    
        


if __name__ == '__main__':
    print(generate_resources())