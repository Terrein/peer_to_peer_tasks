def get_absolute_url(url, *args, **kwargs):
    """ Сборка url-адресса по входящим параметрам. 
    :param ulr: обязательный аргумент.
    :param *args: позиционный(е) аргумент(ы). Возможен ввод любого кол-ва аргументов
    :param **kwargs: именованный(е) аргумент(ы). Возможен ввод любого кол-ва аргументов
    """  
    str_url = ""
    for el in args:
        str_url += el.strip() + "/"
    str_url = str_url + "?"
    for k, v in kwargs.items():
        str_url += ((k.strip()) + "=" + str(v).strip() + "&")
    str_url = str_url[:-1]
    return(url + "/" + str_url)

# https://www.da-office.ru/store/zashitnii-kovriki-pod-kreslo/bsl-100-x-120-sm-1-2-mm-matovyy-pesok-polipropilen/?utm_source=YM&utm_medium=cpc&utm_content=bsl-100-x-120-sm-1-2-mm-matovyy-pesok-polipropilen&utm_campaign=zashitnii-kovriki-pod-kreslo&r1=&ymclid=16012405962867952112500007
#Тестовый вывод
print(get_absolute_url('www.da-office.ru', 'store', 'zashitnii-kovriki-pod-kreslo', 'bsl-100-x-120-sm-1-2-mm-matovyy-pesok-polipropilen', utm_source='YM',
                       utm_medium='cpc', utm_content='bsl-100-x-120-sm-1-2-mm-matovyy-pesok-polipropilen', 
                       utm_campaign='zashitnii-kovriki-pod-kreslo', r1='', ymclid=16012405962867952112500007))

#Тестовый вывод
print(get_absolute_url('yandex.ru','news', utm_source='main_stripe_big'))

""" Сделал в двух вариантах т.к. считаю, что с / перед ? правильнее. 
В некоторых случаях не влияет на вывод, но можете затестировать ввывод например с такой ссылкой: 
https://www.da-office.ru/store/zashitnii-kovriki-pod-kreslo/bsl-100-x-120-sm-1-2-mm-matovyy-pesok-polipropilen/?utm_source=YM&utm_medium=cpc&utm_content=bsl-100-x-120-sm-1-2-mm-matovyy-pesok-polipropilen&utm_campaign=zashitnii-kovriki-pod-kreslo&r1=&ymclid=16012405962867952112500007
в ней принципиален / перед ? """

def get_absolute_url_2(url, *args, **kwargs):
    """ Сборка url-адресса по входящим параметрам. 
    :param ulr: обязательный аргумент.
    :param *args: позиционный(е) аргумент(ы). Возможен ввод любого кол-ва аргументов
    :param **kwargs: именованный(е) аргумент(ы). Возможен ввод любого кол-ва аргументов
    """  
    str_url = ""
    for el in args:
        str_url += el.strip() + "/"
    str_url = str_url[:-1] + "?"
    for k, v in kwargs.items():
        str_url += ((k.strip()) + "=" + str(v).strip() + "&")
    str_url = str_url[:-1]
    return(url + "/" + str_url)
    
#Тестовый вывод
print(get_absolute_url_2('www.da-office.ru', 'store', 'zashitnii-kovriki-pod-kreslo', 'bsl-100-x-120-sm-1-2-mm-matovyy-pesok-polipropilen', utm_source='YM',
                       utm_medium='cpc', utm_content='bsl-100-x-120-sm-1-2-mm-matovyy-pesok-polipropilen', 
                       utm_campaign='zashitnii-kovriki-pod-kreslo', r1='', ymclid=16012405962867952112500007)) 

#Тестовый вывод   
print(get_absolute_url_2('yandex.ru','news', utm_source='main_stripe_big'))
