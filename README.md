# Shopee MY Scraper
A web scraper in python that extract sales, price, avaliable stock and more of a targeted seller in Malaysia.
I modified it to find a targeted item stock and check if it is available.

Python 3 was used to build the project. 

The Shopee public API is used to run the script.

# How to use it
1. The first thing you have to do is to find the seller's id. It's present in the product link.

Example:
https://shopee.com.my/Le-Mood-Clover-Japan-Dressmaking-Silk-Pin-Jarum-Peniti-Sewing-Pin-Tailoring-Pattern-Making-Tool-Fix-Position-Pin-i.12065998.4229067630
- 12065998 is the seller's id. That's required to run the script.
- 4229067630 is the product's id

2. Before running the code, change the file directory where you want to save the csv file generated what will contain all the data extracted.
 ```python
file=open("/YOUR-DIRECTORY/%s-YOUR-FILE-NAME.csv" % data, "a")
```
- The %s- right before the file name prints the date when the csv was generated. It's recommended to keep it that way, in order to track down your files.

3. Using the terminal, go to the script's folder and run:
 ```python
python3 shopee-scraper.py
```

Built Based on:
https://github.com/paulodarosa/shopee-scraper