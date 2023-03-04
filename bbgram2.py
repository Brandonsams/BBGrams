import itertools
import math
from tqdm import tqdm
from english_words import get_english_words_set

def is_bbgram(first_word, second_word, third_word):
	square_word_1 = first_word[0:3] + second_word[0:3] + third_word[0:3]
	if square_word_1 != first_word:
		return False
	print(f'square_word_1 = {square_word_1}')

	square_word_2 = first_word[3:6] + second_word[3:6] + third_word[3:6]
	if square_word_2 != second_word:
		return False
	print(f'square_word_2 = {square_word_2}')

	square_word_3 = first_word[6:9] + second_word[6:9] + third_word[6:9]
	if square_word_3 != third_word:
		return False
		print(f'square_word_3 = {square_word_3}')
	return True

def is_bbgram_2(first_word, second_word, third_word):
	if first_word[3:6] == second_word[0:3]:
		if first_word[6:9] == third_word[0:3]:
			if second_word[6:9] == third_word[3:6]:
				return True
	return False

with open('words_alpha.txt') as f:
	words = f.read().splitlines()

nine_lettered_words = [word.upper() for word in words if len(word) == 9]
nine_lettered_words.sort()
perm_count = math.perm(len(nine_lettered_words), 3)

print(len(nine_lettered_words))
print(perm_count)

count = 0
chunk = 10_000_000
for word_perm in tqdm(itertools.permutations(nine_lettered_words, 3), total=perm_count, miniters=chunk):
	# if count > chunk:
	# 	count = 0
	# 	print(word_perm)
	if is_bbgram_2(word_perm[0], word_perm[1], word_perm[2]):
		print(word_perm)
	# count = count + 1

# print(len(three_element_word_permutations))