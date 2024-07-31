import nltk
import sys
import re
from nltk.tokenize import word_tokenize


# Define CFG terminals and non-terminals for sentence parsing
TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | VP | S P S | S Conj S
NP -> N | Det NP | AP NP | Conj NP | Adv NP | N NP | N Adv | N PP | Det AP NP
VP -> V | V NP | Adv VP | V Adv | VP PP
PP -> P NP
AP -> Adj | Adj AP
"""

# Non-terminal symbols explained:
# S = represents a sentence
# NP = represents a noun phrase
# VP = represents a verb phrase
# PP = represents a prepositional phrase
# AP = represents an adjective phrase
# The rules define various structures and combinations for sentence parsing.

# Create the CFG grammar and parser
grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():
    """
    Main function to read input sentence, preprocess it, parse it,
    and print the parse trees and noun phrase chunks.
    """
    # Check if a filename is specified as a command-line argument
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            sentence = f.read()
    else:
        sentence = input("Sentence: ")

    # Preprocess the input sentence
    words = preprocess(sentence)

    # Attempt to parse the sentence
    try:
        trees = list(parser.parse(words))
    except ValueError as e:
        print(e)
        return

    if not trees:
        print("Could not parse sentence.")
        return

    # Print each parse tree and noun phrase chunks
    for tree in trees:
        tree.pretty_print()
        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Preprocess the sentence by tokenizing, converting to lowercase, 
    and filtering out non-alphabetic tokens.

    Args:
        sentence (str): The input sentence to preprocess.

    Returns:
        list: A list of preprocessed word tokens.
    """
    # Tokenize the sentence into a list of words
    tokens = word_tokenize(sentence)
    # Convert each word to lowercase if it consists only of alphabetic characters
    new_tokens = [word.lower() for word in tokens if word.isalpha()]
    
    # # ====
    # # The following code is an alternative way to preprocess the sentence.
    # # It converts all characters to lowercase, removes digits, and extracts words without punctuation.
    
    # # Lower all characters in sentence
    # lower_sentence = sentence.lower()
    # # Remove all digits from sentence
    # new_sentence = re.sub(r'[0-9]', '', lower_sentence)
    # # Extract words from sentence without punctuation
    # words = re.findall(r'\w+', new_sentence)
    
    # # Print the words (for debugging purposes)
    # print(words)
    # return words
    # # ====

    # Return the preprocessed list of words
    return new_tokens

 

def np_chunk(tree):
    """
    Extract noun phrase chunks from a parse tree.

    Args:
        tree (Tree): The parse tree.

    Returns:
        list: A list of noun phrase subtrees.
    """
    noun_phrase_chunks = []
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            noun_phrase_chunks.append(subtree)
    return noun_phrase_chunks


if __name__ == "__main__":
    main()




# (.conda) (base) razvansavin@AEGIS:~/ProiecteVechi/CS50AI/parser$ python parser.py sentences/8.txt
#                      S                   
#          ____________|________            
#         |            |        S          
#         |            |        |           
#         |            |        VP         
#         |            |     ___|___        
#         S            |    |       NP     
#    _____|___         |    |    ___|___    
#   NP        VP       |    |   |       NP 
#   |      ___|___     |    |   |       |   
#   N     V      Adv  Conj  V  Det      N  
#   |     |       |    |    |   |       |   
# holmes sat     down and  lit his     pipe

# Noun Phrase Chunks
# holmes
# his pipe
# pipe
# (.conda) (base) razvansavin@AEGIS:~/ProiecteVechi/CS50AI/parser$ 