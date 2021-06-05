from transformers import pipeline
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.kl import KLSummarizer


def get_abs_bart_model():
    return pipeline("summarization")

def get_abs_T5_model():
    return pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")

def get_ext_LexRank():
    return LexRankSummarizer()

def get_ext_Lsa():
    return LsaSummarizer()

def get_ext_Luhn():
    return LuhnSummarizer()

def get_ext_KL():
    return KLSummarizer()


