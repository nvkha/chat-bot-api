import requests
from bs4 import BeautifulSoup
import re
from googlesearch import search # Performing Google searches

class TextUtils:
    ## Copy at https://github.com/mailong25/bert-vietnamese-question-answering
    @staticmethod
    def get_content(url):
        html = requests.get(url, timeout = 3)
        tree = BeautifulSoup(html.text,'lxml')
        for invisible_elem in tree.find_all(['script', 'style']):
            invisible_elem.extract()

        paragraphs = [p.get_text() for p in tree.find_all("p")]

        for para in tree.find_all('p'):
            para.extract()

        for href in tree.find_all(['a','strong']):
            href.unwrap()

        tree = BeautifulSoup(str(tree.html),'lxml')

        text = tree.get_text(separator='\n\n')
        text = re.sub('\n +\n','\n\n',text)

        paragraphs += text.split('\n\n')
        paragraphs = [re.sub(' +',' ',p.strip()) for p in paragraphs]
        paragraphs = [p for p in paragraphs if len(p.split()) > 10]

    
        txt = '\n\n'.join(paragraphs)
        if len(txt) > 1000:
            for i in range(len(txt)):
                if i > 800 and txt[i] == ".":
                    return txt[:i + 1].replace(". .", ".")
        return txt.replace(". .", ".")
    
    @staticmethod
    def query_pages(query, n=1):
        return list(search(query, num_results=n ,lang="vi"))

    @staticmethod
    def format_text(text):
        text = text.replace('\n', ' ')
        return text
    
    @staticmethod
    def query_to_text(query):
        txt = ""
        for link in TextUtils.query_pages(query, 1):
            print(link)
            txt = TextUtils.get_content(link)
            txt = TextUtils.format_text(txt)
            if txt:
                return txt
        return ""
    
#print(TextUtils.query_to_text("Tác phẩm tắt đèn nói về nội dung gì"))