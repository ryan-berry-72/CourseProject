from music_generation.Refrain import Refrain


class Song:

    def __init__(self, text_analysis):
        self.text_analysis = text_analysis
        self.refrains = []
        self.sleep_multipliers = []
        self.note_values = []
        self.notes_adsr = []

    def generate_song(self):
        self.refrains = self.create_refrains()
        for i in range(len(self.refrains)):
            self.sleep_multipliers.append(self.refrains[i].sleep_multiplier)
            notes = self.refrains[i].notes
            note_values = []
            notes_adsr = []
            for j in range(len(notes)):
                note_values.append(notes[j].note_value)
                adsr = notes[j].adsr
                notes_adsr.append(adsr.get_adsr_values())
            self.note_values.append(note_values)
            self.notes_adsr.append(notes_adsr)

    def create_refrains(self):
        refrains = []
        for i in range(len(self.text_analysis.sentences)):
            pos_codes = self.text_analysis.pos_codes[i]
            word_lengths = self.text_analysis.word_lengths[i]
            word_sentiment_scores = self.text_analysis.word_sentiment_scores[i]
            sentence_length = self.text_analysis.sentence_lengths[i]
            avg_sentence_length = self.text_analysis.avg_sentence_length
            sentence_sentiment = self.text_analysis.sentence_sentiment_scores[i]
            avg_word_length = self.text_analysis.avg_word_lengths[i]
            refrain = Refrain(pos_codes, word_lengths, word_sentiment_scores, sentence_length, avg_sentence_length, sentence_sentiment, avg_word_length)
            refrain.generate_refrain()
            refrains.append(refrain)
        return refrains

    def package_parameters(self):
        return "note_values = " + str(self.note_values) + "\nnotes_adsr = " + str(self.notes_adsr) + "\nsleep_multipliers = " + str(self.sleep_multipliers)

    def to_dict(self):
        return {"note_values": str(self.note_values),
                "notes_adsr": str(self.notes_adsr),
                "sleep_multipliers": str(self.sleep_multipliers)}
