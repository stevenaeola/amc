# from https://stackoverflow.com/questions/603687/how-do-i-generate-sentences-from-a-formal-grammar

from nltk import CFG, ChartParser
from random import choice
import glob
import survey


def produce(grammar, symbol):
        words = []
        productions = grammar.productions(lhs = symbol)
        production = choice(productions)
        for sym in production.rhs():
            if isinstance(sym, str):
                words.append(sym)
            else:
                words.extend(produce(grammar, sym))
        return words

cfg_files = glob.glob("*.cfg")
cfg_files.append("exit")

while True:
    index = survey.routines.select('Pick a constraint: ', options = cfg_files)

    if index >= len(cfg_files) - 1:
        quit()

    cfg_file = cfg_files[index]

    with open(cfg_file, 'r') as file:
        file_content = file.read()
    grammar = CFG.fromstring(file_content)

    parser = ChartParser(grammar)

    gr = parser.grammar()
    print(' '.join(produce(gr, gr.start())))