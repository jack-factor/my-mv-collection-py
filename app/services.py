from bs4 import BeautifulSoup
from app.models import CollectionMV
import requests
import os


class CollectionApi():

    def get_list():
        data = CollectionMV.get_all()
        result = []
        for item in data:
            result.append(
                {'id': item.id, 'title': item.title, 'image': item.image,
                 'path_image': item.path_image,
                 'is_exist': item.is_exist})
        return result

    def check_exist(pk):
        return CollectionMV.check(pk)


class ScrapWeb():

    def save():
        data = ScrapWeb.get_data()
        for item in data:
            # save
            row = CollectionMV(
                title=item['title'], description=item['description'],
                path_image=item['image'], image='', is_exist=False,
                ord_publication=item['ord']).save()
            if row is False:
                return False
        return True

    def get_data():
        data_object = ScrapWeb._get_scrapp_data()
        count = 0
        result = []
        for item in data_object:
            count += 1
            row = ScrapWeb._get_data_item(item, count)
            result.append(row)
        return result

    def _get_scrapp_data():
        web_path = os.environ.get('SOURCE_WEB', '')
        r = requests.get(web_path)
        soup = BeautifulSoup(r.text, 'lxml')
        # content
        content_data = soup.find('div', class_='entry-content clear')
        result = content_data.find_all('div', class_='wp-block-column')
        return result

    def _get_data_item(data_html, num_ord):
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
        return result
