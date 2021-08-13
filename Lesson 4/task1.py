import requests
from lxml import html

url = 'https://yandex.ru/'
response = requests.get(url)
root = html.fromstring(response.text)

news_quantity = len(root.xpath('//*[@id="news_panel_news"]/ol[1]/li'))

all_news = []

for i in range(1, news_quantity+1):
    news_xpath = f'//*[@id="news_panel_news"]/ol[1]/li[{i}]/a/span/span/text()'
    news = root.xpath(news_xpath)[0].replace('\xa0',' ')

    source_xpath = f'//*[@id="news_panel_news"]/ol[1]/li[{i}]/a/span/div/object/@title'
    source = root.xpath(source_xpath)[0]

    link_xpath = f'//*[@id="news_panel_news"]/ol[1]/li[{i}]/a/@href'
    link = root.xpath(link_xpath)[0]

    all_news.append({
        'Заголовок': news,
        'Источник': source,
        'URl': link
    })
