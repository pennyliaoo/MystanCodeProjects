"""
File: anagram.py
Name:Penny
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    word_lst = read_dictionary()
    print('Welcome to stanCode ''Anagram Generator'' (or -1 to quit)')
    while True:
        start = time.time()
        n = input('Find anagrams for: ')
        if n == EXIT:
            break
        else:
            find_anagrams(n)
            # print(len(anagram_lst), 'anagrams: ', anagram_lst)
            end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    dct_lst = []
    with open(FILE,'r') as f:
        for line in f:
            add_word = line.strip('\n')
            dct_lst.append(add_word)
    return dct_lst


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    word_lst = read_dictionary()
    anagram_lst = []
    find_anagrams_helper(s,[],len(s),word_lst,anagram_lst,[])
    print(len(anagram_lst), 'anagrams: ', anagram_lst)

def find_anagrams_helper(str, current_lst, ans_len, word_lst,anagram_lst, index_lst):
    if len(current_lst) == ans_len:
        new_str = ''.join(current_lst)
        if new_str in word_lst:
            if new_str not in anagram_lst:
                print('searching...')
                print('Found: ',new_str)
                anagram_lst.append(new_str)
    else:
        for index in range(len(str)):
            if index in index_lst:
                pass
            else:
                current_lst.append(str[index])
                index_lst.append(index)
                current_str = ''.join(current_lst)
                print(current_lst)
                if has_prefix(current_str, word_lst):
                    find_anagrams_helper(str, current_lst,ans_len,word_lst,anagram_lst,index_lst)
                print(current_lst)
                current_lst.pop()
                index_lst.pop()

def has_prefix(sub_s,dct_lst):
    """
    :param sub_s:
    :return:
    """
    for word in dct_lst:
        if word.startswith(sub_s):
            return True
    return False



if __name__ == '__main__':
    main()
