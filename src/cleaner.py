import string


class Cleaner:

    def __init__(self, df):
        self.df = df


    def column_selection(self, columns: list):
        self.df = self.df[columns]


    def remove_punctuation_marks(self, column):
        symbols = string.punctuation
        # symbols = '[!#$%&()*+-./:;<=>?@[\]^_`{|}~]'
        # self.df[column] = self.df[column].str.replace(symbols, "")
        for i in self.df.loc[:,column].index:
            new_text = ""
            for signal in self.df.loc[i, column]:
                if signal not in symbols:
                    new_text += signal
            self.df.loc[i, column] = new_text


    def convert_to_lowercase(self, column):
        self.df.loc[:, column] = self.df.loc[:, column].map(str.lower)


    def remove_by_category(self, category):
        self.df = self.df[~self.df[category].isna()]


