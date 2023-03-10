from urllib.request import urlopen
import requests, csv
from bs4 import BeautifulSoup

req = requests.get("https://www.billboard.com/charts/hot-100/2023-03-11/")  
html = req.text
bsObject = BeautifulSoup(html, "html.parser") 

# get data from billboard website
ranks = bsObject.select('div.pmc-paywall > div > div > div > div.chart-results-list.\/\/.lrv-u-padding-t-150.lrv-u-padding-t-050\@mobile-max > div > ul > li.o-chart-results-list__item.\/\/.lrv-u-background-color-black.lrv-u-color-white.u-width-100.u-width-55\@mobile-max.u-width-55\@tablet-only.lrv-u-height-100p.lrv-u-flex.lrv-u-flex-direction-column\@mobile-max.lrv-u-flex-shrink-0.lrv-u-align-items-center.lrv-u-justify-content-center.lrv-u-border-b-1.u-border-b-0\@mobile-max.lrv-u-border-color-grey > span.c-label.a-font-primary-bold-l.u-font-size-32\@tablet.u-letter-spacing-0080\@tablet')
songs = bsObject.select('div.pmc-paywall > div > div > div > div.chart-results-list.\/\/.lrv-u-padding-t-150.lrv-u-padding-t-050\@mobile-max > div > ul > li.lrv-u-width-100p > ul > li.o-chart-results-list__item.\/\/.lrv-u-flex-grow-1.lrv-u-flex.lrv-u-flex-direction-column.lrv-u-justify-content-center.lrv-u-border-b-1.u-border-b-0\@mobile-max.lrv-u-border-color-grey-light.lrv-u-padding-l-1\@mobile-max')

# save into a csv file
csv_filename = "20230311_chart.csv"
csv_open = open(csv_filename, 'w', encoding='UTF-8', newline='')
csv_writer = csv.writer(csv_open)
csv_writer.writerow(('Date','Rank','Title','Artist'))

for i in zip(ranks, songs):
    date = '2023-03-11'
    rank = i[0].text.strip()
    title = i[1].find('h3').text.strip()
    artist = i[1].find('span').text.strip()
    csv_writer.writerow([date, rank, title, artist])



