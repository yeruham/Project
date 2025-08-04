from src.Data_exploration import DataExploration
from src.loader import Loader
from src.writer import Writer

# load tweets_dataset.csv file to Data Frame
url = 'C:/python_data/TestProject/data/tweets_dataset.csv'
df = Loader.load_csv(url)
# object initialization of DataExploration with one column as a category ('Biased'), and a second column to analysis (''Text)
data_exploration = DataExploration(df, 'Text', 'Biased')

# all information about Text column by total df and category
num_by_category = data_exploration.num_by_category()
average_words = data_exploration.average_words()
common_words = data_exploration.common_words(10)
long_texts = data_exploration.long_texts(3)
num_upper_case_values = data_exploration.num_upper_case_values()

# dict with all this information
results = {"total_tweets": num_by_category,
           "average_length": average_words,
           "common_words": common_words,
           "longest_3_tweets": long_texts,
           "uppercase_words": num_upper_case_values
           }

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


# write all results to results.json file
Writer.write_json('../results/results.json', clear_information)


