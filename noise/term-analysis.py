from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from inout.corpus_reader import CorpusReader
import math
import os
from nltk.corpus.reader.wordnet import WordNetError


class NoiseAnalyser(object):
    @staticmethod
    def extract_synsets_dist(year):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = current_dir + "/../data/logs/"

        # get the synsets from all of the year's tweets
        synsets = NoiseAnalyser.noise_quantifier(year)

        # construct the file for write access
        output = ""
        for synset in synsets:
            output += str(len(synset)) + "\n"
        file = open(data_dir + "synsets/" + str(year) + "_synset_dist.csv", "w")
        file.write(output)
        file.close()


    # quantifies the level of noise in the dataset
    @staticmethod
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


    @staticmethod
    def sense_similarity_quantifier(year):
        drought_sense = wn.synset("drought.n.01")

        # get the tweets from the respective dataset
        tweets = CorpusReader.read_post_2010_dataset(year)

        # for each tweet derive the number of synsets for each unique term in the tweet's text
        resnik_sims = []
        path_sims = []
        lch_sims = []
        wup_sims = []

        # preamble: load necessary corpus
        brown_ic = wordnet_ic.ic('ic-brown.dat')

        for tweet in tweets:
            # tokenise the tweet's text by whitespace
            tokens = tweet.text.split(" ")
            for token in tokens:
                try:
                    synsetsA = wn.synsets(token)
                    # for each synset, determine the distance with the drought_sense
                    for synset in synsetsA:
                        if synset is not synsetsA:
                            # Resnik sim
                            try:
                                resnik_sims.append(drought_sense.res_similarity(synset, brown_ic))
                            except WordNetError:
                                pass

                            # Path based sim
                            # try:
                            #     path_sims.append(drought_sense.path_similarity(synset))
                            # except WordNetError:
                            #     pass

                            # lch sim
                            try:
                                lch_sims.append(drought_sense.lch_similarity(synset))
                            except WordNetError:
                                pass

                            # # wup sim
                            # try:
                            #     wup_sims.append(drought_sense.wup_similarity(synset))
                            # except WordNetError:
                            #     pass
                    # print token + " ... " + str(synsetsA)
                except UnicodeDecodeError:
                    pass

        # write the distributions to disk
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = current_dir + "/../data/logs/"

        # Resnik
        resnik_sims_output = ""
        for sim in resnik_sims:
            resnik_sims_output += str(sim) + "\n"
        file = open(data_dir + "similarity/" + str(year) + "_resnik_dist.csv", "w")
        file.write(resnik_sims_output)
        file.close()

        # Path
        # paths_sims_output = ""
        # for sim in path_sims:
        #     paths_sims_output += str(sim) + "\n"
        # file = open(data_dir + "similarity/" + str(year) + "_path_dist.csv", "w")
        # file.write(paths_sims_output)
        # file.close()

        # LCH
        lch_sims_output = ""
        for sim in lch_sims:
            lch_sims_output += str(sim) + "\n"
        file = open(data_dir + "similarity/" + str(year) + "_lch_dist.csv", "w")
        file.write(lch_sims_output)
        file.close()

        # WUP
        # wup_sims_output = ""
        # for sim in wup_sims:
        #     wup_sims_output += str(sim) + "\n"
        # file = open(data_dir + "similarity/" + str(year) + "_wup_dist.csv", "w")
        # file.write(wup_sims_output)
        # file.close()


    @staticmethod
    def deriveCandidateTerms(year):
        # set the cutoffs for the years
        lch_settings = {2011: {"mu": 1.151493755, "sigma": 0.2281746702},
                        2012: {"mu": 1.145638145, "sigma": 0.2275964631}}
        z = float(2.576)

        lch_mean = lch_settings.get(year).get("mu")
        lch_sd = lch_settings.get(year).get("sigma")

        print lch_settings
        print lch_mean
        print lch_sd

        threshold = float(lch_mean) - (z * float(lch_sd))

        drought_sense = wn.synset("drought.n.01")

        # get the tweets from the respective dataset
        tweets = CorpusReader.read_post_2010_dataset(year)

        # for each tweet derive the number of synsets for each unique term in the tweet's text
        lch_sim_terms = set()

        # preamble: load necessary corpus
        brown_ic = wordnet_ic.ic('ic-brown.dat')

        for tweet in tweets:
            # tokenise the tweet's text by whitespace
            tokens = tweet.text.split(" ")
            for token in tokens:
                try:
                    synsetsA = wn.synsets(token)
                    # for each synset, determine the distance with the drought_sense
                    for synset in synsetsA:
                        if synset is not synsetsA:
                            # lch sim
                            try:
                                lch_distance = drought_sense.lch_similarity(synset)

                                # check if the distance is below the threshold
                                if lch_distance < threshold:
                                    lch_sim_terms.add(token)
                            except WordNetError:
                                pass

                    # print token + " ... " + str(synsetsA)
                except UnicodeDecodeError:
                    pass

        # write the distributions to disk
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = current_dir + "/../data/logs/"


        # LCH
        lch_sims_output = ""
        for token in lch_sim_terms:
            lch_sims_output += str(token) + "\n"
        file = open(data_dir + "similarity/" + str(year) + "_lch_terms_csv", "w")
        file.write(lch_sims_output)
        file.close()



years = [2011, 2012]
for year in years:
    # NoiseAnalyser.extract_synsets_dist(year)
    # NoiseAnalyser.sense_similarity_quantifier(year)
    NoiseAnalyser.deriveCandidateTerms(year)



