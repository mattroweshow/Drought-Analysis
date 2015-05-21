from nltk.corpus import wordnet as wn
from inout.corpus_reader import CorpusReader
import math
import os

# quantifies the level of noise in the dataset
def noise_quantifier(year):
    # get the tweets from the respective dataset
    tweets = CorpusReader.read_post_2010_dataset(year)

    # for each tweet derive the number of synsets for each unique term in the tweet's text
    synsets = []
    for tweet in tweets:
        # tokenise the tweet's text by whitespace
        tokens = tweet.text.split(" ")
        for token in tokens:
            try:
                synsetsA = wn.synsets(token)
                # print token + " ... " + str(synsetsA)
                synsets.append(synsetsA)
            except UnicodeDecodeError:
                pass
    return synsets

years = [2011, 2012]
for year in years:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = current_dir + "/../data/logs/"

    # get the synsets from all of the year's tweets
    synsets = noise_quantifier(year)

    # construct the file for write access
    output = ""
    for synset in synsets:
        output += str(len(synset)) + "\n"
    file = open(data_dir + "synsets/" + str(year) + "_synset_dist.csv", "w")
    file.write(output)
    file.close()


