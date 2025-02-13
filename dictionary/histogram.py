def histogram(s: str):
    dictionary = {}
    for char in s:
        if char not in dictionary:
            dictionary[char] = ""
        dictionary[char] += "*"
    return dictionary

groups = histogram("statistically")

for k, v in groups.items():
    print(f"{k} {v}")