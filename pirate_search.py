from bs4 import BeautifulSoup
import requests
import json

dic = {}
lis = []
def psearch(msg):
    search_key = str(msg)
    search_result = requests.get(f'https://thepiratebay.org/search/{search_key}/0/99/0').text

    soup = BeautifulSoup(search_result,'lxml')

    all_td = soup.findAll('td')
    count = max(len(all_td),1)
    for j in range(count):
        single_td = all_td[j]
        try:
            for i in range(len(single_td)):
                single_td_div = single_td.findAll('div',{'class':'detName'})[i]
                name = str(single_td_div.text)[:-1]

                single_td_a = single_td.findAll('a',{'title':'Download this torrent using magnet'})[i]
                link = single_td_a.get('href')

                dic[name] = link

        except Exception:
            pass
    ret = json.dumps(dic)
    return str(ret)