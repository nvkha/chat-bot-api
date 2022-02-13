import random
import requests
from bs4 import BeautifulSoup

class NewsSkills:
    
    __categories = ["thế giới", "sức khỏe", "đời sống", "thời sự", "du lịch", "kinh doanh", 
        "khoa học", "giải trí", "xe", "thể thao", "pháp luật", "giáo dục", "công nghệ", "game", 
        "đời sống", "làm đẹp"]

    @classmethod
    def get_news(cls, question, limit = 5):
        category = random.choice(cls.__categories)
        for item in cls.__categories:
            if item in question:
                category = item
        
        try:
            URL_GOOOGLE_NEWS  = f"https://news.google.com/rss/search?q={category}&hl=vi&gl=VN&ceid=VN"
            response = requests.get(URL_GOOOGLE_NEWS)
            soup = BeautifulSoup(response.content, "xml")
            items = soup.find_all("item")
            news = []
            for item in items[:limit]:
                title = str(item.title.text).lower().replace("vietnamnet.vn", "việt nam net")
                title = title.replace("baotintuc.vn", "báo tin tức")
                title = title.replace("cafef.vn", "cà phê f")
                link = item.link.text
                news.append(title + "\n " + link)
            return news
        except Exception as e:
            print(e)
            return None
