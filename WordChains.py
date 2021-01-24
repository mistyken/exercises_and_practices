# Word Chains
# ===========

# Implement a function `chain(word1, word2)`, that returns a short-as-possible list that "links" the two given words, where:

# - Your list starts with `word1` and ends with `word2`
# - Each word in your list differs by only one letter from the entry before it
# - Each word in your list is in /usr/share/dict/words

# All words involved are expected to be all lowercase. Ignore any words from the dictionary that contain uppercase letters or punctuation.
# If no chain can be found between the input words, return an empty value that is idiomatic for the language that you're using. You should expect each call to this function always to return within a few seconds.

# Examples:

# - chain("duck", "bill") might return: ["duck", "buck", "bulk", "bilk", "bill"]
# - chain("spinning", "top") returns an empty value
# - chain("sport", "spine") might return: ["sport", "spore", "spire", "spine"]
# - chain("tallow", "wallow") should return: ["tallow", "wallow"]
# - chain("orange", "pillow") returns an empty value

# wordfile: https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words

mem = {}


def chain(word1, word2):
    # if the two word length doesn't match, then we can't form a chain
    if len(word1) != len(word2):
        return []

    result = []
    dictionary = set()
    file_object  = open("dictionary.txt", "r")
    if file_object.mode == 'r':
        contents = file_object
        for content in contents:
            word = content.replace("\n", "")
            # only add those words that are of same length as the target to the dictionary
            if checkCharacter(word) and len(word) == len(word2) and word not in dictionary:
                dictionary.add(word)
    
    # if either word1 or word2 is not in the dictionary, we don't have a chain
    if word1 not in dictionary or word2 not in dictionary:
        return []

    queue = [word1]
    result = []
    while queue:
        cur_word = queue.pop(0)
        # find all possibilities within one hamming distance of our current word
        possibilities = set(list(filter(lambda x: getHammingDistance(cur_word, x) < 2, dictionary)))
        mem[cur_word] = possibilities - {cur_word}

        # if target is found, start processing the result list from mem
        if word2 in possibilities:
            result.append(word2)
            result.append(cur_word)
            while cur_word != word1:
                for word, possibilities in mem.items():
                    if cur_word in possibilities:
                        result.append(word)
                        cur_word = word
            break
        
        # put the word we had encountered onto the queue and remove from dictionary to prevent visiting
        # same word again
        for possibility in possibilities:
            if possibility != cur_word:
                queue.append(possibility)
            dictionary.remove(possibility)

    result.reverse()
    return result
    

def checkCharacter(word):
    for c in word:
        if ord(c) < 97 or ord(c) > 122:
            return False
    return True


def getHammingDistance(word1, word2):
    distance = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1
    return distance


print(chain("man", "ape"))
print(chain("duck", "bill"))
print(chain("spinning", "top"))
print(chain("orange", "pillow"))