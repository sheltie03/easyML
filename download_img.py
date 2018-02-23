# -*- coding: utf-8 -*-
import requests
import re
import os


def save_image(filename, image):
    with open(filename, 'wb') as fp:
        fp.write(image)


def ext_pics_urls(target):
    urls = []
    response = requests.get(target)
    body = response.content
    pattern = r'//i.imgur.com/.*.jpg'
    match_list = re.findall(pattern, body)
    for img_url in match_list:
        urls.append('https:' + img_url)
    return urls


if __name__ == '__main__':
    os.mkdir('tmp')
    for page in range(2):
        target = 'https://imgur.com/gallery/hot/viral/page/'
        target += str(page)
        target += '/hit?scrolled&set=0'

        pic_list = ext_pics_urls(target)

        ind = 0
        for url in pic_list:
            filename = './tmp/' + str(page) + '_' + str(ind) + '.jpg'
            ind += 1
            response = requests.get(url)
            image = response.content
            save_image(filename, image)
