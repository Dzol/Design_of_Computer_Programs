# -----------------
# User Instructions
#
# This homework deals with anagrams. An anagram is a rearrangement
# of the letters in a word to form one or more new words.
#
# Your job is to write a function anagrams(), which takes as input
# a phrase and an optional argument, shortest, which is an integer
# that specifies the shortest acceptable word. Your function should
# return a set of all the possible combinations of anagrams.
#
# Your function should not return every permutation of a multi word
# anagram: only the permutation where the words are in alphabetical
# order. For example, for the input string 'ANAGRAMS' the set that
# your function returns should include 'AN ARM SAG', but should NOT
# include 'ARM SAG AN', or 'SAG AN ARM', etc...


def anagrams(phrase, shortest=2):
    """Return a set of phrases with words from WORDS that form anagram
    of phrase. Spaces can be anywhere in phrase or anagram. All words
    have length >= shortest. Phrases in answer must have words in
    lexicographic order (not all permutations)."""
    return find_anagrams(phrase.replace(' ', ''), '', shortest)


def find_anagrams(letters, previous_word, shortest):
    """Using letters, form anagrams using words >= previous_word and longer than shortest."""
    results = set()
    for w in find_words(letters):
        if len(w) >= shortest and w > previous_word:
            remainder = removed(letters, w)
            if remainder:
                for rest in find_anagrams(remainder, w, shortest):
                    results.add(w + ' ' + rest)
            else:
                results.add(w)
    return results


# ------------
# Helpful functions
#
# You may find the following functions useful. These functions
# are identical to those we defined in lecture.

def removed(letters, remove):
    """Return a str of letters, but with each letter in remove removed once."""
    for L in remove:
        letters = letters.replace(L, '', 1)
    return letters


def find_words(letters):
    return extend_prefix('', letters, set())


def extend_prefix(pre, letters, results):
    if pre in WORDS:
        results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            extend_prefix(pre + L, letters.replace(L, '', 1), results)
    return results


def prefixes(word):
    """A list of the initial sequences of a word, not including the complete word."""
    return [word[:i] for i in range(len(word))]


def readwordlist(filename):
    """Read the words from a file and return a set of the words
    and a set of the prefixes."""
    word_set = set()
    prefix_set = set()
    with open(filename, 'r') as fin:
        for line in fin:
            word = line.strip().upper()
            if word:
                word_set.add(word)
                prefix_set.update(prefixes(word))
    return word_set, prefix_set


WORDS, PREFIXES = readwordlist('../words4k.txt')


# ------------
# Testing
#
# Run the function test() to see if your function behaves as expected.

def test():
    assert 'DOCTOR WHO' in anagrams('TORCHWOOD')
    assert 'BOOK SEC TRY' in anagrams('OCTOBER SKY')
    assert 'SEE THEY' in anagrams('THE EYES')
    assert 'LIVES' in anagrams('ELVIS')
    assert anagrams('PYTHONIC') == {'NTH PIC YO', 'NTH OY PIC', 'ON PIC THY', 'NO PIC THY',
                                    'COY IN PHT', 'ICY NO PHT', 'ICY ON PHT', 'ICY NTH OP',
                                    'COP IN THY', 'HYP ON TIC', 'CON PI THY', 'HYP NO TIC',
                                    'COY NTH PI', 'CON HYP IT', 'COT HYP IN', 'CON HYP TI'}
    return 'tests pass'

print(test())