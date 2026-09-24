import random
import string

def generate_password(length=12):

    if length < 4:
        return "Length should be more than 4"


    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits =string.digits
    special = string.punctuation

    all_characters = lower + upper + digits + special

    password_list = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special),
    ]    

    remaining_length = length -4

    for _ in range(remaining_length):
        password_list.append(random.choice(all_characters))

    random.shuffle(password_list)

    final_password="".join(password_list)   

    return final_password



print(generate_password())