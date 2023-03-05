import json
import re

class Plant:
    file = "database/plants.json"

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def generate_dict(self):
        return {
            "name": self.name,
            "address": self.address
        }

    def save(self):
        self.get_all_plants()
        file = open(self.file, "r")
        plants = json.loads(file.read())
        file.close()
        file = open(self.file, "w")
        plant = self.generate_dict()
        if len(plants) > 1:
            plant["id"] = len(plants) + 1
        else:
            plant["id"] = 1
        plants.append(plant)
        file.write(json.dumps(plants))
        file.close()
    @classmethod
    def exist_plant_id(cls, input_id):
        file = open(cls.file, "r")
        plants = json.loads(file.read())
        file.close()
        list_id = []
        for plant in plants:
            list_id.append(plant["id"])
        if input_id in list_id:
            return True
        else:
            return False

    @classmethod
    def get_all_plants(cls):
        file = open(cls.file, "r")
        plants = json.loads(file.read())
        file.close()
        for plant in plants:
            print(plant["name"])
            print(plant["address"])


class Employee:
    file = "database/employees.json"

    def __init__(self, name, email, plant_id):
        self.name = name
        self.email = email
        self.plant_id = plant_id

    def generate_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "plant_id": self.plant_id
        }

    def save(self):
        file = open(self.file, "r")
        employees = json.loads(file.read())
        file.close()
        file = open(self.file, "w")
        employee = self.generate_dict()
        if len(employees) > 1:
            employee["id"] = len(employees) + 1
        else:
            employee["id"] = 1
        employees.append(employee)
        file.write(json.dumps(employees))
        file.close()


    def valid_email(self, email):

        result = True

        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.match(pat, self.email):
            result += True
        else:
            result += False

        file = open(self.file, "r")
        data = json.loads(file.read())
        file.close()

        check_list = []
        for item in data:
            check_list.append(item["email"])
        # print(check_list)

        if self.email in check_list:
            return result and False
        else:
            return result and True


    @classmethod
    def get_all_employees(cls):
        file = open(cls.file, "r")
        employees = json.loads(file.read())
        file.close()
        for employee in employees:
            print(employee["name"])
            print(employee["email"])
            print(employee["plant_id"])

    @classmethod
    def get_list_employees(cls):
        file = open(cls.file, "r")
        employees = json.loads(file.read())
        file.close()

        result = []
        for employee in employees:
            result.append(employee["name"])
        print(result)

    @classmethod
    def change_item(cls, input_id):
        file = open(cls.file, "r")
        employees = json.loads(file.read())
        file.close()
        for employee in employees:
            if employee["id"] == input_id:
                employee["name"] = input("Enter new name: ")
                employee["email"] = input("Enter new email: ")
                employee["plant_id"] = input("Enter new plant id: ")
            else:
                print("This employee doesnt exist!")
        file = open(cls.file, "w")
        employees = json.dumps(employees)
        file.write(employees)
        file.close()
