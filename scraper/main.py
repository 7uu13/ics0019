import requests
from bs4 import BeautifulSoup

def fetch(url, headers):
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        return req.text
    else:
        print(f"Failed to retrieve page. Status code: {req.status_code}")
        return None

def parse_product_listings(content):
    soup = BeautifulSoup(content, 'lxml')
    listings = soup.find_all('li', class_='classifieds__item')
    product_links = []
    for listing in listings:
        link_tag = listing.find('a', class_='horiz-offer-card__image-link')
        if link_tag:
            link = link_tag.get('href')
            product_links.append(link)
    return product_links

def parse_each_listing(listing_url, headers):
    PREFIX = 'https://www.okidoki.ee'
    listing_page_url = PREFIX + listing_url
    listing_html = requests.get(listing_page_url, headers=headers).text
    listing_soup = BeautifulSoup(listing_html, 'lxml')

    title = listing_soup.find('h1').text
    price = listing_soup.find('p', class_='price').text
    description = listing_soup.find('div', class_='item-description-text').text

    return {
        'title': title,
        'price': price,
        'description': description
    }

def run(url, headers):
    content = fetch(url, headers)
    product_list = []
    
    if content:
        product_links = parse_product_listings(content)
        for listing in product_links:
            product_details = parse_each_listing(listing, headers)
            product_list.append(product_details)

    for product in product_list:
        print(product)
    print(len(product_list))

if __name__ == '__main__':
    MBP_URL = 'https://www.okidoki.ee/buy/all/?p=0&query=macbook+pro&c=0&pp=200'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Referer': 'http://www.google.com/'
    }

    run(MBP_URL, headers)
