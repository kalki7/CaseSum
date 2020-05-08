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
from tfidf import tfidf


language = "english"

def extra(text,n,op):
    parser = PlaintextParser(text, Tokenizer(language))

    if op == 1:
        return(bow(text,n))
    elif op == 2:
        return(lexs(parser,n))
    elif op == 3:
        return(luhn(parser,n))
    elif op == 4:
        return(lsa(parser,n))
    elif op == 5:
        return(textrank(parser,n))
    elif op == 6:
        return(sumbasic(parser,n))
    elif op == 7:
        return(klsum(parser,n))
    elif op == 8:
        return(reduction(parser,n))
    elif op ==9:
        return(tfidf(text,n))


def lexs(parser,sentence_count):
    summarizer = LexRankSummarizer(Stemmer(language))
    summarizer.stop_words = get_stop_words(language)
    summary = summarizer(parser.document, sentence_count) 
    temp = ''
    for sentence in summary:
        temp = temp + str(sentence)
    return (temp)

def luhn(parser,sentence_count):
    summarizer_1 = LuhnSummarizer(Stemmer(language))
    summarizer_1.stop_words = get_stop_words(language)
    summary_1 = summarizer_1(parser.document, sentence_count)
    temp = ''
    for sentence in summary_1:
        temp = temp + str(sentence)
    return (temp)

def lsa(parser,sentence_count):
    summarizer_2 = LsaSummarizer(Stemmer(language))
    summarizer_2.stop_words = get_stop_words(language)
    summary_2 = summarizer_2(parser.document, sentence_count)
    temp = ''
    for sentence in summary_2:
        temp = temp + str(sentence)
    return (temp)

def textrank(parser,sentence_count):
    summarizer_3 = TextRankSummarizer(Stemmer(language))
    summarizer_3.stop_words = get_stop_words(language)
    summary_3 = summarizer_3(parser.document, sentence_count)
    temp = ''
    for sentence in summary_3:
        temp = temp + str(sentence)
    return (temp)

def sumbasic(parser, sentence_count):
    summarizer_5 = SumBasicSummarizer(Stemmer(language))
    summarizer_5.stop_words = get_stop_words(language)
    summary_5 = summarizer_5(parser.document, 5)
    temp = ''
    for sentence in summary_5:
        temp = temp + str(sentence)
    return (temp)

def klsum(parser, sentence_count):
    summarizer_6 = KLSummarizer(Stemmer(language))
    summarizer_6.stop_words = get_stop_words(language)
    summary_6 = summarizer_6(parser.document, sentence_count)
    temp = ''
    for sentence in summary_6:
        temp = temp + str(sentence)
    return (temp)

def reduction(parser, sentence_count):
    summarizer_7 = ReductionSummarizer(Stemmer(language))
    summarizer_7.stop_words = get_stop_words(language)
    summary_7 = summarizer_7(parser.document, sentence_count)
    temp = ''
    for sentence in summary_7:
        temp = temp + str(sentence)
    return (temp)