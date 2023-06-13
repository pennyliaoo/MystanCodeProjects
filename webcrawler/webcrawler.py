"""
File: webcrawler.py
Name: Penny
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text # It is a single hugh string
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tags = soup.find_all('table', {'class': 't-stripe'})
        male_sum = 0
        female_sum = 0
        for tag in tags:
            rank = tag.tbody.text
            rank_lst = rank.split()
            for i in range(len(rank_lst)):
                if rank_lst[i] == 'sample':
                    break
                if i % 5 == 2:
                    male_number = int(rank_lst[i].replace(',', ''))
                    male_sum += male_number
            for j in range(len(rank_lst)):
                if rank_lst[j] == 'on':
                    break
                if j % 5 == 4:
                    female_number = int(rank_lst[j].replace(',', ''))
                    female_sum += female_number
        print('Male number:', male_sum)
        print('Female number:', female_sum)




if __name__ == '__main__':
    main()
