
class Tweet():
    def __init__(self, tweet_id, user_id, date, text, location):
        self.tweet_id = tweet_id
        self.user_id = user_id
        self.date = date
        self.text = text
        self.location = location

    def __str__(self):
        return str(self.tweet_id) + " - " + str(self.user_id) + " - " + str(self.date) + " - " + str(self.text) \
               + " - " + str(self.location)