import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
import sys
from heapq import nlargest

import en_core_web_lg
nlp = en_core_web_lg.load()

stopwords = list(STOP_WORDS)

def calc_word_frequencies(doc):
    word_frequencies = {}
    for word in doc:
        if word.text not in stopwords and word.text not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    return word_frequencies

def get_max_frequency(word_frequencies):
    return max(word_frequencies.values())

def normalize_word_frequencies(word_frequencies):
    max_frequency = get_max_frequency(word_frequencies)
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/max_frequency)
    return word_frequencies

def get_sent_scores(sentence_list,word_frequencies):
    sentence_scores = {}  
    for i,sent in enumerate(sentence_list):  
        for word in sent:
            if word.text in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = [word_frequencies[word.text],i]
                else:
                    sentence_scores[sent][0] += word_frequencies[word.text]
    return sentence_scores

def generate_summary(doc,sents_in_summary):
    word_frequencies = calc_word_frequencies(doc)
    word_frequencies = normalize_word_frequencies(word_frequencies)
    sentence_scores = get_sent_scores([sent for sent in doc.sents],word_frequencies)
    
    #sorting according to decreasing order of importance and choosing the first (sents_in_summary) sentences
    summarized_sentences = sorted(sentence_scores.items(),key=lambda x: x[1],reverse=True)[:sents_in_summary]
    
    #sorting according to appearance of sentences in the original text
    summarized_sentences = sorted(summarized_sentences,key=lambda x: x[1][1])
    
    final_sentences = [x[0].text.capitalize() for x in summarized_sentences]
    summary = " ".join(final_sentences)
    return summary

if __name__ == "__main__":
    doc = '''

Employment. The Company hereby agrees to employ Employee, and Employee hereby agrees to render his exclusive service to the Company, in his current capacity of Senior Vice President and Chief Financial Officer of the Company, with such duties as may be assigned to him from time to time by the Board of Directors. Property of Company. All data, drawings, and other records and written material prepared or compiled by Employee or furnished to Employee while in the employ of the Company shall be the sole and exclusive property of the Company, and none of such data, drawings or other records, or copies thereof, shall be retained by Employee upon termination of his employment. Notwithstanding the foregoing, Employee shall be under no obligation to return public information. Indemnification; Directors and Officers Insurance. The Company shall (a) during the Employment Period and thereafter without limitation of time, indemnify and advance expenses to the Employee to the fullest extent permitted by the laws of the State of Nevada from time to time in effect and (b) during the Employment Period, acquire and maintain directors and offices liability insurance covering the Employee (and to the extent the Company desires, other directors and officers of the Company and its affiliated companies) to the extent it is available at commercially reasonable rates as determined by the Board; provided, however, that in no event shall the Employee be entitled to indemnification or advancement of expenses under this Paragraph 17 with respect to any proceeding, or matter therein, brought or made by the Employee against the Company other than one initiated by the Employee to enforce the Employee's advancement of expenses as provided in this Paragraph 17 shall not be deemed exclusive of any other rights to which the Employee may at any time be entitled under applicable law, the certificate of incorporation or bylaws of the Company, any agreement, a vote of stockholders, a resolution of the Board, or otherwise. The provisions of this Paragraph 17 shall continue in effect notwithstanding termination of the Employee's employment hereunder for any reason, including, without limitation, Employee's voluntary termination. In furtherance thereof, and not by way of limitation, the Company shall reimburse Employee for all reasonable legal fees and expenses incurred by Employee in connection with Employee's obtaining and enforcing any right or benefit provided by this Agreement. The reimbursement of such legal fees and expenses shall be made within 30 days after Employee's request for payment accompanied by evidence of the fees and expenses incurred. For a period of ten (10) years after the termination, for any reason, of Employee's employment with the Company, the Company shall indemnify, hold harmless and defend Employee, to the fullest extent permitted by applicable law, from and against any loss, cost or expense related to or arising out of any action or claim with respect to (i) the Company or its affiliated companies or (11) any action taken or omitted by the Employee (INCLUDING, BUT NOT LIMITED TO, MATTERS THAT CONSTITUTE NEGLIGENCE OF THE EMPLOYEE) for or on behalf of the Company or its affiliated companies, whether, in either case, such action or claim, or the facts and circumstances giving rise thereto, occurred or accrued before or after such termination of employment.

'''
    doc = nlp(doc.lower())
    # tokens = [token for token in doc]
    sents_in_summary = 1
    summary = generate_summary(doc,sents_in_summary)
    print (summary)