import sys
from dailyprogrammer.wordfunnel1.funnel import WordFunnel

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: funnel.py <path to word list>')
        exit(0)

    word_list_filename = sys.argv[1]

    wf = WordFunnel(word_list_filename)
    assert wf.funnel_length("gnash") == 4
    assert wf.funnel_length("princesses") == 9
    assert wf.funnel_length("turntables") == 5
    assert wf.funnel_length("implosive") == 1
    assert wf.funnel_length("programmer") == 2
