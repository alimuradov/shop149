from collections import defaultdict

from dbfread import DBF
import csv
import os
import ftplib


def ru_to_lat(st):
    if st == 'Аптека №149 (второй отдел)':
        return 'parafarm'
    elif st == 'Аптека №149 (ул. Хизроева 8)':
        return 'xizroeva'
    elif st == 'Аптека №149 (Агасиева 26А)':
        return 'agasieva26'            
    elif st == 'Аптека №149 (Агасиева 17А)':
        return 'agasieva17'
    elif st == 'Аптека №149 (Ленина 86)':
        return 'lenina86'
    elif st == 'Аптека №149 (ул. 345 ДСД 17)':
        return '345'
    elif st == 'Аптека №149 (ул. Сальмана 87А)':
        return 'salmana'
    elif st == 'Аптека №149 (г. Даг. Огни)':
        return 'ogni'
    elif st == 'Аптека №149 (ТЦ Глобус)':
        return 'globus'
    elif st == 'Аптека №149 (ул. Пушкина 50)':
        return 'pushkina'
    else:
        return ''                                     

def dbfcsv():
    # try:
    #     os.remove('/home/nariman/goods.csv')
    #     os.remove('/home/nariman/prices.csv')
    #     print('Old file succes delete ')
    # except:
    #     print("Error while deleting file ")    


    ftp = ftplib.FTP('192.168.88.115')
    ftp.login('nariman', '89285576366')
    print("Получен файл с каталогом")

    
    # Путь на нашем компьютере где сохранить файл.
    out = '/home/nariman/ostlocal.dbf'
    
    with open(out, 'wb') as f:
        ftp.retrbinary('RETR ' + 'ostlocal.dbf', f.write)

    #По партиям
    pills = DBF('/home/nariman/ost.dbf', encoding='cp866')
    
    #для каталога
    prices_pharmacy = DBF('/home/nariman/ostlocal.dbf', encoding='cp866')

    
    goods = []
    prices = []

    #для катлога
    for item in prices_pharmacy:
        table_row = []
        table_row.append(item['CODTMC']) #sku
        table_row.append('') #store_view_code
        table_row.append('Default') #attribute_set_code
        table_row.append('simple') #product_type
        table_row.append("Все товары/" + item['GROUP']) #categories
        table_row.append('base') #product_websites
        table_row.append("[" + str(item['CODTMC']) + "] " + item['NAMETMC']) #name
        table_row.append(item['MNN']) #description
        table_row.append(item['FACTORY']) #short_description
        table_row.append(1) #product_online
        table_row.append('') #tax_class_name
        table_row.append('Catalog, Search') #visibility
        table_row.append(item['PRICE']) #price
        table_row.append('') #special_price
        table_row.append('') #special_price_from_date
        table_row.append('') #special_price_to_date
        table_row.append('') #url_key
        table_row.append('') #meta_title
        table_row.append('') #meta_keywords
        table_row.append('') #meta_description
        table_row.append('') #created_at
        table_row.append('') #updated_at
        table_row.append('') #new_from_date
        table_row.append('') #new_to_date
        table_row.append('') #display_product_options_in
        table_row.append('') #map_price
        table_row.append('') #msrp_price
        table_row.append('') #map_enabled
        table_row.append('') #gift_message_available
        table_row.append('') #custom_design
        table_row.append('') #custom_design_to
        table_row.append('') #custom_layout_update
        table_row.append('') #page_layout
        table_row.append('') #product_options_container
        table_row.append('') #msrp_display_actual_price_type
        table_row.append('') #country_of_manufacture
        table_row.append('') #additional_attributes
        table_row.append(item['OST']) #qty
        table_row.append('') #out_of_stock_qty
        table_row.append('') #use_config_min_qty
        table_row.append('') #is_qty_decimal
        table_row.append('') #allow_backorders
        table_row.append('') #use_config_backorders
        table_row.append('') #min_cart_qty
        table_row.append('') #use_config_min_sale_qty
        table_row.append('') #max_cart_qty
        table_row.append('') #use_config_max_sale_qty
        table_row.append('') #is_in_stock
        table_row.append('') #notify_on_stock_below
        table_row.append('') #use_config_notify_stock_qty
        table_row.append('') #use_config_manage_stock
        table_row.append('') #use_config_qty_increments
        table_row.append('') #qty_increments
        table_row.append('') #use_config_enable_qty_inc
        table_row.append('') #enable_qty_increments
        table_row.append('') #is_decimal_divided
        table_row.append('') #website_id
        table_row.append('') #deferred_stock_update
        table_row.append('') #use_config_deferred_stock_update
        table_row.append('') #related_skus
        table_row.append('') #crosssell_skus
        table_row.append('') #upsell_skus
        table_row.append('') #hide_from_product_page
        table_row.append('') #custom_options
        table_row.append('') #bundle_price_type
        table_row.append('') #bundle_sku_type
        table_row.append('') #bundle_price_view
        table_row.append('') #bundle_weight_type
        table_row.append('') #bundle_values
        table_row.append('') #associated_skus

        goods.append(table_row)

    #для партий
    

    d = {}
    for item in pills:
        
        list_cluch = (ru_to_lat(item['NAMEPODR']), item['CODTMC'], 1)
        new_ost = d.get(list_cluch)
        if  new_ost == None:
            d[list_cluch] = int(item['OST'])
        else:
            d[list_cluch] = new_ost + int(item['OST'])

    for key in d:    
        table_price = []
        table_price.append(key[0]) #айди аптеки
        table_price.append(key[1]) #код товара
        table_price.append(key[2]) #какая то хрень
        table_price.append(d[key]) #остаток 
        prices.append(table_price)
        del table_price          



    table_header = []
    table_header.append('sku')
    table_header.append('store_view_code')
    table_header.append('attribute_set_code')
    table_header.append('product_type')
    table_header.append('categories')
    table_header.append('product_websites')
    table_header.append('name')
    table_header.append('description')
    table_header.append('short_description')
    table_header.append('product_online')
    table_header.append('tax_class_name')
    table_header.append('visibility')
    table_header.append('price')
    table_header.append('special_price')
    table_header.append('special_price_from_date')
    table_header.append('special_price_to_date')
    table_header.append('url_key')
    table_header.append('meta_title')
    table_header.append('meta_keywords')
    table_header.append('meta_description')
    table_header.append('created_at')
    table_header.append('updated_at')
    table_header.append('new_from_date')
    table_header.append('new_to_date')
    table_header.append('display_product_options_in')
    table_header.append('map_price')
    table_header.append('msrp_price')
    table_header.append('map_enabled')
    table_header.append('gift_message_available')
    table_header.append('custom_design')
    table_header.append('custom_design_to')
    table_header.append('custom_layout_update')
    table_header.append('page_layout')
    table_header.append('product_options_container')
    table_header.append('msrp_display_actual_price_type')
    table_header.append('country_of_manufacture')
    table_header.append('additional_attributes')
    table_header.append('qty')
    table_header.append('out_of_stock_qty')
    table_header.append('use_config_min_qty')
    table_header.append('is_qty_decimal')
    table_header.append('allow_backorders')
    table_header.append('use_config_backorders')
    table_header.append('min_cart_qty')
    table_header.append('use_config_min_sale_qty')
    table_header.append('max_cart_qty')
    table_header.append('use_config_max_sale_qty')
    table_header.append('is_in_stock')
    table_header.append('notify_on_stock_below')
    table_header.append('use_config_notify_stock_qty')
    table_header.append('use_config_manage_stock')
    table_header.append('use_config_qty_increments')
    table_header.append('qty_increments')
    table_header.append('use_config_enable_qty_inc')
    table_header.append('enable_qty_increments')
    table_header.append('is_decimal_divided')
    table_header.append('website_id')
    table_header.append('deferred_stock_update')
    table_header.append('use_config_deferred_stock_update')
    table_header.append('related_skus')
    table_header.append('crosssell_skus')
    table_header.append('upsell_skus')
    table_header.append('hide_from_product_page')
    table_header.append('custom_options')
    table_header.append('bundle_price_type')
    table_header.append('bundle_sku_type')
    table_header.append('bundle_price_view')
    table_header.append('bundle_weight_type')
    table_header.append('bundle_values')
    table_header.append('associated_skus')


    with open('/home/nariman/goods.csv', 'w', newline='') as fileGD:
        writerGoods = csv.writer(fileGD)
        writerGoods.writerow(table_header)
        for item in goods:
            writerGoods.writerow(item)


    table_header.clear()
    table_header.append('source_code')
    table_header.append('sku')
    table_header.append('status')
    table_header.append('quantity')
    with open('/home/nariman/price.csv', 'w', newline='') as filePR:
        writerPrice = csv.writer(filePR)
        writerPrice.writerow(table_header) 
        for item in prices:
            writerPrice.writerow(item)                   
        


    print("Writing complete")



    session = ftplib.FTP('192.168.88.115','nariman','89285576366')
    fileGoods = open('/home/nariman/goods.csv','rb') 
    session.storbinary('STOR goods.csv', fileGoods) 
    fileGoods.close()  

    filePrice = open('/home/nariman/price.csv','rb')                  # file to send
    session.storbinary('STOR price.csv', filePrice)     # send the file                    # close file and FTP
    filePrice.close()                                    # close file and FTP
    session.quit()
    print("File send ftp server")

dbfcsv()            
