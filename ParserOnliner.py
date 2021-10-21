from bs4 import BeautifulSoup
import requests

url = 'https://people.onliner.by/' #ссылка на ресурс

page = requests.get(url)

#print(page.status_code)# 200 - успешное подключение

soup = BeautifulSoup(page.text, 'html.parser') #выбираем режим

def news(main_link, link_link, title_link, span_or_div):
    filteredPosts = []
    link = []

    allPosts = soup.findAll('div', class_= main_link) #блок с новостью

    for data in allPosts:
        links = data.find("a", {'class': link_link}) #блок с ссылкой

        if data.find('a', class_=link_link) is not None:
            link.append(links.get('href')) #из блока с ссылкой достаем саму ссылку
            data = data.find(span_or_div, {'class': title_link}) #блок с заголовком новости
            filteredPosts.append(data.text) #из блока с зоголовком достаем текст

    times = 0

    for data in filteredPosts:
        print("\n================")
        print(data.strip() + "\n" + 'https://people.onliner.by' + str(link[times]))
        print("================")
        LinksList.write("\n================\n" + data.strip() +
                        '\n' + 'https://people.onliner.by' +
                        str(link[times]) + "\n================")
        times = times + 1
        if times == -1: #если нужно поставить ограничение (например 10)
            break

LinksList = open("Onliner.txt", "w")

news("news-tidings__item news-tidings__item_1of3 news-tidings__item_condensed",
    "news-tidings__stub",
     "news-helpers_hide_mobile-small",
     "span") #в функцию передаем названия классов блоков и тип блока с заголовком (div, span и т.д.)

news("news-tidings__item news-tidings__item_1of3",
     "news-tiles__stub",
     "news-tiles__subtitle",
     "div")

LinksList.close()
