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
        by_category = {"total": int(self.df[self.analysis_column].count())}
        series_of_category = self.df[self.category]
        by_category.update(series_of_category.value_counts().to_dict())
        return by_category


    def average_words(self):
        average_values = {}
        for category in self.by_category:

            if category != "total":
                df = self.df[self.df[self.category] == category]
            else:
                df = self.df

            sum_all = 0
            for text in df[self.analysis_column]:
                words = text.split()
                sum_all += len(words)
            average_values[category] = sum_all / df.shape[0]

        return  average_values


    def long_texts(self, num_texts):
        long_texts_by_category = {}
        for category in self.by_category:
            if category == "total":
                continue

            df = self.df[self.df[self.category] == category]
            new_df = pd.DataFrame(df[self.analysis_column]).reset_index()
            long_texts = []

            for i in new_df.index:
                new_df.loc[i, 'length_text'] = len(new_df.loc[i, self.analysis_column])

            new_df = new_df.sort_values(by='length_text', ascending=False)

            for i in range(0, num_texts):
                long_texts.append(new_df.loc[i, self.analysis_column])

            long_texts_by_category[category] = long_texts

        return long_texts_by_category



    # def func_by_category(self, func, num, including_total: bool):
    #     info_by_category = {}
    #     for category in self.by_category:
    #         if category == 'total':
    #             if not including_total:
    #                continue
    #
    #         df = self.df[self.df[self.category] == category]
    #         new_df = pd.DataFrame(df[self.analysis_column]).reset_index()
    #
    #         info = func(df, num)
    #         info_by_category[category] = info
    #
    #     return info_by_category


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

        df_of_amount_of_words = pd.DataFrame({'word': words, 'amount': amount_of_words})
        df_of_amount_of_words = df_of_amount_of_words.sort_values(by='amount', ascending=False).reset_index()

        common_words = df_of_amount_of_words.loc[:num_words, 'word'].to_list()
        return common_words


    def upper_case_values(self):
        uppercase_words = {}
        for category in self.by_category:
            if category != "total":
                df = self.df[self.df[self.category] == category]
            else:
                df = self.df

            series = df[self.analysis_column]
            num_upper_case = 0
            for text in series:
                words = text.split()
                for word in words:
                    if word.isupper():
                        num_upper_case += 1

            uppercase_words[category] = num_upper_case

        return uppercase_words




