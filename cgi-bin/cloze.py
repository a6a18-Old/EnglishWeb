import requests
from bs4 import BeautifulSoup
import random
import cgitb
cgitb.enable()

def cloze(word):

    url = 'https://tw.dictionary.search.yahoo.com/search;_ylt=AwrtXG4A1MBddHcAXxx7rolQ;_ylc=X1MDMTM1MTIwMDM3OQRfcgMyBGZyAwRncHJpZANic25FZFpQSlFJS3JJMWRnSFNvMFhBBG5fcnNsdAMwBG5fc3VnZwM0BG9yaWdpbgN0dy5kaWN0aW9uYXJ5LnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIEcXVlcnkDZG8EdF9zdG1wAzE1NzI5MTgyNzg-?p='+str(word)+'&fr=sfp&iscqry=&guccounter=1'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }

    html = requests.get(url, headers=header)
    soup = BeautifulSoup(html.text, 'html.parser')
    word_sentence_list = soup.select('p span.fz-14.fw-500')

    try:
        sentence = random.sample(word_sentence_list, 1)  # 後面的1表示取一個句子，可取多個唷，依照個人需求。 #取出為清單 需要再調整。
    except ValueError:
        return print("無此單字例句")

    # sentence.text   # It takes a lot of work to dig a deep well. 挖一口深井很費事。
    question = sentence[0].text.replace(str(word), '____')   # __ed。
    #print(question)
    return question


if __name__ == '__main__':

    cloze('afdsfds')