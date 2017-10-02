# this solution will timeout for high values of magazine and ransom
def ransom_note(magazine, ransom):
    if len(magazine) < len(ransom):
        return False
    word_list = []
    for word in ransom:
        if word in magazine:
            word_list.append(word)
            magazine.remove(word)
    for word in word_list:
        if word in ransom:
            ransom.remove(word)
    if ransom:
        return False
    else:
        return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    


# Other solution
from collections import Counter
def ransom_note(magazine, ransom):
    return (Counter(ransom) - Counter(magazine) == {})

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")

# Other solution without using Counter
#if any negatives in hash than it's not do-able
# if key isn't in magazine has than it's not do-able
# insert into hash magazine with frequency
# subtract from hash if it exists in ransom
# if it's not in magazine has than it's not doable
def ransom_note(magazine, ransom):
    freq_hash = {}
    for word in magazine:
        if word in freq_hash:
            freq_hash[word] = freq_hash.get(word) + 1
        else:
            freq_hash[word] = 1
    for word in ransom:
        if word not in freq_hash:
            return False
        else:
            freq_hash[word] = freq_hash.get(word) - 1
    for freq in freq_hash:
        if freq_hash.get(freq) < 0:
            return False
    return True