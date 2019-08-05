import time, requests, re, xlrd, sys, xlrd, xlwt
import xml.etree.cElementTree as ET
from bs4 import BeautifulSoup
from random import choice
from datetime import datetime


class Html:
    def get_html(self, URL):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
        self.html = requests.get(URL, headers=headers).text
        # print(self.html)
        # input()
        return self.html

    def sleep_time(self):
        mas = [1, 2, 3, 4]
        pausa = choice(mas)
        time.sleep(pausa)

class Get_price:
    def price_dronestore(self, html):
        mas=[]
        soup = BeautifulSoup(html, "lxml")
        price = soup.find('p', class_="price").find_all('span', class_="woocommerce-Price-amount amount")[-1].text[:-4]
        mas.append(price)
        try:
            status = soup.find('p', class_="stock out-of-stock").text
        except: status=''
        mas.append(status)
        return mas


    def price_4copter(self, html):
        soup = BeautifulSoup(html, "lxml")
        price = soup.find_all('h2', class_="vc_custom_heading")[1].text[5:-5]
        return [price, '']

    def price_modelistam(self, html):
        mas=[]
        try:
            soup = BeautifulSoup(html, "lxml")
            price = soup.find_all('div', class_="price_block")[0].find('div').text.replace(' ', '')[:-3]
        except:
            soup = BeautifulSoup(html, "lxml")
            price = soup.find_all('div', class_="price_block")[0].find('p', class_='price_in').text.replace(' ', '')[:-3]
        mas.append(price)
        try:
            status = soup.find('div', class_="footer_prod_extra_buy").find('div', class_="tovar_nalich_2").text
        except: status=''
        mas.append(status)
        return mas

    def price_game_shop(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")
        price = soup.find('span', class_="orig-price").text[:-4]
        mas.append(price)
        try:
            status = soup.find('div', class_="tab__hit").text
        except: status=''
        mas.append(status)
        return mas

    def price_copterland(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")
        price = soup.find('div', class_="summary entry-summary").find_all('span', class_="woocommerce-Price-amount amount")[-1].text.replace(',', '').replace('.', '').replace('00 грн', '')
        mas.append(price)

        try:
            status = soup.find('p', class_="stock out-of-stock").text
        except: status=''
        mas.append(status)
        return mas

    def price_kopter(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")
        try:
            price = soup.find('div', id="product").find('span', class_="price-new").text.replace(' грн.', '')
            mas.append(price)
        except:
            price = soup.find('div', id="product").find('span', class_="price").text.replace(' грн.', '')
            mas.append(price)

        try:
            status = soup.find('p', class_="stock out-of-stock").text
        except:
            status = ''
        mas.append(status)
        return mas

    def price_foxtrot(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")
        try:
            price = soup.find('div', class_="widget-information").find('div', class_="price__relevant").find('span', class_="numb").text
            mas.append(price)
        except:
            price = soup.find('div', class_="widget-information").find('span', class_="numb").text
            mas.append(price)

        try:
            status = soup.find('a', class_="purchase__button").text
        except:
            status = ''
        mas.append(status)
        return mas

    def price_skycopter(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")

        price = soup.find('span', class_="product-price-data").text
        mas.append(price)

        try:
            status = soup.find('a', class_="purchase__button").text
        except:
            status = ''
        mas.append(status)
        return mas

    def price_moyo(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")

        try:
            price = soup.find('span', class_="price-block-amount").text
            price_tru=''
            for i in price:
                try:
                    if int(i) <= 9 and int(i) >= 0:
                        price_tru +=str(i)

                except: pass
            mas.append(price_tru)
        except:
            price=0
            mas.append(price)

        try:
            status = soup.find('div', class_="status").text
        except:
            status = ''
        mas.append(status)
        return mas

    def price_gamestore(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")
        price = soup.find('div', class_="sidebar").find('div', class_="now")#.find('span').text
        price_tru = ''
        for i in str(price):
            try:
                if int(i) <= 9 and int(i) >= 0:
                    price_tru += str(i)
            except: pass
        mas.append(price_tru)
        status = ''
        mas.append(status)

        return mas

    def price_radiomodel(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")
        price = soup.find('span', class_="autocalc-product-price").text
        price_tru = ''
        for i in str(price):
            try:
                if int(i) <= 9 and int(i) >= 0:
                    price_tru += str(i)
            except:
                pass
        mas.append(price_tru)
        try:
            status = soup.find_all('div', class_="col-sm-6 col-md-6")[-1].text
        except:
            status = ''
        mas.append(status)
        return mas

    def price_yukke(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")
        try:
            price = soup.find('span', class_="numbers block").text.replace(' ', '').replace('грн', '')
        except:
            price = 0

        try:
            status = soup.find('span', class_="product__main-availability product__main-availability_type_ok").text
        except:
            status = soup.find('span', class_="product__main-availability product__main-availability_type_fail").text

        mas.append(price)
        mas.append(status)
        return mas

    def price_aks(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")

        price = soup.find('span', class_="price__value").text
        mas.append(price)

        try:
            status = soup.find('div', class_="itemcols clearfix").find('span', class_="availability inactive").text
        except:
            status = soup.find('div', class_="itemcols clearfix").find('span', class_="availability active").text
        mas.append(status)
        return mas

    def price_deshevshe(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")
        try:
            price = soup.find('span', class_="product__price_current").text.replace(' грн', '')
        except:
            price = soup.find('span', class_="product__price_new").text.replace(' грн', '')
        mas.append(price)

        try:
            status = soup.find('span', class_="product__price_presence").text
        except:
            status = soup.find('div', class_="itemcols clearfix").find('span', class_="availability active").text
        mas.append(status)
        return mas

    def price_stylus(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")
        try:
            price = soup.find('div', id="product-layout").find('div', class_="regular-price").text.replace('грн', '').replace(' ', '')
        except:
            price = 0
        mas.append(price)
        try:
            status = soup.find('div', id="product-layout").find('div', class_="center-part").find('div', class_="availability available").text
        except:
            status = ''
        if len(status) == 0:
            try:
                status = soup.find('div', id="product-layout").find('div', class_="center-part").find('button',
                                                                                                      class_="buy-btn disabled").text
            except: status = soup.find('div', id="product-layout").find('div', class_="center-part").find('div',
                                                                                                      class_="availability not-available").text

        mas.append(status)
        return mas

    def price_rc_hobby(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")

        price = soup.find('div', class_="price_hide ").find('div', class_="price").text.split('грн')
        if len(price) == 3 : price = price[1].replace('\n', '').replace('\t', '').replace(' ', '')
        elif len(price) == 2: price = price[0].replace('\n', '').replace('\t', '').replace(' ', '')
        else: price = 0

        mas.append(int(price))

        try:
            status = soup.find('div', class_="price_hide ").find('div', class_="diAvail").text.replace('\n', '').replace('\t', '')
        except:
            status = ''

        mas.append(status)
        return mas

    def price_gadgitec(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")
        try:
            price = soup.find('span', class_="main-price").text.replace('\nгрн\n', '').replace(' ', '')
        except:
            price = 0
        try:
            status = soup.find('span', class_="availability").text
        except:
            status = ''

        mas.append(price)
        mas.append(status)
        return mas

    def price_allprosale(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")
        try:
            price = soup.find('h2').find('span', class_="label label-success").text.replace(' ', '').replace('грн', '')
        except:
            price = 0
        try:
            status = soup.find('span', class_="label label-danger").text
        except:
            status = ''
        mas.append(price)
        mas.append(status)

        return mas

    def price_sanford(self, html):
        mas = []
        soup = BeautifulSoup(html, "lxml")
        try:
            price = soup.find('div', class_="priceBig").text.replace(' грн.', '').replace(' ', '')
        except:
            price = 0
        try:
            status = soup.find('div', class_="alert-alt alert-success-alt").text.replace('\n', '')
        except:
            status = ''
        mas.append(price)
        mas.append(status)

        return mas

    def find_func_get_price(self, URL):
        self.dict_func = {"dronestore":self.price_dronestore, "4copter":self.price_4copter, "modelistam":self.price_modelistam \
            , "game-shop": self.price_game_shop, "copterland": self.price_copterland, "kopter": self.price_kopter,\
            "foxtrot": self.price_foxtrot, "skycopter": self.price_skycopter, "moyo": self.price_moyo, "gamestore": self.price_gamestore \
            , "radiomodel": self.price_radiomodel, "yukke": self.price_yukke, "aks": self.price_aks, "deshevshe": self.price_deshevshe \
            , "stylus": self.price_stylus, "rc-hobby": self.price_rc_hobby, "gadgitec": self.price_gadgitec, "allprosale": self.price_allprosale \
            , "sanford": self.price_sanford}
        return self.dict_func.get(URL)

class Exel:

    def read_file(self):
        try:
            self.rb = xlrd.open_workbook('list_url.xlsx')
            self.sheet = self.rb.sheet_by_index(0)
        except:
            print('Нe найден файл с именем list_url.xlsx.\n ')
            input()
            sys.exit()
        self.count_param = len([self.sheet.row_values(rownum) for rownum in range(self.sheet.nrows)][0])
        self.count_line = len([self.sheet.row_values(rownum) for rownum in range(self.sheet.nrows)])

    def push_URL_in_dict(self):
        self.URL_dict = {self.sheet.row_values(i)[1]:[self.sheet.row_values(i)[1], self.sheet.row_values(i)[2]] \
                         for i in range(self.count_line) if len(self.sheet.row_values(i)[1])>=1}
        return self.URL_dict

    def tru_URL(self, url):
        url = url.split('//')
        if url[1][0] != 'w':
            self.URL = url[0] + '//www.' + url[1]
        else: self.URL = url[0] + '//' + url[1]
        return self.URL


class Violators:                                        # Класс нарушителей
    def initialization_Exel_file(self):
        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet('List')

    def writer(self, line, column, value, name_file):
        self.ws.write(line, column, value)
        self.wb.save(name_file)

    def write_status(self, line, status, name_file):
        self.ws.write(line, 3, status)
        self.wb.save(name_file)

    def initialization_param_Exel(self, name_file):
        self.ws.write(0, 0, "URL")
        self.ws.write(0, 1, "Оur price")
        self.ws.write(0, 2, "Price on website")
        self.ws.write(0, 3, "Status")
        self.wb.save(name_file)




class Clock_parsing:
    def get_time(self):
        try:
            text = open('time_parsing.txt').readlines()
            # print(text)
            # self.mas_time = [i[:-1] for i in text if len(i) == 6 or len(i) == 5] # читаем в файле только время. Вместо пустых строк и т.д.
            self.mas_time = []
            for i in text:
                if len(i) == 6 or len(i) == 5:
                    if len(i) == 5:
                        self.mas_time.append(i)
                    else: self.mas_time.append(i[:-1])
            print(self.mas_time)

            return self.mas_time
        except:
            print('Не найден файл time_parsing.txt')
            input()
            sys.exit()

    def system_time(self):
        while(1):
            time.sleep(3)  # изменить на 20
            now = datetime.now()
            self.hour = str(now)[11:13]
            self.minute = str(now)[14:16]
            for i in self.mas_time:
                hour = i.split('.')[0]
                minute = i.split('.')[1]
                if int(hour) == int(self.hour) and int(minute) == int(self.minute):
                    year = str(now)[:4]
                    manth = str(now)[5:7]
                    day = str(now)[8:10]

                    name_file = hour + '.' + minute + ' = ' + day + '.' + manth + '.'  + year + '.xls'
                    print(name_file)
                    # наш код
                    Violatores = Violators()
                    Violatores.initialization_Exel_file()
                    Violatores.initialization_param_Exel(name_file)

                    data = Exel()
                    data.read_file()
                    dict_URL = data.push_URL_in_dict()

                    link = Html()

                    shop_price = Get_price()

                    line = 0

                    for key in dict_URL.keys():
                        try:
                            line += 1
                            html = link.get_html(key)

                            url = data.tru_URL(key)
                            name_site = url.split(".")[1]
                            func_for_get_price = shop_price.find_func_get_price(name_site)
                            price_status = func_for_get_price(html)

                            price_site = int(price_status[0])
                            # price_in_Exel = int(dict_URL.get(key)[1])
                            link.sleep_time()
                            # print(price_site, price_in_Exel)
                            # if price_site < price_in_Exel:  # сравниваем цену в прайсе и на сайте

                            print(str(dict_URL.get(key)[0]), " ", str(dict_URL.get(key)[1]), " ",
                                    str(price_site), " ", str(price_status[1]))
                            our_price = str(dict_URL.get(key)[1])
                            if len(our_price) == 0 : our_price = 0

                            Violatores.writer(line, 0, str(dict_URL.get(key)[0]), name_file)
                            Violatores.writer(line, 1, our_price, name_file)
                            Violatores.writer(line, 2, str(price_site), name_file)
                            Violatores.write_status(line, str(price_status[1]), name_file)

                        except:
                            print('Error: ', key)
                            Violatores.writer(line, 0, key, name_file)
                            Violatores.write_status(line, 'Error URL', name_file)








if __name__ == '__main__':

    checkTimeParsing = Html()
    stroka = checkTimeParsing.get_html('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=13DURFVRIdmuZcQq5SvqxTHidgqGMvGHe')
    print(stroka)
    if stroka == 'Ok':
        time_parsing = Clock_parsing()
        time_parsing.get_time()
        time_parsing.system_time()
    else:
        print('\n\n\n\nОшибка интернат соединения, или закончился пробный период использования программы! vladprogramer@gmail.com ')
        input()
        sys.exit()
    #
    # Violatores = Violators()
    # Violatores.initialization_Exel_file()
    # Violatores.initialization_param_Exel()
    #
    # data = Exel()
    # data.read_file()
    # dict_URL = data.push_URL_in_dict()
    #
    # link = Html()
    #
    # shop_price = Get_price()
    #
    #
    #
    #
    #
    #
    # line = 0
    #
    # for key in dict_URL.keys():
    #     html = link.get_html(key)
    #
    #     url = data.tru_URL(key)
    #     name_site = url.split(".")[1]
    #     func_for_get_price = shop_price.find_func_get_price(name_site)
    #     price_status = func_for_get_price(html)
    #
    #     price_site = int(price_status[0])
    #     price_in_Exel = int(dict_URL.get(key)[1])
    #     link.sleep_time()
    #     print(price_site, price_in_Exel)
    #     if price_site < price_in_Exel  :  # сравниваем цену в прайсе и на сайте
    #         line+=1
    #         print('Нашли', str(dict_URL.get(key)[0]), " ", str(dict_URL.get(key)[1]), " ", str(price_site), " ", str(price_status[1]))
    #
    #         Violatores.writer(line, 0, str(dict_URL.get(key)[0]))
    #         Violatores.writer(line, 1, str(dict_URL.get(key)[1]))
    #         Violatores.writer(line, 2, str(price_site))
    #         Violatores.write_status(line, str(price_status[1]))
    #     else: print(price_site)


