import pandas as pd
from matplotlib import style as st, pyplot as plt

from data import get_data
from forms import confirm, form, prompt

st.use('ggplot')

# Set pandas option to show all rows
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


class Library:
    df: pd.DataFrame

    def __init__(self) -> None:
        self.df = get_data()

    def view_all_books(self):
        print(self.df)

    def create_new_book(self):
        self.df = self.df.append(new_book_form(), ignore_index=True)
        print(f"Successfully created book {self.df.name.values[-1]} ({self.df.genre.values[-1]})")

    def delete_book(self):
        self.view_all_books()
        choice = -1
        while choice not in self.df.index:
            choice = prompt('Choose a book (index):', int)
        if confirm(f"Are you sure you want to delete the book '{self.df.name[choice]}'"):
            self.df = self.df.drop(index=choice)
            print(
                f"Successfully deleted book '{self.df.name[choice]}' by {self.df.author[choice]}")
        else:
            print('Delete action cancelled')

    def update_library(self) -> dict:
        def borrow_book():
            # Print all available books
            available = self.df[self.df.copies_avail > 0]
            print(available[['name', 'author', 'genre']])
            choice = -1
            while choice not in available.index:
                choice = prompt('Choose a book (index):', int)
            self.df.at[choice, 'copies_avail'] -= 1  # Reduce copies available by 1
            self.df.at[choice, 'reads'] += 1  # Increase no. of reads by 1
            print(
                f"Borrowed a copy of '{self.df.name[choice]}' by {self.df.author[choice]}")

        def return_book():
            # Print all available books
            available = self.df[self.df.copies_avail < self.df.copies_total]
            print(available[['name', 'author', 'genre']])
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

    def view_graphs(self) -> dict:
        """
        Display graphs visualizing the library data. The user can choose from:
        1. Bar graph of genre v/s no. of books
        2. Bar graph of genre v/s no. of reads

        :return: A sub-menu dict giving the user choices for which graph to view
        """
        def get_graphing_func_genre_vs(field: str):
            """
            Creates a function that displays a bar graph of:
            Genre v/s <field> -> ('copies_total' or 'reads')
            """
            def graph_genre_vs_field():
                data_by_genre = self.df.groupby('genre')
                genre_books = data_by_genre[field].sum()
                ylabel = {'copies_total': 'No. of books', 'reads': 'No. of times read'}.get(field)

                # Plotting and graph config
                plt.bar(genre_books.index, genre_books.values, color='#fa2b5c', width=0.2)
                plt.xlabel('Genre')
                plt.ylabel(ylabel)
                plt.title(f'Graph of Genre v/s {ylabel}')
                plt.show()
            # Return the function that displays the required graph
            return graph_genre_vs_field

        # Return the submenu
        return {
            'genre v/s no. of books': get_graphing_func_genre_vs("copies_total"),
            'genre v/s no. of reads': get_graphing_func_genre_vs("reads")
        }


def new_book_form() -> dict:
    book_form = form(header='New Book', form_fields={
        ('name', 'Name'): str,
        ('author', 'Author'): str,
        ('genre', 'Genre'): str,
        ('copies_total', 'Total copies'): int
    })
    book_form['copies_avail'] = book_form['copies_total']
    book_form['reads'] = 0

    return book_form
