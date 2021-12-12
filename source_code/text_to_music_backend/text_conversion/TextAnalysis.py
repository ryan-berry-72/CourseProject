from statistics import mean


class TextAnalysis:

    def __init__(self, sentences, sentiment_analyzer, pos_analyzer):
        self.sentiment_analyzer = sentiment_analyzer
        self.pos_analyzer = pos_analyzer
        self.sentences = sentences  # a list of sentences where each sentence contains a list of words
        self.sentence_lengths = []  # count of words in each sentence
        self.word_lengths = []  # count of letters in each word
        self.avg_word_lengths = []  # avg number letters in the words in a sentence
        self.avg_sentence_length = None  # avg number of words in the list of sentences
        self.sentence_sentiment_scores = []  # score per sentence
        self.word_sentiment_scores = []  # score per word
        self.pos_codes = []  # part of speech code assigned to each word in each sentence

    def analyze_sentences(self):
        for sentence in self.sentences:
            self.sentence_lengths.append(len(sentence))
            sentiment = self.sentiment_analyzer.determine_sentiment(' '.join(word for word in sentence))
            self.sentence_sentiment_scores.append(sentiment)
            self.pos_codes.append(self.pos_analyzer.determine_pos_codes(sentence))
            char_counts = []
            sentence_word_sentiment_scores = []
            for word in sentence:
                char_counts.append(len(word))
                sentence_word_sentiment_scores.append(self.sentiment_analyzer.determine_sentiment(word))
            self.word_lengths.append(char_counts)
            self.word_sentiment_scores.append(sentence_word_sentiment_scores)
            self.avg_word_lengths.append(round(mean(char_counts), 2))
        self.avg_sentence_length = round(mean(self.sentence_lengths), 2)
