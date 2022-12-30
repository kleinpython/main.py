URL = 'http://www.manascinema.com/movies'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}


def get_html(url):
    req = requests.get(url=url, headers=HEADERS)
    return req


def get_data(html):
    soup = BS(html, 'html.parser')

    items = soup.find_all('div', class_="short_movie_info")
    movies = []
    for item in items:
        title = item.find("div", class_="pl-item-info-expandable").find("a").getText().split(" ")
        movies.append({
            "link": f"https://shina.kg{item.find('a').get('href')}",
            "size": title[1],
            "logo": title[2],
            "price": item.find("div", class_="price-wrapper").find("span").getText()

        })
    return movies

def parse():
    global cur_page
    html = get_html(URL)
    if html.status_code == 200:
        movies = []
        for i in range(1,3):
            html = get_html(f'{URL}?page={i}/')
            cur_page = get_data(html.text)
            movies.extend(cur_page)
        return movies
    else:
        raise Exception('не правильный запрос')


def parser():
    html = get_html(URL)
    data = get_data(html.text)
    return data


parser()