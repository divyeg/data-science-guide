from nltk.corpus import stopwords
from collections import Counter
import string


class StringHandler(object):
    def __init__(self):
        pass

    def remove_punnctuations_from_text(self, text):
        """
        This function is used to remove punctuations from text

        """
        punctuations = string.punctuation
        return text.translate(str.maketrans("", "", punctuations))

    def remove_punctuations_from_df(self, df, text_column):
        """
        This function is used to remove punctuations from a text column in pandas DataFrame

        """
        df["text_wo_punct"] = df[text_column].apply(
            lambda text: self.remove_punnctuations_from_text(text)
        )
        return df

    def remove_stop_words_from_text(self, text):
        """
        This function is used to remove punctuations from a text

        """
        stop_words = stopwords.words("english")
        return " ".join([word for word in str(text).split() if word not in stop_words])

    def remove_stop_words_from_df(self, df, text_column):
        """
        This function is used to remove stop words from a text column in pandas DataFrame

        """
        df["text_wo_stopwords"] = df[text_column].apply(
            lambda text: self.remove_stop_words_from_text(text)
        )
        return df

    def count_word_frequency_df(self, df, text_column):
        """
        This function is used to count word frequency from text column in pandas dataframe
        """
        count = Counter()
        for text in df[text_column].values:
            for word in text.split():
                count[word] += 1
        return count

    def remove_topn_frequent_words_text(self, text, counter, n):
        """
        This function is used to remove most frequent words from text

        """
        frequent_words = set([w for (w, wc) in counter.most_common[n]])
        return " ".join([word for word in text.split() if word not in frequent_words])

    def remove_topn_frequent_words_df(self, df, text_column, counter, n):
        """
        This function is used to remove most frequent words from text column in pandas dataframe

        """
        df["text_wo_stopfreq"] = df[text_column].apply(
            lambda text: self.remove_topn_frequent_words_text(text, counter, n)
        )
        return df
