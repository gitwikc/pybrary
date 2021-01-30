from utils import Library
from data import save_data
from menu_flow_control import menu_flow


def main():
    library = Library()
    menu_flow({
        'New': library.create_new_book,
        'View': library.view_all_books,
        'Update': library.update_library(),
        'Delete': library.delete_book
    })
    save_data(library.df)


if __name__ == "__main__":
    main()
