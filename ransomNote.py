'''
given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
'''
def ransom_note(ransomNote, magazine):
    ransom_dict = {}
    for char in ransomNote:
        if char in ransom_dict:
            ransom_dict[char] += 1
        else:
            ransom_dict[char] = 1
            
    magazine_dict = {}
    for char in magazine:
        if char in magazine_dict:
            magazine_dict[char] += 1
        else:
            magazine_dict[char] = 1
            
    for char, count in ransom_dict.items():
        if char not in magazine_dict or magazine_dict[char] < count:
            return False
            
    return True
# Example usage:
ransomNote = "aa"
magazine = "ab"
result = ransom_note(ransomNote, magazine)
print(result)
