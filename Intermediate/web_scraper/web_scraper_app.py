# first file was for practising and learning , this one include complete implementations parsing from 2 pages with comple flow and clean structure....
import requests
import time
from bs4 import BeautifulSoup
from pathlib import Path
import json

file=Path('Intermediate/web_scraper')
fl=file/'books.json'

empty_books=[]
rating_map={
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}
def web_scraper(soup):
    global empty_books
    books=soup.find_all('article',class_='product_pod')
    bkl=[]

    for b in books:
        title=b.find('h3').find('a')['title']
        price=b.find('p',class_='price_color').text.strip()
        price=price.replace("Â", "").replace('£','').strip()
        rat_class=b.find('p',class_='star-rating')['class']
        rating_word=rat_class[1]
        rating=rating_map.get(rating_word,0)
        bkl.append({'title':title,'price':float(price),'rating':rating})
        empty_books.append({'title':title,'price':float(price),'rating':rating})
    return bkl
       
def show_books(soup):
   
    Books = web_scraper(soup)
   
    print(f'Total no. Books scraped : {len(empty_books)}')
    time.sleep(3) # to avoid overwhelming the server with requests
    print('Scraping done...showing books...')
    for book in Books:
        print(f"⭐  {book['rating']} | £{book['price']} | {book['title']}")

def save_books(empty_books):
    if not empty_books:
        print('No books available to save.')
        return

    with open(fl,'w') as f:
        json.dump(empty_books, f, indent=4)
        print('Books saved to JSON')
    print('THE OVERALL SUMMARY IS : .......')
    high_list=[]
    print(f'Total no. Books scraped : {len(empty_books)}')
    filtered=[num for num in empty_books if num['rating']==4 or num['rating']==5]
    for i in empty_books:
        high_list.append(i['price'])
    print('⭐ Highest rated books: ...')
    for i,b in enumerate(filtered,start=1):
        print(f'{i}. {b['title']}')
    print(f'💰 Cheapest book: ...{min(high_list)}')
    print(f'💰 Most expensive book: ...{max(high_list)}')


def starter():
    for page in range(1, 3):  # pages 1 to 5
        if page == 1:
            url = "http://books.toscrape.com/"
            response = requests.get(url)
            print(f'status code: {response.status_code}')
            soup=BeautifulSoup(response.text,'html.parser')
            print(f'Scraping page no. {page} with url: {url}')
            show_books(soup)
      
        else:
            url = f"http://books.toscrape.com/catalogue/page-{page}.html"
            response = requests.get(url)
            print(f'status code: {response.status_code}')
            soup=BeautifulSoup(response.text,'html.parser')
            print(f'Scraping page no. {page} with url: {url}')
            show_books(soup)


def menu():
    ch=int(input('Enter 1 to scrape Books and show it \n'))
    if ch==1:
        print('Scraping Books and showing it...please wait')
        starter()
    else:
        print('Invalid choice')
    ch=int(input('Enter 2 to save Books in a JSON file\n'))
    if ch==2:
        print('Saving Books in a JSON file...please wait')
        save_books(empty_books)
    else:
        print('Invalid choice')

menu()
