def number_needed(a, b):
    freq_number = 0
    freq_hash = {}
    for c in a:
        if c in freq_hash:
            freq_hash[c] = freq_hash[c] + 1
        else:
            freq_hash[c] = 1
    for c in b:
        if c in freq_hash:
            freq_hash[c] = freq_hash[c] - 1
        else:
            freq_hash[c] = -1
    for (key,value) in freq_hash.items():
        freq_number += abs(value)
    return freq_number
        
a = input().strip()
b = input().strip()

print(number_needed(a, b))