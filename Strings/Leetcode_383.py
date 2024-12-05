'''
    Ransome Note
'''

from collections import Counter

def canConstruct(ransomNote, magazine):
    sett = Counter(magazine)
    for i in ransomNote:
        if sett[i] == 0:
            return False
        sett[i] -= 1
    return True