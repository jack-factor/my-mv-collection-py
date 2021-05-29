# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import os

load_dotenv()

web_path = os.environ.get('SOURCE_WEB', '')
r = requests.get(web_path)
soup = BeautifulSoup(r.text, 'lxml')
# content
content_data = soup.find('div', class_='entry-content clear')
item_list = content_data.find_all('div', class_='wp-block-column')


def get_data_item(data_html, num_ord):
    image_obj = data_html.find('img')
    title_obj = data_html.find('h4')
    content_obj = data_html.find('div', class_='ugb-accordion__content')
    content_text = ''
    if content_obj:
        content_text = content_obj.text
    title = ''
    if title_obj:
        title = title_obj.text
    image = ''
    if image_obj['src']:
        image = image_obj['src']
    title = title_obj.text
    result = {
        'image': image, 'title': title, 'description': content_text, 'ord': num_ord}
    print(result)
    return result


# read items
count = 0


for item in item_list:
    count += 1
    # print(item)
    get_data_item(item, count)
    print('-----------------')
print(count)
