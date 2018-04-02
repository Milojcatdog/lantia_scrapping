__author__ = 'MiloJcatdog'
from Scrapping_web import scrapping_page

def list2div(list_notices, url):
    """
    Esta funcion convierte una lista de noticias en formato string-html para el renderizado.
    :param list_notices: 
    :param url: 
    :return: 
    """

    names = ['Image', 'Titulo', 'Contenido', 'Date']
    dict_tags = {'Titulo': u'<h2> {cont} </h2>',
                 'Contenido': u'<p> {cont} </p>',
                 'Date': u'<h6> {cont} </h6>'}

    div_tag = u'<div style="width: 400px; display: inline-block; padding: 35px;"> {cont} </div>'
    a_tag = u'<a href={href}> {cont} </a>'
    string_template = ''

    for notice in (list_notices):
        str_notice = ''

        for idx, content in enumerate(notice):
            if 'Image' in content:
                tag = a_tag.format(href=url+content['Url'], cont=u'<img src={href} height="42" width="42">'.format(href=url+content['Image']))
            else:
                tag = dict_tags[names[idx]].format(cont=a_tag.format(href=url+content['Url'], cont=content[names[idx]]))

            str_notice += (tag + '\n')

        string_template += (div_tag.format(cont=str_notice) + '\n')

    return string_template

if __name__ == '__main__':
    print list2div(*scrapping_page())

