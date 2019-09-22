import requests
import traceback
import re
from bs4 import BeautifulSoup
import csv

fieldsname = ['STT', 'URL', 'Ho Ten', 'Dia Chi', 'Tinh', 'Mo Ta Ngan Gon', 'Mo Ta Chi Tiet', 'Ma So', 'Ngay Dang Ki', 'Danh muc']
numberOfPage = 9999
nameFile = 'database.csv'
key = 0

def writingToFile(ideas):
    try:
        filename = nameFile
        with open(filename, 'a') as f:
            w = csv.DictWriter(f, fieldsname)
            for idea in ideas:
                w.writerow(idea)
    except Exception:
        print('Error occurred while writing file!')
        print(traceback.format_exc())

def getDetails(DetailsURL):
    try:
        r = requests.get(DetailsURL)
        _soup = BeautifulSoup(r.content, 'html5lib')
        table = _soup.find('div', attrs={'class': 'col-md-9 table-responsive right_form'}).tbody
        return table.contents[9].contents[3].text.strip()
    except Exception:
        print('Get details of idea failed!')
        print(traceback.format_exc())

def getNumberOfPages(soup):
    global numberOfPage
    try:
        result = soup.find('div', attrs={'class': 'pagination'})
        link = result.contents[1].contents[4].contents[0].get('href')
        x = re.search('(\d+){2}', link)
        # print(int(x[0]))
        return int(x[0])
    except Exception:
        print('Get number of page failed')
        print(traceback.format_exc())
        return -1

ideas = []
def getIdeasFromPage(URL, category):
    global key
    global ideas
    global numberOfPage
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        #print(soup)
        if (key==0):
            numberOfPage = getNumberOfPages(soup)
            print(numberOfPage)
        table = soup.find('table', attrs={'class': 'table'}).tbody
        numberOfRow = len(table.contents)
        count = 3
        while count < numberOfRow:
            idea = {}
            key += 1
            idea['STT'] = key
            idea['URL'] = 'http://ytuongsangtao.net/' + (table.contents[count].contents[5].contents[0].get('href'))
            idea['Ho Ten'] = (table.contents[count].contents[3].contents[0].string.rstrip())
            idea['Dia Chi'] = (table.contents[count].contents[3].contents[2].text)
            idea['Tinh'] = (table.contents[count].contents[3].contents[4].text)
            idea['Mo Ta Ngan Gon'] = (table.contents[count].contents[5].text.rstrip())
            idea['Mo Ta Chi Tiet'] = getDetails(idea['URL'])
            idea['Ma So'] = (table.contents[count].contents[7].text)
            idea['Ngay Dang Ki'] = (table.contents[count].contents[9].text)
            idea['Danh muc'] = category
            count += 2
            ideas.append(idea)
            print(round((key/(numberOfPage*20))*100, 3), '%, SUCCESS: ', idea['URL'])
    except Exception:
        print('Get idea from page failed!')
        print(traceback.format_exc())

def getIdeasFromAllPage(urlCategory, category):
    i = 1
    global ideas
    while i <= numberOfPage:
        URL = urlCategory + "page-" + i.__str__() + "/"
        getIdeasFromPage(URL, category)
        writingToFile(ideas)
        ideas.clear()
        i+=1
    ideas=[]

#getIdeasFromAllPage()

# getIdeasFromAllCategory()