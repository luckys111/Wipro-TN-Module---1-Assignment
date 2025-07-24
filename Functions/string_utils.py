# string_utils.py
# string_utils.py

def ispalindrome(name):
    return name == name[::-1]

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in name if ch in vowels)

def frequency_of_letters(name):
    freq = {}
    for ch in name:
        if ch != ' ':
            freq[ch] = freq.get(ch, 0) + 1
    return freq
