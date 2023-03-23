# ====== Notes on the below results ======
# It's very interesting that the library is able to find similarities across groups such as animals, fruits,
# and what animals eat what fruits. There are greater similarities within groups than across groups
# (see apple-banana vs. banana-monkey), which is probably to be expected. It's also interesting that monkey-apple (23)
# and cat-apple (20) are practically the same.
#
# I introduced three new words: judo, boxing, and climbing. All three are sports. Judo and boxing are martial arts.
# Climbing is something both monkeys and cats do, but monkeys do more of. And indeed monkey and climbing are more
# similar than cat and climbing. Surprisingly boxing and judo are a 0.9999999 match! I wonder why.

import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("judo")
word5 = nlp("boxing")
word6 = nlp("climbing")

print(word1, word2)
print(word1.similarity(word2))
print(word3, word2)
print(word3.similarity(word2))
print(word3, "-", word1)
print(word3.similarity(word1))

print(word4, word5)
print(word4.similarity(word5))
print(word4, word6)
print(word4.similarity(word6))
print(word6, word2)
print(word6.similarity(word2))
print(word6, word1)
print(word6.similarity(word1))

tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))




sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ", similarity)


