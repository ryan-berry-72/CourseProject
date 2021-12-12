min_sentiment = -1
max_sentiment = 1
min_sleep_multiplier = 1
max_sleep_multiplier = 2
min_note_duration = 0.2
max_note_duration = 0.7
key_min = 50
key_max = 70

# 0 = noun
# 1 = pronoun
# 2 = verb
# 3 = adverb
# 4 = adjective
# 5 = article_adj
# 6 = preposition
# 7 = number
# 99 = other
pos_dict = {
    0: 3,
    1: 1,
    2: 4,
    3: -1,
    4: -2,
    5: -5,
    6: -3,
    7: 10,
    99: 0
}

nltk_dict = {
    'CC': 99,
    'CD': 7,
    'DT': 5,
    'EX': 99,
    'FW': 99,
    'IN': 6,
    'JJ': 4,
    'JJR': 4,
    'JJS': 4,
    'LS': 99,
    'MD': 99,
    'NN': 0,
    'NNS': 0,
    'NNP': 0,
    'NNPS': 0,
    'PDT': 99,
    'POS': 99,
    'PRP': 1,
    'PRP$': 1,
    'RB': 3,
    'RBR': 3,
    'RBS': 3,
    'RP': 99,
    'TO': 6,
    'UH': 99,
    'VB': 2,
    'VBD': 2,
    'VBG': 2,
    'VBN': 2,
    'VBP': 2,
    'VBZ': 2,
    'WDT': 99,
    'WP': 1,
    'WP$': 1,
    'WRB': 3
}
