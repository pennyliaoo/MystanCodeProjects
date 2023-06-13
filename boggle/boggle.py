"""
File: boggle.py
Name: Penny
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
ROW = 4
COL = 4
def main():
	"""
	TODO:
	"""
	start = time.time()
	board = []
	word_lst = read_dictionary()
	lock = True
	# create board
	for i in range(ROW):
		letter = input('%s row of letters: '%(i+1)).split()
		for j in range(len(letter)):
			if len(letter[j]) > 1:
				print('Illegal input')
				lock = False
				break
		if not lock:
			break
		if len(letter) < 4:
			print('Illegal input')
			break
		board.append(letter)
	find_word(board)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')

def find_word(board):
	# input list
	word_lst = read_dictionary()
	wordfinding = []
	# current_lst = []
	# current_pos_lst = []
	for row in range(ROW):
		for column in range(COL):
			find_word_helper(board,[board[row][column]],wordfinding,word_lst,"",row, column,[(row,column)])
	# current_lst.pop()
	# current_pos_lst.pop()
	print('There are',len(wordfinding),'words in total')

def find_word_helper(board, current_lst, wordfinding, word_lst, current_str, row ,column, current_pos_lst=[]):
	if len(current_lst) >= 4:
		new_str = ''.join(current_lst)
		if new_str in word_lst:
			if new_str not in wordfinding:
				print('Found: ', new_str)
				wordfinding.append(new_str)
	for i in range(-1,2):
		for j in range(-1,2):
			if 0 <= row + i < 4:
				if 0 <= column+j < 4:
						current_pos = row+i, column+j
						if current_pos in current_pos_lst:
							pass
						else:
							current_lst.append(board[row+i][column+j])
							current_pos_lst.append(current_pos)
							current_str = ''.join(current_lst)
							# print(current_pos_lst)
							# print(current_lst)
							if has_prefix(current_str,word_lst):
								find_word_helper(board, current_lst, wordfinding, word_lst, current_str,row+i,column+j,current_pos_lst)
							current_lst.pop()
							current_pos_lst.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dct_lst = []
	with open(FILE,'r') as f:
		for line in f:
			add_word = line.strip('\n')
			dct_lst.append(add_word)
	return dct_lst

def has_prefix(sub_s, dct_lst):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dct_lst:
		if word.startswith(sub_s):
			return True
	return False

if __name__ == '__main__':
	main()
