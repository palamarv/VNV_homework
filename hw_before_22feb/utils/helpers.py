import json
import re

def get_all_humans() -> list:
    try:
        f = open("database/persons.json", "r")
        data = json.loads(f.read())
        f.close()
    except FileNotFoundError:
        f = open("database/persons.json", "w")
        f.write("[]")
        f.close()
        data = json.loads(f.read())
    return data


def write_new_human(human: dict):
    data = get_all_humans()
    if len(data) < 1:
        human["id"] = 1
    else:
        human["id"] = len(data) + 1
    data.append(human)
    file = open("database/persons.json", "w")
    data = json.dumps(data)
    file.write(data)
    file.close()


# 1. Додати перевірку чи введений емейл дійсно емейл, щоб користувач
# не міг вписати "blabla" допускається тільки формат "blabla@blabla.com"

def check_email(email):

    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat, email):
        return True
    else:
        return False


# 2.* Додати можливість редагувати людину

def change_human_items(input_id):
    data = get_all_humans()
    for item in data:
        if item["id"] == int(input_id):
            item["first_name"] = input("Edit your first name: ")
            item["last_name"] = input("Edit your last name: ")
            email = input("Edit your emai: ")
            # додатково перевірив чи коректний емейл)
            while check_email(email) is False:
                email = input("Enter correct Email: ")
            item["email"] = email

    file = open("database/persons.json", "w")
    data = json.dumps(data)
    file.write(data)
    file.close()


# 3.** Додати перевірку чи емейл який вводить користувач вже є в базі данних
# Також додав перевірку чи правильно введений емейл

def is_email_correct(em):
    data = get_all_humans()
    check_list = []
    for item in data:
        check_list.append(item["email"])
    # print(check_list)
    result = check_email(em)
    if em in check_list:
        return result and False
    else:
        return result and True
