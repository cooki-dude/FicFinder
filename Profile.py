from Fanfic import Fanfic

class Profile:
    tag_ratings = {}

    def __init__(self, initial_fics:list[Fanfic]=[]):
        for i in initial_fics:
            for j in i.tags():
                if j not in self.tag_ratings:
                    self.tag_ratings[j] = 1
                else:
                    self.tag_ratings[j] += 1
    
    def get_tag_ratings(self, tag:str):
        return self.tag_ratings[tag]
    
    def add_tag(self, i:str):
        if i not in self.tag_ratings:
            self.tag_ratings[i] = 1
        else:
            self.tag_ratings[i]+=1
    
    def add_tags(self, tags:list):
        for i in tags:
            if i not in self.tag_ratings:
                self.tag_ratings[i] = 1
            else:
                self.tag_ratings[i] += 1

    def decrement_tag(self, i:str):
        if i not in self.tag_ratings:
            self.tag_ratings[i] = -1
        else:
            self.tag_ratings[i] -= 1
    
    def decrement_tags(self, tags:list):
        for i in tags:
            if i not in self.tag_ratings:
                self.tag_ratings[i] = -1
            else:
                self.tag_ratings[i] -= 1

