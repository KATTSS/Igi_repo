"""LR3/igi
String handler module
Version: 1.0
Author: Ekaterina Butkevich
Group: 453501
Date: 11.03.2026
"""

def find_lowercase_count(s):
    """Returns amount of lowercase symbols in string."""
    count=0
    for symbol in s:
        if symbol.islower():
            count += 1
    return count

def find_digit_count(s):
    """Returns amount of digits in string."""
    count = 0
    for symbol in s:
        if symbol.isdigit():
            count += 1
    return count

def count_consonant_starters(s):
    """Returns amount of consonant-starter words in a string."""

    words=s.upper().split(' ')
    vowels=['A','E', 'I', 'O', 'U']
    count=0

    for word in words:
        if word[0] not in vowels:
            count +=1
    return count

def find_double_letter(s):
    """Returns a set of words with double letters from the string."""
    s = s.replace(',', '').replace('.', '')

    words=s.split(' ')
    result=set()

    for word in words:
        for i in range(len(word)-1):
            if word[i].lower==word[i+1].lower:
                result.add(word)
                continue
    return result

def alphabet_sort(s):
    """Returns sorted by alphabet string"""
    s = s.replace(',', '').replace('.', '')

    words=s.split(' ')

    sorted_words=sorted(words, key=str.lower)

    return ' '.join(sorted_words)