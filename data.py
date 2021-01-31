import pandas as pd


def get_data() -> pd.DataFrame:
    """
    Gets the data from the library.csv file as a pandas DataFrame
    """
    try:
        return pd.read_csv('library.csv')
    except FileNotFoundError as ex:
        return pd.DataFrame(columns=['name', 'author', 'genre', 'copies_total', 'copies_avail', 'reads'])


def save_data(df: pd.DataFrame, verbose: bool = False) -> None:
    """
    Saves the DataFrame to the 'library.csv' file

    :param df: The DataFrame containing the latest library data
    :param verbose: Decides if the save action is verbose
    """
    try:
        df.to_csv('library.csv', index=False)
    except:
        print('\N{cross mark} Oops, something went wrong')
    else:
        print('\N{party popper} Data successfully saved!')
