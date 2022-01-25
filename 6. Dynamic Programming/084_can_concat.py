"""
can concat
Write a function, can_concat, that takes in a string and a list of words as arguments. The function should return boolean indicating whether or not it is possible to concatenate words of the list together to form the string.

You may reuse words of the list as many times as needed.

test_00:
can_concat("oneisnone", ["one", "none", "is"]) #  -> True
test_01:
can_concat("oneisnone", ["on", "e", "is"]) #  -> False
test_02:
can_concat("oneisnone", ["on", "e", "is", "n"]) #  -> True
test_03:
can_concat("foodisgood", ["is", "g", "ood", "f"]) #  -> True
test_04:
can_concat("santahat", ["santah", "hat"]) #  -> False
test_05:
can_concat("santahat", ["santah", "san", "hat", "tahat"]) #  -> True
test_06:
can_concat("rrrrrrrrrrrrrrrrrrrrrrrrrrx", ["r", "rr", "rrr", "rrrr", "rrrrr", "rrrrrr"]) #  -> False
"""
