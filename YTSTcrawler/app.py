import requests
import traceback
import re
from bs4 import BeautifulSoup
import csv
from writingToFile.write import writingToFile as writer

class App:
    fieldsname = ['STT', 'URL', 'Ho Ten', 'Dia Chi', 'Tinh', 'Mo Ta Ngan Gon', 'Mo Ta Chi Tiet', 'Ma So',
                  'Ngay Dang Ki', 'Danh muc']
    numberOfPage = 9999
    nameFile = 'database.csv'
    key = 0
    ideas = []
    category = ''
    URL = ''
    page = 1
    urlCategory = ''

    def __init__(self, urlCategory, category):
        self.URL = urlCategory + "page-" + self.page.__str__() + "/"
        self.urlCategory = urlCategory
        self.category = category
    #
    # def writingToFile(self, ideas):
    #     try:
    #         filename = self.nameFile
    #         with open(filename, 'a') as f:
    #             w = csv.DictWriter(f, self.fieldsname)
    #             for idea in ideas:
    #                 w.writerow(idea)
    #     except Exception:
    #         print('Error occurred while writing file!')
    #         print(traceback.format_exc())

    def getDetails(self, DetailsURL):
        try:
            r = requests.get(DetailsURL)
            _soup = BeautifulSoup(r.content, 'html5lib')
            table = _soup.find('div', attrs={'class': 'col-md-9 table-responsive right_form'}).tbody
            return table.contents[9].contents[3].text.strip()
        except Exception:
            print('Get details of idea failed!')
            print(traceback.format_exc())

    def getNumberOfPages(self, soup):
        global numberOfPage
        try:
            result = soup.find('div', attrs={'class': 'pagination'})
            link = result.contents[1].contents[4].contents[0].get('href')
            numbers = re.findall('(\d+)', link)
            return max(int(numbers[0]), int(numbers[1]))
        except Exception:
            print('Get number of page failed')
            print(traceback.format_exc())
            return -1

    def getIdeasFromPage(self, URL, category):
        global key
        global ideas
        global numberOfPage
        try:
            r = requests.get(URL)
            soup = BeautifulSoup(r.content, 'html5lib')
            #print(soup)
            if (self.key==0):
                self.numberOfPage = self.getNumberOfPages(soup)
                # print(category,' ', self.numberOfPage, '\n')
            table = soup.find('table', attrs={'class': 'table'}).tbody
            numberOfRow = len(table.contents)
            count = 3
            while count < numberOfRow:
                idea = {}
                self.key += 1
                idea['STT'] = self.key
                idea['URL'] = 'http://ytuongsangtao.net/' + (table.contents[count].contents[5].contents[0].get('href'))
                idea['Ho Ten'] = (table.contents[count].contents[3].contents[0].string.rstrip())
                idea['Dia Chi'] = (table.contents[count].contents[3].contents[2].text)
                idea['Tinh'] = (table.contents[count].contents[3].contents[4].text)
                idea['Mo Ta Ngan Gon'] = (table.contents[count].contents[5].text.rstrip())
                idea['Mo Ta Chi Tiet'] = self.getDetails(idea['URL'])
                idea['Ma So'] = (table.contents[count].contents[7].text)
                idea['Ngay Dang Ki'] = (table.contents[count].contents[9].text)
                idea['Danh muc'] = category
                count += 2
                self.ideas.append(idea)
                print('Task ', idea['Danh muc'],' ', round((self.key/(self.numberOfPage*20))*100, 3), '%, SUCCESS: ', idea['URL'])
        except Exception:
            print('Get idea from page failed!')
            print(traceback.format_exc())

    def getIdeasFromAllPage(self):
        global ideas
        global page
        while self.page <= self.numberOfPage:
            self.URL = self.urlCategory + "page-" + self.page.__str__() + "/"
            self.getIdeasFromPage(self.URL, self.category)
            self.writer(self.ideas)
            self.ideas.clear()
            self.page+=1
        ideas=[]

#getIdeasFromAllPage()

# getIdeasFromAllCategory()

# item = "Ẩm thực"
# newURL = 'http://ytuongsangtao.net/am-thuc-ili2/'
# print(newURL)
# app = App
# app.getIdeasFromAllPage(app, item)