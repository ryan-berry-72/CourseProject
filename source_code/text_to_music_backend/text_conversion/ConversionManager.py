from text_conversion.TextCleaner import clean_text, create_sentences
from text_conversion.TextAnalysis import TextAnalysis
from text_conversion.SentimentAnalyzer import SentimentAnalyzer
from text_conversion.PosAnalyzer import PosAnalyzer
from music_generation.Song import Song
from util.AnalysisUtil import print_object


def create_song(text, sentiment_analyzer=None):
    text = clean_text(text)
    sentences = create_sentences(text)
    if sentiment_analyzer is None:
        sentiment_analyzer = SentimentAnalyzer()
    text_analysis = TextAnalysis(sentences, sentiment_analyzer, PosAnalyzer())
    text_analysis.analyze_sentences()
    song = Song(text_analysis)
    song.generate_song()
    return song


def main():
    text = "This is an awesome sample! I hate cats."
    song = create_song(text)
    print("\n")
    print(song.package_parameters())


if __name__ == '__main__':
    main()
