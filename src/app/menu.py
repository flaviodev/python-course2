def show_menu(str_title, dict_options, dict_functions):
    while(1):
        print_title(str_title)
        print_menu_title()
        print_menu_options(dict_options)
        chosen_option = get_chosen_option()
        
        try:
            if(int(chosen_option) == 0):
                break
        
            execute_chosen_option(chosen_option, dict_functions)
        except:
            continue


def print_title(str_title):
    print("---------------------------------------------------------------")
    print(str_title)
    print("---------------------------------------------------------------")

def print_menu_title():
    print("Menu")

def print_menu_options(dict_options):
    for option in dict_options:
        print('({}) {}'.format(option,dict_options[option]))
    print('(0) Exit')

def get_chosen_option():
    return input("Choose an option: ")

def execute_chosen_option(str_option, dict_functions):
    try:
        option = int(str_option)
        if(option in dict_functions):
            dict_functions[option].run()
        else:
            raise Exception()
    except:
        print("You must type a valid option!")
        raise Exception()
