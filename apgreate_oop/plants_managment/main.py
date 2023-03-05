from models import Plant, Employee

while True:
    print("1. Add Plant"
          "\n2. Gel all plants"
          "\n3. Add Employee"
          "\n4. Get all employees"
          "\n5. Get list of employees"
          "\n6. Change item of emplooees")

    flag = int(input("Choose menu item: "))
    if flag == 1:
        name = input("Plant name: ")
        address = input("Plant address: ")
        plant = Plant(name, address)
        plant.save()
    elif flag == 2:
        Plant.get_all_plants()
    elif flag == 3:
        name = input("Employee name: ")
        email = input("Employee email: ")
        plant_id = int(input("Plant id: "))

        # перевірка чи існує завод
        while Plant.exist_plant_id(plant_id) is False:
            plant_id = int(input("Enter exist Plant id: "))

        employee = Employee(name, email, plant_id)

        # перевірка хромає
        while employee.valid_email(email) is False:
            email = input("Enter correct and new email: ")
            employee = Employee(name, email, plant_id)
        else:
            employee = Employee(name, email, plant_id)

        employee.save()
    elif flag == 4:
        Employee.get_all_employees()
        # це тож працює але толку з нього, хз
    elif flag == 5:
        Employee.get_list_employees()
    elif flag == 6:
        # цей прапорець працює норм
        id = int(input("Enter id of employee: "))
        Employee.change_item(id)
    else:
        print("Not correct meny item")
