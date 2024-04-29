from nltk.tokenize import word_tokenize
from nltk import pos_tag
text = '''The/DT planet/NN Jupiter/NNP and/CC its/PPS moons/NNS are/VBP in/IN effect/NN a/DT minisolar/JJ system/??
,/, and/CC Jupiter/NNP itself/PRP is/VBZ often/RB called/VBN a/DT star/?? that/IN never/RB caught/??? fire/NN ./.'''
pairs = [pair.split('/') for pair in text.split()]
print(pairs)
words = []
tags=[]
