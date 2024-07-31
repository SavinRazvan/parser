# Parser

## Overview
The Parser project focuses on implementing a context-free grammar (CFG) parser to analyze English sentences and extract noun phrases. The goal is to build a tool that can interpret sentence structures and provide insights into their grammatical components.

## Features
- **Context-Free Grammar Parsing**: Utilizes CFG to decompose sentences into their grammatical elements.
- **Noun Phrase Extraction**: Identifies and extracts noun phrases based on CFG rules.
- **Tokenization and Normalization**: Processes sentences into tokens and normalizes them for consistent analysis.

## Requirements
- Python 3
- `nltk` library

## Setup
1. **Install NLTK**:
   ```bash
   pip install nltk
   ```
2. **Download Required NLTK Resources**:
   ```python
   import nltk
   nltk.download('punkt')
   ```

## Project Structure
- `parser.py`: Main script implementing the CFG parser and noun phrase extraction.
- `sentences/[sentence_file].txt`: Text files containing sample sentences for parser testing.

## Usage
1. **Run the Parser**:
   ```bash
   python parser.py sentences/1.txt
   ```
   - If a filename is specified, the script reads the sentence from that file.
   - If no filename is provided, the script will prompt for an input sentence.

2. **Example Code**:
   ```python
   from parser import preprocess, np_chunk

   sentence = "The quick brown fox jumps over the lazy dog."
   tokens = preprocess(sentence)
   trees = list(parser.parse(tokens))
   for tree in trees:
       tree.pretty_print()
       for np in np_chunk(tree):
           print(" ".join(np.flatten()))
   ```

## Code Details
- **Grammar Definitions**: CFG rules are specified in `TERMINALS` and `NONTERMINALS` to represent sentence structure and parts of speech.
- **Preprocessing**: The `preprocess` function tokenizes the input sentence, converts it to lowercase, and filters out non-alphabetic words.
- **Noun Phrase Chunking**: The `np_chunk` function extracts noun phrases from the parse tree, avoiding nested noun phrases.

## Example Outputs
The parser provides visual representations of sentence structure and extracted noun phrases for various sample sentences.

For more information, visit the [Parser Project](https://cs50.harvard.edu/ai/2020/projects/6/parser/).

