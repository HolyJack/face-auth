import numpy as np
import pandas as pd
from datetime import datetime
import warnings


class DataBase:
    BASE_DIR = './logins.pckl'
    columns = ['login', 'embedding', 'last_update']

    def __init__(self) -> None:
        try:
            self.df = pd.read_pickle(self.BASE_DIR)
            self.df.reset_index(drop=True, inplace=True)
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=['login', 'embedding', 'last_update'])
            self.save()

    def add_new_face(self, login: str, embedding: np.array):
        time = datetime.isoformat(datetime.now(), timespec = 'seconds', sep=' ')
        if login in set(self.df.login):
            warnings.warn('Login already in database. Use update_face method to add new user.')
            return 

        new_row = pd.DataFrame([[login, [embedding], time]], columns=self.columns)
        self.df = pd.concat([self.df, new_row])
        self.df.reset_index(drop=True, inplace=True)
        self.save()

    def update_face(self, login: str, embedding: np.array):
        if login not in set(self.df.login):
            warnings.warn('No such login in database. Use add_new_face method to update user face.')
            return

        self.df = self.df[self.df.login != login]
        self.add_new_face(login, embedding)
        self.save()

    def delete_user(self, login):
        self.df = self.df[self.df.login != login]
        self.save()

    def get(self, login: str) -> np.array:
        return self.df.embedding[self.df.login == login]

    def get_all(self):
        return self.df.embedding

    def count(self) -> int:
        return self.df.shape[0]

    def clear(self):
        self.df = pd.DataFrame(columns=['login', 'embedding', 'last_update'])
        self.save()

    def save(self):
        self.df.to_pickle(self.BASE_DIR)
