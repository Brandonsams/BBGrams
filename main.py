import itertools
import math
from tqdm import tqdm
from english_words import get_english_words_set

# # Long list of words
# with open('words_alpha.txt') as f:
# 	words = f.read().splitlines()

# Short list of words
words = list(get_english_words_set(['gcide'], alpha=True))

# Add in extra words, if desired
with open('words_extra.txt') as f:
	extra_words = f.read().splitlines()
words = list(set(words + extra_words))

# Cleanup word list
nine_lettered_words = [word.upper() for word in words if len(word) == 9]
nine_lettered_words.sort()
perm_count = math.perm(len(nine_lettered_words), 2)

# Now we search
file_name = 'bbgrams.txt'
open(file_name, 'w').close() # delete old file contents
with open(file_name, "a") as results:
	for word_pair in tqdm(itertools.permutations(nine_lettered_words, 2), total=perm_count):
		if (word_pair[0][3:6] == word_pair[1][0:3]):
			for last_word in nine_lettered_words:
				if last_word != word_pair[0]: # can't match the first word
					if last_word != word_pair[1]: # can't match the second word
						if word_pair[0][6:9] == last_word[0:3]:
							if word_pair[1][6:9] == last_word[3:6]:
								# yay!
								results.write(f'{word_pair[0]},{word_pair[1]},{last_word}\n')
