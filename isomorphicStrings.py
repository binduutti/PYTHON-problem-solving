''' given a string s and a string t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters in s can be replaced to get t.
  All occurrences of a character must be replaced with another character while preserving the order of characters.
  No two characters may map to the same character, but a character may map to itself.
'''
def are_isomorphic(s, t):
    if len(s) != len(t):
        return False

    mapping = {}
    for i in range(len(s)):
        if s[i] in mapping:
            if mapping[s[i]] != t[i]:
                return False
        else:
            mapping[s[i]] = t[i]

    return True