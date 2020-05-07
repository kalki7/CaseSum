from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.parsers.plaintext import PlaintextParser

from sumy.summarizers.lex_rank import LexRankSummarizer 
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer
from sumy.summarizers.kl import KLSummarizer
from sumy.summarizers.reduction import ReductionSummarizer

from bow import bow


language = "english"

def extra(text,n,op):
    parser = PlaintextParser(text, Tokenizer(language))

    if op == 1:
        return(bow(text,n))
    elif op == 2:
        return(lexs(parser,n))

def lexs(parser,sentence_count):
    summarizer = LexRankSummarizer(Stemmer(language))
    summarizer.stop_words = get_stop_words(language)
    summary = summarizer(parser.document, sentence_count) 
    for sentence in summary:
        print(sentence)

def luhn(parser,sentence_count):
    summarizer_1 = LuhnSummarizer(Stemmer(language))
    summarizer_1.stop_words = get_stop_words(language)
    summary_1 = summarizer_1(parser.document, sentence_count)
    for sentence in summary_1:
        print(sentence)

def lsa(parser,sentence_count):
    summarizer_2 = LsaSummarizer(Stemmer(language))
    summarizer_2.stop_words = get_stop_words(language)
    summary_2 = summarizer_2(parser.document, sentence_count)
    for sentence in summary_2:
        print(sentence)

def textrank(parser,sentence_count):
    summarizer_3 = TextRankSummarizer(Stemmer(language))
    summarizer_3.stop_words = get_stop_words(language)
    summary_3 = summarizer_3(parser.document, sentence_count)
    for sentence in summary_3:
        print(sentence)

def sumbasic(parser, sentence_count):
    summarizer_5 = SumBasicSummarizer(Stemmer(language))
    summarizer_5.stop_words = get_stop_words(language)
    summary_5 = summarizer_5(parser.document, 5)
    for sentence in summary_5:
        print(sentence)

def klsum(parser, sentence_count):
    summarizer_6 = KLSummarizer(Stemmer(language))
    summarizer_6.stop_words = get_stop_words(language)
    summary_6 = summarizer_6(parser.document, sentence_count)
    for sentence in summary_6:
        print(sentence)

def reduction(parser, sentence_count):
    summarizer_7 = ReductionSummarizer(Stemmer(language))
    summarizer_7.stop_words = get_stop_words(language)
    summary_7 = summarizer_7(parser.document, sentence_count)
    for sentence in summary_7:
        print(sentence)