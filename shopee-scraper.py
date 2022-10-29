from datetime import date
from threading import Timer
import time
import requests
from yaspin import yaspin
from random import randint

#print date to help users to track down when the file was generated.
data = date.today()
data.strftime("%d/%m/%Y")
data1 = date.today()

#asks for seller id.
# seller_shopee_id = input('Type in the seller id: \n')
#hardcoded seller id.
seller_shopee_id = '12065998'

#shopee public api url.
url_api_request = 'https://shopee.com.my/api/v4/recommend/recommend?bundle=shop_page_product_tab_main&limit=999&offset=0&section=shop_page_product_tab_main_sec&shopid=' + seller_shopee_id
r = requests.get(url_api_request)

#define the number of ads published.
num_ads = (r.json()['data']['sections'][0]['data']['item'])
list_size = len(num_ads)

#loading starts here.
with yaspin(text="Fetching Product",timer=True , color="cyan") as sp:
#creates a while statement using the number of ads created. Since the (index) json file stars with 0, the while statment starts with -1. 
    creat_while = -1
    while creat_while < list_size - 1:
        creat_while += 1
        
        # print('No 1', creat_while)
        #store the information displayed inside the json file. It's possible to extract even more data, you only need to add the exact json's children path you're interested in. The scrapper will sleep for 1 second and then get the next ad's information.
        ad_id = (r.json()['data']['sections'][0]['data']['item'][creat_while]['itemid'])
        title = (r.json()['data']['sections'][0]['data']['item'][creat_while]['name'])
        stock = (r.json()['data']['sections'][0]['data']['item'][creat_while]['stock'])
        price = (r.json()['data']['sections'][0]['data']['item'][creat_while]['price'])
        # sales = (r.json()['data']['sections'][0]['data']['item'][creat_while]['historical_sold'])
        # likes = (r.json()['data']['sections'][0]['data']['item'][creat_while]['liked_count'])
        # views = (r.json()['data']['sections'][0]['data']['item'][creat_while]['view_count'])
        # rating = (r.json()['data']['sections'][0]['data']['item'][creat_while]['item_rating']['rating_count'][0])
        time.sleep(0.4)

        #you've to set where you wanna save the csv file. If you run the code without changing the directory settings, you'll get no data.
        # print(ad_id, '|', title, '|', stock, '|', price, '|', sales, '|', rating, '|', likes, '|', views, file=open("./%s-shopee_scraped.csv" % data, "a"))
        if title == 'Le Mood Clover Japan Dressmaking Silk Pin Jarum Peniti Sewing Pin Tailoring Pattern Making Tool Fix Position Pin':
            # sp.ok("✔ Product Found!")
            sp.ok()
            time.sleep(0.5)
            sp.write(text="✔ Product Found!")
            # print('Product: ',title ,'| Stock:', stock,)
            print('| Product: ',title )
            # print('| Price:', price )
            print('| Stock:', stock )
            print('AryNo: ',creat_while,'ID: ',ad_id,'Product:',title ,'| Stock:', stock, file=open("./%s-shopee_scraped.csv" % data, "a"))
            time.sleep(0.5)
            if stock <= 1:
                sp.write("✖ No Stock Yet :(")
                exit()
            else:
                sp.write("✔ STOCK FOUND! PLEASE CHECK!")
                sp.write('url: https://shopee.com.my/Le-Mood-Clover-Japan-Dressmaking-Silk-Pin-Jarum-Peniti-Sewing-Pin-Tailoring-Pattern-Making-Tool-Fix-Position-Pin-i.12065998.4229067630?sp_atk=205f0137-c883-4330-81dc-c472935b660c&xptdk=205f0137-c883-4330-81dc-c472935b660c')
                exit()
        #All items before the target item will be recorded in the csv file.
        print('AryNo: ',creat_while,'ID: ',ad_id,'Product:',title ,'| Stock:', stock, file=open("./%s-shopee_scraped.csv" % data, "a"))
        # print(ad_id, '|', title, '|', stock, '|', price, '|', sales, '|', likes, '|', file=open("~/Documents/Kambyan/test-lab/shopee-scraper/%s-shopee_scraped.csv" % data, "a"))

    # print('The scrapping is done. Your CSV file is ready!')
    # sp.ok("✔2")