from bs4 import BeautifulSoup
from Fanfic import Fanfic
from Profile import Profile
import requests

with open("bookmarks.html", "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# raw_website = requests.get("https://archiveofourown.org/users/iSoulatte/pseuds/iSoulatte/bookmarks")
# print(raw_website.headers['content-type'])
# print(raw_website.text)
# soup = BeautifulSoup(raw_website.text, 'html.parser')

def search_criteria(tag):
    if not tag.has_attr('class'):
        return False
    return 'index' in tag['class'] and 'group' in tag['class']

bookmark_list = soup.find(search_criteria)
user_bookmarks = bookmark_list.contents

# t = [i for i in user_bookmarks[11].find("ul", "tags") if not i == '/n']



ffs = [Fanfic(i) for i in user_bookmarks if not i == "\n" and "/works/" in str(i)]

profile = Profile(ffs)
t = dict(sorted(profile.tag_ratings.items(), key=lambda item: item[1]))

print(t)