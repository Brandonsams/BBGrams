import itertools
from tqdm import tqdm
from english_words import get_english_words_set

def is_bbgram(first_word, second_word, third_word):
	pass

words = get_english_words_set(['gcide'], alpha=True)
nine_lettered_words = [word.upper() for word in words if len(word) == 9]

for word_perm in tqdm(itertools.permutations(nine_lettered_words, 3)):
	pass

# print(len(three_element_word_permutations))