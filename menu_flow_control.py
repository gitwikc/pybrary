from types import FunctionType, MethodType
from forms import menu


def menu_flow(flowchart: dict) -> None:
    """ Controls the program control flow according to the flowchart dict.
    The flowchart dict is a tree of the menu options and the subsequent menus
    or functions to be executed on choice of the respective menu options.

    :param flowchart: The dictionary defining the menu flow
    """
    # Get the options, and add the 'Exit' option in the end
    options = list(flowchart.keys()) + ['Exit']

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
            next_step = flowchart[choice[1]]
            if type(next_step) is dict:
                # If there is a sub menu, call menu_flow on that one as well
                menu_flow(next_step)
            elif type(next_step) is FunctionType or type(next_step) is MethodType:
                # A function needs to be performed on choosing that option
                next_step()
        print()


if __name__ == "__main__":
    flowchart = {
        'morning': {
            '8.00 am': lambda: print('Nice time to wake up'),
            '10.00 am': lambda: print('Yeah, just ok...'),
            '11.00 am': lambda: print('It is breakfast time now')
        },
        'evening': {
            '7.00 pm': {
                'rainy?': {
                    'Board games': {
                        'Chess': lambda: print('See you on the board'),
                        'Ludo': lambda: print("We'll see how lucky you are, then")
                    },
                    'Video games': {
                        'PS4': lambda: print("Let's play 'Ghost Of Tsushima'"),
                        'XBOX': lambda: print("Let's play 'Minecraft Dungeons'")
                    }
                },
                'cool?': lambda: print('Go for a walk')
            },
            '9.00 pm': lambda: print('Watch a show with friends/family')
        },
        'night': {
            '10.00 pm': lambda: print('Have dinner'),
            '11.00 pm': {
                'sleepy?': lambda: print('Good night'),
                'not sleepy?': lambda: print('Watch a late night movie then')
            }
        }
    }
    menu_flow(flowchart)
