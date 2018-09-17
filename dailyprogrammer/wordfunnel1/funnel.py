import sys

class WordFunnel:
    def __init__(self, word_list_filename):
        self.wordlist = self.parse_word_list(word_list_filename)

    def parse_word_list(self, filename):
        result = []
        with open(filename, 'r') as f:
            for line in f:
                result.append(line.strip().lower())
        return result

    @staticmethod
    def is_funnel(first, second):
        if len(second) >= len(first):
            return False

        if len(first) - len(second) != 1:
            return False

        for i in range(len(first)):
            if first[:i] + first[i+1:] == second:
                return True

        return False
    
    def find_list(self, given):
        result = set()
        for word in self.wordlist:
            if self.is_funnel(given, word):
                result.add(word)
        return list(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: funnel.py <path to word list>')
        exit(0)

    word_list_filename = sys.argv[1]

    wf = WordFunnel(word_list_filename)
    
    assert wf.is_funnel("leave", "eave")
    assert wf.is_funnel("reset", "rest")
    assert wf.is_funnel("dragoon", "dragon")
    assert not wf.is_funnel("eave", "leave")
    assert not wf.is_funnel("sleet", "lets")
    assert not wf.is_funnel("skiff", "ski")
    
    print wf.find_list("dragoon")  #  => ["dragon"]
    print wf.find_list("boats")  # => ["oats", "bats", "bots", "boas", "boat"]
    print wf.find_list("affidavit")  # => []
