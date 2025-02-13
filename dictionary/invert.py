s = {1: "first", 2: "second", 3: "third", 4: "fourth"}

def invert(dictionary: dict):
    new_s = {}
    for k, v in dictionary.items():
        new_s[v] = k
    dictionary.clear()
    dictionary.update(new_s)
    return dictionary
print(invert(s))