"""
detect dictionary
Write a function, detectDictionary, that takes in a dictionary of words and an alphabet string. The function should return a boolean indicating whether or not all words of the dictionary are lexically-ordered according to the alphabet.

You can assume that all characters are lowercase a-z.

You can assume that the alphabet contains all 26 letters.

test_00:
dictionary = ["zoo", "tick", "tack", "door"]
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
detect_dictionary(dictionary, alphabet) # -> True
test_01:
dictionary = ["zoo", "tack", "tick", "door"]
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
detect_dictionary(dictionary, alphabet) # -> False
test_02:
dictionary = ["zoos", "zoo", "tick", "tack", "door"]
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
detect_dictionary(dictionary, alphabet) # -> False
test_03:
dictionary = ["miles", "milestone", "proper", "process", "goal"]
alphabet = "mnoijpqrshkltabcdefguvwzxy"
detect_dictionary(dictionary, alphabet) # -> True
test_04:
dictionary = ["miles", "milestone", "pint", "proper", "process", "goal"];
alphabet = "mnoijpqrshkltabcdefguvwzxy"
detect_dictionary(dictionary, alphabet) # -> True
test_05:
dictionary = ["miles", "milestone", "pint", "proper", "process","goal", "apple"];
alphabet = "mnoijpqrshkltabcdefguvwzxy"
detect_dictionary(dictionary, alphabet) # -> False
"""
