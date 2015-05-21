from datetime import datetime
from datatypes import Tweet


class CorpusReader(object):
    @staticmethod
    def read_post_2010_dataset(year):
        print "Running year: " + str(year)
        datasets_dir = "/home/rowem/Documents/Git/Data/Drought-Project/"
        dateFormatter = "%Y-%m-%d %H:%M:%S"
        file = open(datasets_dir + "drought_" + str(year) + "_corpus.csv", 'r')
        # each line should have 18 tokens - if not then the splitting is going to be erroneous
        correct_token_count = 18
        tweets = []
        for line in file:
            tokens = line.split(",")
            if len(tokens) == correct_token_count:
                try:
                    # tweet_id
                    tweet_id = tokens[12]
                    # userid
                    user_id = tokens[0]
                    # date
                    date_string = tokens[10]
                    date = datetime.strptime(date_string, dateFormatter)
                    # text
                    text = tokens[11].replace("\"", "").lower()
                    # location
                    location = tokens[3]

                    tweet = Tweet(tweet_id, user_id, date, text, location)
                    tweets.append(tweet)
                # handle the exception in case the number of tokens is the same as the correct number,
                # but the date still throws an exception
                except:
                    pass
        return tweets