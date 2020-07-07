from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('fixstreet1.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['link', 'title', 'reported_category',
                     'council_sent', 'description', 'images'])
for i in range(9521, 2187006):
    url = "https://www.fixmystreet.com/report/" + str(i)
    fetchHtml = requests.get(url).text
    try:
        soup = BeautifulSoup(fetchHtml, 'lxml')
        block = soup.find('div', class_='problem-header clearfix')
        title = block.h1.text
        reported_in = block.find('p', class_='report_meta_info')
        council_sent = block.find('p', class_='council_sent_info')
        description = block.find('div', class_='moderate-display')
        try:
            image_urls = []
            image_block = block.find('div', class_='update-img-set')
            for images in image_block.find_all('div', class_='update-img'):
                image = images.find('a', href=True)
                image_urls.append("https://www.fixmystreet.com"+image['href'])

        except:
            image_urls = None

        csv_writer.writerow([url, title, reported_in.text,
                             council_sent.text, description.p.text, image_urls])
    except:
        pass
    print(title)
    print(reported_in.text)
    print(council_sent.text)
    print(description.p.text)
csv_file.close()
