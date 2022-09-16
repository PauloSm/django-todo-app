"""
Given a pattern and a string strg, find if strg follows the same pattern
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in strg.

Example 1:
Input: pattern = "abba", strg = "dog cat cat dog"
Output: True  
Example 2:
Input:pattern = "abba", strg = "dog cat cat fish"
Output: False 

Example 3:
Input: pattern = "aaaa", strg = "dog cat cat dog"
Output: False

Example 4:
Input: pattern = " ", strg = "dog dog dog dog"
Output: False


Call this functions from the interview.py to be included in the web application.
"""


def test_function(pattern: str, strg: str) -> bool:
    words = strg.split(" ")
    if len(words) != len(pattern) or len(strg) == 0:
        return False
    dict_word, dict_pattern = dict(), dict()
    for letter_word, letter_pattern in zip(words, pattern):
        if letter_word not in dict_word and letter_pattern not in dict_pattern:
            dict_word[letter_word] = letter_pattern
            dict_pattern[letter_pattern] = letter_word
        elif dict_word.get(letter_word) == letter_pattern and dict_pattern.get(letter_pattern) == letter_word:
            pass
        else:
            return False
    return True
