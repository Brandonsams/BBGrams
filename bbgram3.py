import itertools
import math
from tqdm import tqdm
from tqdm.contrib.concurrent import process_map  # or thread_map
from english_words import get_english_words_set
import asyncio

def background(f):
	def wrapped(*args, **kwargs):
		return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)
	return wrapped

# @background
def is_bbgram(word_tuple):
	if word_tuple[0][3:6] == word_tuple[1][0:3]:
		if word_tuple[0][6:9] == word_tuple[2][0:3]:
			if word_tuple[1][6:9] == word_tuple[2][3:6]:
				return True
	return False


with open('words_alpha.txt') as f:
	words = f.read().splitlines()

nine_lettered_words = [word.upper() for word in words if len(word) == 9]
nine_lettered_words.sort()
perm_count = math.perm(len(nine_lettered_words), 3)

print(len(nine_lettered_words))
print(perm_count)

# r = process_map(is_bbgram, itertools.permutations(nine_lettered_words[0:10], 3), max_workers=2)

for word_tuple in tqdm(itertools.permutations(nine_lettered_words[0:1000], 3), total=perm_count):
	if is_bbgram(word_tuple):
		print(word_tuple)


# count = 0
# chunk = 1_000_000
# for word_perm in tqdm(itertools.permutations(nine_lettered_words, 3), total=perm_count, miniters=chunk):
# 	# if count > chunk:
# 	# 	count = 0
# 	# 	print(word_perm)
# 	if is_bbgram(word_perm[0], word_perm[1], word_perm[2]):
# 		print(word_perm)
# 	# count = count + 1
#
# # print(len(three_element_word_permutations))