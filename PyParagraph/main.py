"""Approximate Word Count
Approximate Sentence Count
Average Letter Count
Average Sentence Length"""


import os
import re
import numpy

filepath = "input.txt"


paragraph = open(filepath).read()
word_count_loop = paragraph.split(" ")
word_count = len(paragraph.split(" "))
avg_sentence_count = len(re.split("(?<=[.!?]) +", paragraph))
letter_count = numpy.mean([len(x) for x in word_count_loop])
sentence_length = word_count/avg_sentence_count

print("Approximate word count:" + str(word_count))
print("Approximate sentence count:" + str(avg_sentence_count))
print("Approximate letter count:" + str(letter_count))
print("Approximate sentence length:" + str(sentence_length))







