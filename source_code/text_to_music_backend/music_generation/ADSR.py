from util.AnalysisUtil import print_object, linear_mapping, contain_value_in_range
from util.AnalysisConstants import min_sentiment, max_sentiment

# Sonic Pi’s ADSR envelopes have the following phases:
# attack - time from 0 amplitude to the attack_level,
# decay - time to move amplitude from attack_level to decay_level,
# sustain - time to move the amplitude from decay_level to sustain_level,
# release - time to move amplitude from sustain_level to 0
# the duration of a note is the summation of these four note phases


# This class controls each note's amplitude over time
class ADSR:
    def __init__(self, max_note_duration, word_length, average_word_length, word_sentiment):
        self.max_note_duration = max_note_duration  # all times are in seconds
        self.word_length = word_length
        self.average_word_length = average_word_length
        self.word_sentiment = word_sentiment
        self.attack = 0
        self.decay = 0  # not using decay
        self.sustain = 0
        self.release = 0
        self.phases = 3  # attack, release, sustain
        self.standard_phase_duration = round(self.max_note_duration / self.phases, 2)
        self.note_duration = 0

    def calibrate_adsr(self):
        self.attack = self.calculate_attack()
        self.decay = self.calculate_decay()
        self.sustain = self.calculate_sustain()
        self.release = self.calculate_release(self.attack)
        self.note_duration = self.calculate_note_duration()

    #  lower attack value indicates more aggressive sound
    def calculate_attack(self):
        phase_min = 0
        phase_max = self.standard_phase_duration
        phase_duration = linear_mapping(self.word_sentiment, min_sentiment, max_sentiment, phase_min, phase_max)
        return round(phase_duration, 2)

    def calculate_decay(self):
        return 0  # not using decay

    def calculate_sustain(self):
        wl_index_min = 0
        wl_index_max = 2
        phase_min = self.standard_phase_duration/4  # last for at least a quarter of the allotted time
        phase_max = self.standard_phase_duration
        wl_index = self.word_length / self.average_word_length  # larger word -> longer duration
        wl_index = contain_value_in_range(wl_index, wl_index_min, wl_index_max)
        phase_duration = linear_mapping(wl_index, wl_index_min, wl_index_max, phase_min, phase_max)
        return round(phase_duration, 2)

    #  lower release value indicates a more aggressive falling off
    def calculate_release(self, attack):
        phase_max = self.standard_phase_duration
        return round(phase_max - attack, 2)

    def calculate_note_duration(self):
        duration = self.attack + self.decay + self.sustain + self.release
        if duration > self.max_note_duration:
            print("Error - note duration: " + str(duration) + " greater than allowed: " + str(self.max_note_duration))
        return round(duration, 2)

    def get_adsr_values(self):
        adsr_values = [self.attack, self.decay, self.sustain, self.release]
        return adsr_values


def main():
    print("LM", linear_mapping(0.7, -1, 1, 0, 0.2))
    adsr = ADSR(0.5, 5, 3.4, 0.99)
    adsr.calibrate_adsr()
    print_object(adsr)


if __name__ == '__main__':
    main()
