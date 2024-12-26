from bs4 import BeautifulSoup
import requests


class KunUzNews:
    def __init__(self):
        pass

    def songi_yangiliklar(self):
        response = requests.get("https://kun.uz")
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all("p", class_="main-news__right-text")
        news = []
        for i in range(len(data)):
            news.append(data[i].text)
        return news

    def yangilik(self):
        response = requests.get("https://kun.uz/news/category/uzbekiston")
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find_all("h3", class_="main-news__left-hero-title")[0].text.replace('\n', '').replace('  ', '')
        body = soup.find_all("p", class_="main-news__left-hero-text")[0].text.replace('\n', '').replace('  ', '')
        return {'title': title, 'body': body}
    
    def yangiliklar(self):
        response = requests.get("https://kun.uz/news/category/uzbekiston")
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all("div", class_='news-page__list')
        a_tags = BeautifulSoup(str(data), 'html.parser')
        datas = [f"https://kun.uz{a.get('href')}" for a in a_tags.find_all('a')]
        titles = []
        descs = []
        for i in range(len(datas)):
            response = requests.get(datas[i])
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find("h1", class_="news-inner__content-title").text
            desc = soup.find("p", class_="news-inner__content-desc")
            titles.append(title)
            descs.append(desc.text)
        return {'titles': titles, 'descs': descs}

    def jahon_yangiliklari(self):
        response = requests.get("https://kun.uz/news/category/jahon")
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all("div", class_="news-page__list")
        a_tags = BeautifulSoup(str(data), 'html.parser')
        datas = [f"https://kun.uz{a.get('href')}" for a in a_tags.find_all('a')]
        titles = []
        descs = []
        for i in range(len(datas)):
            response = requests.get(datas[i])
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find("h1", class_="news-inner__content-title")
            desc = soup.find("p", class_="news-inner__content-desc")
            titles.append(title.text)
            descs.append(BeautifulSoup(str(desc), 'html.parser').text)
        return {'titles': titles, 'descs': descs}
