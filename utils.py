from typing import ValuesView
from data import get_data
from forms import confirm, form, prompt
import pandas as pd

# Set pandas option to show all rows
pd.set_option('display.max_rows', None)


class Library:
    df: pd.DataFrame

    def __init__(self) -> None:
        self.df = get_data()

    def view_all_books(self):
        print(self.df)

    def create_new_book(self):
        self.df = self.df.append(new_book_form(), ignore_index=True)
        print(
            f"Successfully created book {self.df.name.values[-1]} ({self.df.genre.values[-1]})")

    def delete_book(self):
        self.view_all_books()
        choice = -1
        while choice not in self.df.index:
            choice = prompt('Choose a book (index):', int)
        if confirm(f"Are you sure you want to remove the book '{self.df.name[choice]}'"):
            self.df = self.df.drop(index=choice)
            print(
                f"Successfully deleted book '{self.df.name[choice]}' by {self.df.author[choice]}")
        else:
            print('Delete action cancelled')

    def update_library(self) -> dict:
        def borrow_book():
            # Print all available books
            available = self.df[self.df.copies_avail > 0]
            print(available)
            choice = -1
            while choice not in available.index:
                choice = prompt('Choose a book (index):', int)
            self.df.at[choice, 'copies_avail'] -= 1
            print(
                f"Borrowed a copy of '{self.df.name[choice]}' by {self.df.author[choice]}")

        def return_book():
            # Print all available books
            available = self.df[self.df.copies_avail < self.df.copies_total]
            print(available)
            choice = -1
            while choice not in available.index:
                choice = prompt('Choose a book (index):', int)
            self.df.at[choice, 'copies_avail'] += 1
            print(
                f"Returned a copy of '{self.df.name[choice]}' by {self.df.author[choice]}")

        return {
            'Borrow book': borrow_book,
            'Return book': return_book
        }


def new_book_form() -> dict:
    book_form = form(header='New Book', form_fields={
        ('name', 'Name'): str,
        ('author', 'Author'): str,
        ('genre', 'Genre'): str,
        ('copies_total', 'Total copies'): int
    })
    book_form['copies_avail'] = book_form['copies_total']

    return book_form
