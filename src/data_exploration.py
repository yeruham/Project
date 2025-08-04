import pandas as pd


class DataExploration:

    # Basic exploration of the data

    def __init__(self, df, analysis_column,  category):
        # Gets dataFrame and two columns out of it -
        # one for investigation, second as a category
        self.df = df
        self.analysis_column = analysis_column
        self.category = category
        self.by_category = self.num_by_category()



    def num_by_category(self):
        by_category = self.df.groupby(self.category)[self.analysis_column].count().to_dict()
        return by_category


    def num_by_total_and_category(self):
        by_all = {"total": int(self.df[self.analysis_column].count())}
        by_all.update(self.by_category)
        return by_all

    def average_words(self, df):

            sum_all = 0
            for text in df[self.analysis_column]:
                words = text.split()
                sum_all += len(words)

            return sum_all / df.shape[0]



    def long_texts(self, df, num_texts):

            new_df = pd.DataFrame(df[self.analysis_column]).reset_index()
            long_texts = []

            for i in new_df.index:
                new_df.loc[i, 'length_text'] = len(new_df.loc[i, self.analysis_column])

            new_df = new_df.sort_values(by='length_text', ascending=False)

            for i in range(0, num_texts):
                long_texts.append(new_df.loc[i, self.analysis_column])

            return long_texts


    def common_words(self, num_words):
        quantity_by_words = {}
        series = self.df[self.analysis_column]
        for i in series.index:
            words = series[i].split()
            for word in words:
                try:
                    quantity_by_words[word] += 1
                except:
                    quantity_by_words[word] = 1


        words = []
        amount_of_words = []
        for word, amount in quantity_by_words.items():
            words.append(word)
            amount_of_words.append(amount)

        df_amount_of_words = pd.DataFrame({'word': words, 'amount': amount_of_words})
        df_amount_of_words = df_amount_of_words.sort_values(by='amount', ascending=False).reset_index()

        common_words = df_amount_of_words.loc[:num_words, 'word'].to_list()
        return common_words


    def num_upper_case_values(self, df):

            series = df[self.analysis_column]
            num_upper_case = 0
            for text in series:
                words = text.split()
                for word in words:
                    if word.isupper():
                        num_upper_case += 1

            return num_upper_case



    def func_by_total_or_category(self, func, total: bool, category: bool, num= None):
        information = {}
        if total:
            if num:
                results = func(self.df, num)
            else:
                results = func(self.df)
            information['total'] = results
        if category:
            for c in self.by_category:
                df = self.df[self.df[self.category] == c]
                if num:
                    results = func(df, num)
                else:
                    results = func(df)

                information[c] = results

        return information

