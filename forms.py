def prompt(prompt_message: str, input_type, left_indent=24) -> str:
    """ Displays a prompt for a single input

    :param left_indent: The left align indentation of the prompt
    :param prompt_message: The message to display as a prompt
    :param input_type: The type of input required
    :return: The input from the user (of specified type)
    """
    while True:
        try:
            user_input = input_type(
                input(f"{(prompt_message + ' ') :<{left_indent}}"))
        except:
            continue
        return user_input


def form(form_fields: dict, header: str) -> dict:
    """ Displays a form for the user to fill

    :param form_fields: A dict containing field names and field data types as key-value pairs
    :param header: The header of the form
    :return: A dict containing field names and user inputs as key-value pairs
    """
    print(header.center(40))
    filled_form = {}
    for field in form_fields:
        field_name: str
        field_prompt: str

        if type(field) is tuple:
            field_name, field_prompt = field
        else:
            field_name = field_prompt = field

        input_type = form_fields[field]
        filled_form[field_name] = prompt(field_prompt, input_type)
    return filled_form


def menu(menu_items, header='MENU'):
    """ Displays a menu for the user to choose from

    :param menu_items: A list containing all menu items
    :param header: The menu header
    :return: A tuple containing the index of chosen item and the item
        in the format (index, item)
    """
    print(header.center(40))
    # Print the menu items
    for i, menu_item in enumerate(menu_items):
        print(f"{(str(i + 1) + '.') :<3} {menu_item}")

    # Validate the input
    user_choice = 0
    while (user_choice - 1) not in range(len(menu_items)):  # Accept only one of the options shown
        user_choice = prompt('>>>', int, left_indent=5)
    return user_choice - 1, menu_items[user_choice - 1]


def confirm(alert: str):
    """
    Displays a confirmation prompt to the user
    :param alert: The confirmation message
    :return: bool value whether the user confirmed or not
    """
    return menu(['Yes', 'No'], alert + '?')[0] == 0  # Yes chosen?
