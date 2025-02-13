s = {1: "first", 2: "second", 3: "third", 4: "fourth"}

def invert(dictionary: dict):
    new_s = {}
    for k, v in dictionary.items():
        new_s[v] = k
    return new_s
print(invert(s))