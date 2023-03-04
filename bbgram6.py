import itertools
import math
import random
from tqdm import tqdm
from tqdm.contrib.concurrent import process_map  # or thread_map
from english_words import get_english_words_set
from multiprocessing import Pool

def is_bbgram(word_tuple):
	if word_tuple[0][3:6] == word_tuple[1][0:3]:
		if word_tuple[0][6:9] == word_tuple[2][0:3]:
			if word_tuple[1][6:9] == word_tuple[2][3:6]:
				print(word_tuple)
				return

# with open('words_alpha.txt') as f:
# 	words = f.read().splitlines()

words = get_english_words_set(['gcide'], alpha=True)

nine_lettered_words = [word.upper() for word in words if len(word) == 9]
nine_lettered_words.sort()
perm_count = math.perm(len(nine_lettered_words), 2)

file_name = 'bbgrams6.txt'
open(file_name, 'w').close()
with open(file_name, "a") as results:
	for word_pair in tqdm(itertools.permutations(nine_lettered_words, 2), total=perm_count, miniters=1_000_000):
		if (word_pair[0][3:6] == word_pair[1][0:3]):
			for last_word in nine_lettered_words:
				if word_pair[0][6:9] == last_word[0:3]:
					if word_pair[1][6:9] == last_word[3:6]:
						if last_word != word_pair[0]:
							if last_word != word_pair[1]:
								results.write(f'{word_pair[0]},{word_pair[1]},{last_word}\n')
