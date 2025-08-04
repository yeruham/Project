from src.cleaner import Cleaner
from src.data_exploration import DataExploration
from src.loader import Loader
from src.writer import Writer


def get_df_information(analysis_column, category):
    # object initialization of DataExploration with one column as a category ('Biased'), and a second column to analysis (''Text)
    data_exploration = DataExploration(df, analysis_column, category)

    # all information about Text column by total df and category
    num_by_category = data_exploration.num_by_total_and_category()
    average_words = data_exploration.func_by_total_or_category(data_exploration.average_words, total=True, category=True)
    common_words = data_exploration.common_words(10)
    long_texts = data_exploration.func_by_total_or_category(data_exploration.long_texts, total=False, category=True, num=3)
    num_upper_case_values = data_exploration.func_by_total_or_category(data_exploration.num_upper_case_values, total=True, category=True)

    # dict with all this information
    results = {"total_tweets": num_by_category,
               "average_length": average_words,
               "common_words": common_words,
               "longest_3_tweets": long_texts,
               "uppercase_words": num_upper_case_values
               }

    return results


def change_names_keys(results):
    # copy results dict to new one -  all '1' key turns into 'antisemitic' and all '0' key turns into 'non_antisemitic'
    clear_information = {}
    for data in results:
        clear_information[data] = {}
        if isinstance(results[data], dict):
            for value in results[data]:
                if value == 1:
                    clear_information[data]["antisemitic"] = results[data][value]
                elif value == 0:
                    clear_information[data]["non_antisemitic"] = results[data][value]
                else:
                    clear_information[data][value] = results[data][value]
        else:
            clear_information[data] = results[data]

    return clear_information


def clean_df(df):
    cleaner = Cleaner(df)
    cleaner.column_selection([analysis_column, category])
    cleaner.remove_punctuation_marks(analysis_column)
    cleaner.convert_to_lowercase(analysis_column)
    cleaner.remove_by_category(category)
    return cleaner.df





if __name__ =='__main__':

    # load tweets_dataset.csv file to Data Frame
    url = 'C:/python_data/TestProject/data/tweets_dataset.csv'
    df = Loader.load_csv(url)

    # select specific columns for analysis and category
    analysis_column = 'Text'
    category = 'Biased'

    # get to all information about analysis column by category
    results = get_df_information(analysis_column, category)
    clear_information = change_names_keys(results)

    # write all results to results.json file
    Writer.write_json('../results/results.json', clear_information)

    # clean the df and save it in results
    clean_df = clean_df(df)
    clean_df.to_csv('../results/tweets_dataset_cleaned.csv')

    data_exploration = DataExploration(df, analysis_column, category)





