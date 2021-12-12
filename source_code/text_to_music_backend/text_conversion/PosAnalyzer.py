import nltk
from util.AnalysisConstants import nltk_dict


class PosAnalyzer:
    def __init__(self):
        self.t=0

    #  based on list of words, create a list of pos codes as defined above
    def determine_pos_codes(self, words):
        return self.convert_to_pos_codes(nltk.pos_tag(words))

    def convert_to_pos_codes(self, pos_ntlks):
        pos_codes = []
        for pos_nltk in pos_ntlks:
            pos_codes.append(self.determine_pos_code(pos_nltk))
        return pos_codes

    def determine_pos_code(self, pos_nltk):
        pos_code = 99
        try:
            pos_code = nltk_dict[pos_nltk[1]]
        except Exception as err:
            print("Failed to determine pos code for: " + str(pos_nltk) + " err: " + str(err))
        return pos_code
