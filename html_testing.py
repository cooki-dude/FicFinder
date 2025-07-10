from bs4 import BeautifulSoup
from Fanfic import Fanfic

with open("bookmarks.html", "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# marked in an ordered list with class "bookmark index group"

tsoup = BeautifulSoup('<html><p class="test index group">a web page</p></html>', 'html.parser')

def search_criteria(tag):
    if not tag.has_attr('class'):
        return False
    return 'index' in tag['class'] and 'group' in tag['class']




bm_list = soup.find(search_criteria)
user_bms = bm_list.contents

ffs = [Fanfic(i) for i in user_bms if not i == "\n"]
print(ffs)
print(len(ffs))