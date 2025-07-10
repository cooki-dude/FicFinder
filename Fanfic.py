from bs4 import element

class Fanfic:
    title:str
    author:str
    authorURL:str
    summary:str
    chapters:str

    symbols:list[str]
    tags:list[str]

    words: int
    kudos:int

    def __init__(self, ff:element.Tag):
        if not ff.find(class_="works") == None:
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
        self.tags = []
        tags_raw = ff.find("ul", "tags").stripped_strings
        for i in tags_raw:
            self.tags.append(i)

        #fandom (more tags)
        fandom_raw = ff.find("h5", class_="fandoms").find_all("a")
        for tag in fandom_raw:
            self.tags.append(tag.string)


        #summary
        summary_raw = ff.find(class_="userstuff summary").stripped_strings
        for i in summary_raw:
            if not i == "\n":
                self.summary = i

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
        out += f"tags: {self.tags}\n"
        out += f"summary: {self.summary}\n"

        return out

