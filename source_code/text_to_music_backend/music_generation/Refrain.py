from util.AnalysisUtil import linear_mapping
from util.AnalysisConstants import min_sentiment, max_sentiment, min_sleep_multiplier, max_sleep_multiplier, \
    min_note_duration, max_note_duration, key_min, key_max
from music_generation.Note import Note


class Refrain:

    def __init__(self, pos_codes, word_lengths, word_sentiment_scores, sentence_length, average_sentence_length, sentence_sentiment_score, average_word_length):
        self.pos_codes = pos_codes
        self.word_lengths = word_lengths
        self.word_sentiment_scores = word_sentiment_scores
        self.sentence_length = sentence_length
        self.average_sentence_length = average_sentence_length
        self.sentence_sentiment_score = sentence_sentiment_score
        self.average_word_length = average_word_length
        self.sleep_multiplier = 0  # multiplied against sleep time (larger value makes beat slower)
        self.max_note_duration = 0
        self.notes = []
        self.key = 0

    def generate_refrain(self):
        self.sleep_multiplier = self.calculate_sleep_multiplier()
        self.max_note_duration = self.calculate_max_note_duration(self.sleep_multiplier)
        self.key = self.calculate_key()
        self.notes = self.create_notes(self.key, self.max_note_duration)

    def calculate_sleep_multiplier(self):
        multiplier = self.average_sentence_length / self.sentence_length  # longer sentences have smaller multipliers
        multiplier = min(multiplier, max_sleep_multiplier)
        multiplier = max(multiplier, min_sleep_multiplier)
        return round(multiplier, 2)

    def calculate_max_note_duration(self, sleep_multiplier):
        # duration = linear_mapping(sleep_multiplier, min_sleep_multiplier, max_sleep_multiplier, min_note_duration, max_note_duration)
        # return round(duration, 2)
        return max_note_duration

    def calculate_key(self):
        key = linear_mapping(self.sentence_sentiment_score, min_sentiment, max_sentiment, key_min, key_max)
        return round(key, 2)

    def create_notes(self, key, note_duration_max):
        notes = []
        for i in range(len(self.word_sentiment_scores)):
            note = Note(key, self.pos_codes[i], note_duration_max, self.word_lengths[i], self.average_word_length, self.word_sentiment_scores[i])
            note.generate_note()
            notes.append(note)
        return notes
