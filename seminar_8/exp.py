def expp(last_name):
    with open("C:\\Users\\mamet\\Documents\\GeekBrainsEducation\\Python_education\\seminar_8\\info.txt", "r", encoding="utf-8") as f:
        info_list = f.read().splitlines()
        for person in info_list:
            if last_name in person:
                print(person)
