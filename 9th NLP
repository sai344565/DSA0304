import nltk

# Define the PCFG probabilities
pcfg_probabilities = {
    "S": [("NP", "VP", 0.6)],
    "NP": [("Det", "N", 0.3), ("NP", "PP", 0.2)],
    "VP": [("V", "NP", 0.5), ("VP", "PP", 0.4)],
    "PP": [("PNP", 0.7)]
}

# Define the productions based on the probabilities
productions = []
for left, rights in pcfg_probabilities.items():
    for right in rights:
        if len(right) == 2:
            prob = right[1]
            right = right[0]
        else:
            prob = 1.0
        productions.append(nltk.Production(nltk.Nonterminal(left), right.split(), prob=prob))

# Define the PCFG grammar
pcfg_grammar = nltk.induce_pcfg(nltk.Nonterminal("S"), productions)

# Define the sentence
sentence = "The cat chased the mouse"

# Use the PCFG to parse the sentence
parser = nltk.ViterbiParser(pcfg_grammar)
parsed_trees = parser.parse(sentence.split())

# Print the parse trees
for tree in parsed_trees:
    print(tree)
