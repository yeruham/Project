import string


class Cleaner:

    def __init__(self, df):
        self.df = df


    def column_selection(self, columns: list):
        self.df = self.df[columns]


    def remove_punctuation_marks(self, column):
        symbols = string.punctuation
        for i in self.df.loc[:,column].index:
            new_text = ""
            for signal in self.df.loc[i, column]:
                if signal not in symbols:
                    new_text += signal
            self.df.loc[i, column] = new_text
