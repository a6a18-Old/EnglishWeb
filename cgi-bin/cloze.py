import requests
from bs4 import BeautifulSoup
import random
import cgitb
cgitb.enable()


def past(word):

    url = 'https://tw.dictionary.search.yahoo.com/search;_ylt=AwrtXG4A1MBddHcAXxx7rolQ;_ylc=X1MDMTM1MTIwMDM3OQRfcgMyBGZyAwRncHJpZANic25FZFpQSlFJS3JJMWRnSFNvMFhBBG5fcnNsdAMwBG5fc3VnZwM0BG9yaWdpbgN0dy5kaWN0aW9uYXJ5LnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIEcXVlcnkDZG8EdF9zdG1wAzE1NzI5MTgyNzg-?p='+str(word)+'&fr=sfp&iscqry=&guccounter=1'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }

    html = requests.get(url, headers=header)
    soup = BeautifulSoup(html.text, 'html.parser')
    word_past_list = soup.select('h4 span.fz-14 b')
    print(type(word_past_list))
    word_past_list = [past_word.text for past_word in word_past_list]  # 很棒的list技巧 可將裡面的各個元素處理完再存回去，此技巧叫做List Comprehension。
    print(word_past_list)


def cloze(word):
    word = word.lower()   # 避免輸入的單字有大小寫不同而無法過濾，一律都先轉小寫
    url = 'https://tw.dictionary.search.yahoo.com/search;_ylt=AwrtXG4A1MBddHcAXxx7rolQ;_ylc=X1MDMTM1MTIwMDM3OQRfcgMyBGZyAwRncHJpZANic25FZFpQSlFJS3JJMWRnSFNvMFhBBG5fcnNsdAMwBG5fc3VnZwM0BG9yaWdpbgN0dy5kaWN0aW9uYXJ5LnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIEcXVlcnkDZG8EdF9zdG1wAzE1NzI5MTgyNzg-?p='+str(word)+'&fr=sfp&iscqry=&guccounter=1'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }

    html = requests.get(url, headers=header)
    soup = BeautifulSoup(html.text, 'html.parser')
    word_sentence_list = soup.select('p span.fz-14.fw-500')  # 抓單字的例句。此為一個list所以後來得取索引。
    word_past_list = soup.select('li.ov-a.fstlst.mt-0 h4 span.fz-14 b')  # 如果此單字有特殊變化，do did done而不是一般的ed 那麼他就會抓到，反之抓不到。這樣可以有 ___ed的效果。


    try:   # 為了避免輸入者輸入不存在的單字而導致的錯誤，事實上在上面就會出錯，但是刻意將error擺在取句子比較精準！ 除非此單字本來就沒有例句，這時就尷尬了。
        sentence = random.sample(word_sentence_list, 1)  # 後面的1表示取一個句子，可取多個唷，依照個人需求。 #取出為清單 需要再調整。
    except ValueError:
        return print("無此單字的例句")


    # sentence.text   # It takes a lot of work to dig a deep well. 挖一口深井很費事。
    question = sentence[0].text


    word_past_list = [past_word.text for past_word in word_past_list]
    word_past_list.append(word)  # 添加原先的單字
    word_past_list.append(word.capitalize())  # 添加大寫過濾 (字首 or 專有名詞)
    #print(word_past_list)


    for keyword in word_past_list:
        if keyword in question:
            question = question.replace(keyword, '____')
    #print(question)
    return question




if __name__ == '__main__':

    #past("do")
    print(cloze('do'))