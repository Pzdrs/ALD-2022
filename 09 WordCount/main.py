import itertools
import sys
from collections import defaultdict


def unique(arr):
    dictionary = defaultdict(int)
    for el in arr:
        dictionary[el] = dictionary[el] + 1
    return dictionary


def extract_phrases(arr):
    phrase_list = []
    for index, el in enumerate(arr):
        phrase_list.append((el, words[index + 1] if len(arr) > index + 1 else None))
    return phrase_list


words = []
for line in sys.stdin:
    line = line.lower().strip()
    if not line:
        continue
    words.extend(line.split(' '))

phrases = extract_phrases(words)

print('Word Frequency:')
for word, occurrences in itertools.islice(sorted(unique(words).items(), key=lambda x: x[1], reverse=True), 15):
    print(f' - {word:12} {occurrences / len(words):.2%} ({occurrences})')

print('Phrase Frequency:')
for phrase, occurrences in itertools.islice(sorted(unique(phrases).items(), key=lambda x: x[1], reverse=True), 15):
    print(f' - {" ".join(phrase):20} {occurrences / len(phrases):.2%} ({occurrences})')
