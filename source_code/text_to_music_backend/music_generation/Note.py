from music_generation.ADSR import ADSR
from util.AnalysisConstants import pos_dict


class Note:

    def __init__(self, key, pos_code, max_note_duration, word_length, avg_word_length, word_sentiment):
        self.key = key
        self.pos_code = pos_code
        self.adsr = ADSR(max_note_duration, word_length, avg_word_length, word_sentiment)
        self.note_value = 0

    def generate_note(self):
        self.adsr.calibrate_adsr()
        self.note_value = self.key + pos_dict[self.pos_code]
