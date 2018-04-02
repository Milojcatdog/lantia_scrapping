# coding: utf-8
__author__ = 'MiloJcatdog'
from BeautifulSoup import BeautifulSoup
from requests import get
from pprint import pprint

def scrapping_page():
    """
    Esta funcion obtiene realiza un scrapping sobre las noticias presentadas en la pagina
    de inicio de 'http://www.portafolio.co'. Dicho scrapping obtiene el titulo de la noticia,
    contenido de la noticia, fecha de la ultima actualizacion e imagen de la noticia.
    :return:
    """
    names_tags = ['Image', 'Titulo', 'Contenido']
    notices_list =  list()

    url_ = 'http://www.portafolio.co'
    url_scrapping = url_+ '/innovacion'
    res = get(url_scrapping)
    soup = BeautifulSoup(res.text)
    notices_tags = soup.findAll(attrs={'itemtype': 'http://schema.org/NewsArticle'})

    for div in notices_tags:
        notice = list()
        for idx, tag in enumerate(div.findAll('a')):
            content = tag.contents[0] if len(tag.contents) == 1 else tag.contents[1]['src']
            url = tag['href']
            notice.append({names_tags[idx]: content, 'Url': url})

        tag_date = div.findAll(attrs={'class':'listing-time'})
        date_notice = tag_date[0].contents[0] if len(tag_date) == 1 else ''
        notice.append({'Date': date_notice, 'Url': ''})
        notices_list.append(notice)

    return (notices_list[1:10], url_)


if __name__ == '__main__':
    print pprint(scrapping_page())
