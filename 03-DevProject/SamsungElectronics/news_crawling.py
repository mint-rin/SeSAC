import requests
import csv
from bs4 import BeautifulSoup

# https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=001&date=20230801&page=1
page = 116
date = '20230801'
oid = '003'

while True:

    print('page', page)

    params = {
        'mode':'LPOD',
        'mid':'sec',
        'oid':'001',
        'date':date,
        'page':str(page)
    }

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    
    res = requests.get('https://news.naver.com/main/list.naver', params=params, headers=headers)
    bs = BeautifulSoup(res.text, 'html.parser')

    now_page = int(bs.select_one('div.paging strong').text.strip())
    
    if page != now_page:
        break
    
    lists = bs.select('ul.type06_headline > li')
    
    for idx, list in enumerate(lists):
        url = list.select_one('a').attrs['href']
        res_content = requests.get(url, headers=headers)
        bs_content = BeautifulSoup(res_content.text, 'html.parser')
        
        title = ''
        content = ''
        reaction = ''
        reaction_cnt = ''
        category = ''
        
        if bs_content.select_one('h2#title_area') != None:
            title = bs_content.select_one('h2#title_area').text.strip()
            # content = bs_content.select_one('article#dic_area').text.replace('\n','').strip()
            reaction = bs_content.select('span.u_likeit_list_name._label')[0].text.strip()
            reaction_cnt = bs_content.select('span.u_likeit_list_count._count')[0].text.strip()
            category = bs_content.select_one('em.media_end_categorize_item').text.strip()
        print(title)
        #print(content)
        print(reaction)
        print(reaction_cnt)
        print(category)
        
