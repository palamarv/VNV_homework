from utils.helpers import write_new_human, get_all_humans, \
     is_email_correct, change_human_items


while True:
    print("1. Add new person! \n2. Get all persons! \n3. Edit person!")
    flag = int(input("Choose what you want to do: "))
    if flag == 1:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")

        # додав перевірку для емейлу(хотів би фідбек, чому
        # is_email_correct(email) підкреслений жовтою лінією, в чому синтаксична помилка)

        while is_email_correct(email) is False:
            email = input("Enter new and correct Email: ")
        else:
            human_dict = {'first_name': first_name, "last_name": last_name, "email": email}
        write_new_human(human_dict)
    elif flag == 2:
        humans = get_all_humans()
        for human in humans:
            print(human["first_name"])
            print(human["last_name"])
            print(human["email"])
            print(human["id"])
            print("==================================================================")
    elif flag == 3:
        change_id = int(input("Enter id human to change item:"))
        change_human_items(change_id)
    else:
        print("Don't have this menu item")
        break
