words = ['ant', 'elephant', 'dog', 'giraffe']
long_words = list(filter(lambda w: len(w) >= 5, words))
print(long_words)