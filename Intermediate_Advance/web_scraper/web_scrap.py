# this file is for just practicing web scraping and learning how to use BeautifulSoup
import requests
from bs4 import BeautifulSoup

url="http://books.toscrape.com/"  # real practice website made for scraping
response=requests.get(url)
print(f'status code: {response.status_code}') #200 means everything is ok
soup=BeautifulSoup(response.text,'html.parser')

books=soup.find_all('article',class_='product_pod') # find all book containers on the page
print(f'Books found on this page:{len(books)}')

# look at the first book raw data
print("\nFirst book raw HTML:")
print(books[0])


#clean scraping of the books
# rating words to numbers converter

rating_map={
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}
def scrape_page(soup):
    books=soup.find_all('article',class_='product_pod')
    bk_list=[]

    for b in books:
        # extract title tags wise joa us ke andr  navigates nested HTML tags like folders
        title=b.find('h3').find('a')['title'] # title square bracketes means we want the value of the title attribute and  reads an HTML attribute, not the text
        price=b.find('p',class_='price_color').text.strip()
        price=price.replace("Â", "").replace('£','').strip()# remove the pound sign
        rat_class=b.find('p',class_='star-rating')['class'] # here class will give us a list like ['star-rating', 'Three'] of classes inside of irt
        rating_word=rat_class[1] # second element of the list will be the rating word
        rating=rating_map.get(rating_word,0) # convert the rating word to a number using the mapping dictionary
        bk_list.append({'title':title,'price':float(price),'rating':rating})

    return bk_list
all_books=scrape_page(soup)
print(f"\nfirst two books  without loop for checking : \n{all_books[:2]}")
for book in all_books:
    print(f"⭐  {book['rating']} | £{book['price']} | {book['title']}")