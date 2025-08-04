import json
from src.Data_exploration import DataExploration
from src.loader import Loader

url = 'C:/python_data/TestProject/data/tweets_dataset.csv'

df = Loader.load_csv(url)

data_exploration = DataExploration(df, 'Text', 'Biased')

num_by_category = data_exploration.num_by_category()
average_words = data_exploration.average_words()
long_texts = data_exploration.long_texts(3)
common_words = data_exploration.common_words(10)
num_upper_case_values = data_exploration.num_upper_case_values()

results = {"total_tweets": num_by_category,
           "average_length": average_words,
           "common_words": common_words,
           "longest_3_tweets": long_texts,
           "uppercase_words": num_upper_case_values
           }

# for data in results:
#     for value in results[data]:
#         if value == 1:
#             results[data]["antisemitic"] = results[data][value]
#         if value == 0:
#             # copy_value = {"non_antisemitic": results[data][value]}
#             results[data]["non_antisemitic"] = results[data][value]
#             # results[data][value] = copy_value


json_results = json.dumps(results)

with open( '../results/results.json', 'w') as f:
    json.dump(results, f)

