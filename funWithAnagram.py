# two string are anagrams if they are permutations of each other.
# remove each string that is an anagram of an earlier string then
# return the result in sorted order

text = ['code', 'doce', 'ecod', 'framer', 'frame']

def funWithAnagrams(text: list):
    result = []
    mem = [sorted(w) for w in result]
    for word in text:
        if sorted(word) not in mem:
            result.append(word)
            mem = [sorted(w) for w in result]
    return sorted(result)


def funWithAnagram2(text: list):
    keys = set(["".join(sorted(w)) for w in text])

    result = []
    for k in list(keys):
        for w in text:
            if k == "".join(sorted(w)):
                result.append(w)
                break
    return sorted(result)

print(funWithAnagram2(text))