def first_non_repeating_letter(s):
    for i in range(len(s)):
        if s.lower().count(s.lower()[i])==1:
            return s[i]
    return ""

""" best
def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
            
    return ""
 """
