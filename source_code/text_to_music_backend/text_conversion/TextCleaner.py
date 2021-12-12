import re
import string
import contractions
from text_conversion.TextAnalysis import TextAnalysis
from text_conversion.SentimentAnalyzer import SentimentAnalyzer
from text_conversion.PosAnalyzer import PosAnalyzer
from util.AnalysisUtil import print_object

alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|Mt)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov|me|edu)"


# many libraries exist to accomplish this, but I'm trying out an interesting approach in an answer posted here:
# https://stackoverflow.com/questions/4576077/how-can-i-split-a-text-into-sentences
def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences


# https://towardsdatascience.com/a-guide-to-cleaning-text-in-python-943356ac86ca
def convert_to_ascii(text):
    # encoding the text to ASCII format
    text_encode = text.encode(encoding="ascii", errors="ignore")
    # decoding the text
    text_decode = text_encode.decode()
    # cleaning the text to remove extra whitespace
    clean_text = " ".join([word for word in text_decode.split()])
    return clean_text


# https://www.geeksforgeeks.org/nlp-expand-contractions-in-text-processing/
def expand_contractions(text):
    # creating an empty list
    expanded_words = []
    for word in text.split():
        # using contractions.fix to expand the shortened words
        expanded_words.append(contractions.fix(word))
    return ' '.join(expanded_words)


punctuation = set(string.punctuation)
def remove_punctuation(text):
    return "".join([ch for ch in text if ch not in punctuation])


def clean_text(text):
    text = text.strip()
    text = convert_to_ascii(text)
    text = ensure_ends_with_punctuation(text)
    return expand_contractions(text)


def ensure_ends_with_punctuation(text):
    if not any(text.endswith(s) for s in [".", "!", "?"]):
        text = text + "."
    return text


def create_sentences(text):
    sentences = split_into_sentences(text)
    if len(sentences) == 0:
        sentences = [text]
    for i in range(len(sentences)):
        sentences[i] = remove_punctuation(sentences[i])
        sentences[i] = sentences[i].split()  # convert sentence strings into lists of words
    return sentences
