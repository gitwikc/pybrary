from types import FunctionType, MethodType
from forms import menu


def menu_flow(flow_dict: dict) -> None:
    """
    Controls the program control flow according to the flowchart dict.
    The flowchart dict is a tree of the menu options and the subsequent menus
    or functions to be executed on choice of the respective menu options.

    :param flow_dict: The dictionary defining the menu flow
    """
    # Get the options, and add the 'Exit' option in the end
    options = list(flow_dict.keys()) + ['Exit']

    '''
    The menu loops until exit is selected. Any other option chosen will create
    a menu flow for the sub tree provided as the value for that option.
    '''
    while True:
        choice = menu(options)
        print()
        if choice[0] == len(options) - 1:
            # User chooses 'Exit' (last option)
            break
        else:
            # Get the next step to do
            next_step = flow_dict[choice[1]]
            if type(next_step) is dict:
                # If there is a sub menu, call menu_flow on that one as well
                menu_flow(next_step)
            elif type(next_step) is FunctionType or type(next_step) is MethodType:
                # A function needs to be performed on choosing that option
                next_step()
        print()
