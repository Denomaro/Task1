#Лекция 1

#Задание 1

def domain_name(url):
    keys = ['https://www.', 'https://', 'http://www.', 'http://', 'www.']
    for i in keys:
        if i in url:
            url = url[len(i):]
            url = url[:url.find('.')]
            return url
    return url[:url.find('.')]
