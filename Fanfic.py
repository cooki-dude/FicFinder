from bs4 import element
from warnings import warn

class Fanfic:
    title:str
    author:str
    authorURL:str
    summary:str
    chapters:str

    symbols:list[str]

    warnings:list[str]
    relationships:list[str]
    characters:list[str]
    freeforms:list[str]
    fandom:list[str]

    words: int
    kudos:int

    exists = True

    def __str__(self):
        out = ""
        out += f"title: {self.title}\n"
        out += f"author: {self.author} {self.authorURL}\n"
        out += f"chapters: {self.chapters}\n"
        out += f"symbols: {self.symbols}\n"
        out += f"tags: {self.tags}\n"
        out += f"{self.kudos} kudos, {self.words} words\n"
        out += self.summary
        return out

    def __init__(self, ff:element.Tag):
        if not ff.find(class_="works") == None:
            warn("This is a Series, not a Work. Exists = False")
            self.exists = False
            return

        #title, author, authorURL
        taf = ff.find("h4", "heading")
        self.title = taf.find("a").string

        author_raw = taf.find(rel = "author")
        self.author = author_raw.string
        self.authorURL = author_raw["href"]

        #symbols
        self.symbols = []
        rtags = ff.find(class_="required-tags").stripped_strings
        for i in rtags:
            self.symbols.append(i)

        #tags
        self.warnings = []
        self.relationships = []
        self.characters = []
        self.freeforms = []
        tags_raw = ff.find("ul", "tags")
        for i in tags_raw:
            if i == '\n':
                continue
            match i['class'][0]:

                case 'warnings':
                    self.warnings.append(next(i.stripped_strings))
                case 'relationships':
                    self.relationships.append(next(i.stripped_strings))
                case 'characters':
                    self.characters.append(next(i.stripped_strings))
                case 'freeforms':
                    self.freeforms.append(next(i.stripped_strings))

        #fandom (more tags)
        self.fandom = []
        fandom_raw = ff.find("h5", class_="fandoms").find_all("a")
        for tag in fandom_raw:
            self.fandom.append(tag.string)


        #summary
        summary_raw = ff.find(class_="userstuff summary").stripped_strings
        self.summary = ""
        for i in summary_raw:
            if not i == "\n":
                self.summary += i + "\n"

        #word count
        self.words = int("".join(ff.find("dd", "words").string.split(",")))

        # #chapter count
        # self.chapters = "".join([i for i in ff.find("dd", "chapters").stripped_strings])

        #kudos
        self.kudos = [i for i in ff.find("dd", "kudos").stripped_strings][0]

    def __str__(self):
        out = "\n"

        out += f"title: {self.title}\n"
        out += f"author: {self.author}\n"
        out += f"authorURL: {self.authorURL}\n"
        # out += f"chapters: {self.chapters}\n"
        out += f"words: {self.words}\n"
        out += f"kudos: {self.kudos}\n\n"

        out += f"symbols: {self.symbols}\n"
        out += f"warnings: {self.warnings}\n"
        out += f"relationships: {self.relationships}\n"
        out += f"characters: {self.characters}\n"
        out += f"freeforms: {self.freeforms}\n"

        out += f"summary: {self.summary}\n"

        return out

    def tags(self):
        return self.relationships + self.characters + self.freeforms