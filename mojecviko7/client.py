import http.client as httplib
import xml.etree.ElementTree as ET

class Error(Exception):
    pass

class CannotRetrieveUrlError(Error):
    def __init__(self, url):
        self.msg = "Cannot retrieve URL: " + url


class FeedItem(object):
    """
    Reprezentuje jeden item ve feedu, tzn.
    <item>
    ...
    </item>
    """
    # TODO 5

class Feed(object):
    """
    Reprezentuje feed, tzn. kanal, ve kterem jsou jednotlive prispevky.
    <channel>
    </channel>
    """
        
    def __init__(self, feed_xml):
        # tato promenna udrzuje string s XML daty, ktera byla
        # stazena ze serveru. Pouzijte ji pro parsovani XML.    
        self.feed_xml = feed_xml
        
        self.title, self.desc, self.lang = self.parse_feed_info()
        #self.title = self.parse_feed_info()[0]
        #self.desc = self.parse_feed_info()[1]
        #self.lang = self.parse_feed_info()[2]

    def print_info(self):
        print("=====================")
        print("Feed info:")
        print("Title: {}".format(self.title))
        print("Desc: {}".format(self.desc))
        print("Lang: {}".format(self.lang))
        print("=====================")
        print()

    def parse_feed_info(self):
        # TODO 2:z XML dat vrati trojici obsahujici informace o feedu
        # title, description, language
        # hint: ET.fromstring("xml string") - vytvoreni objektu na parzovani xml ze stringu
        # hint: find("nazev tagu") - metoda nad vyse uvedenym objektem - nalezeni nazvu tagu a vraceni objektu nad kterym lze dale pracovat
        # hint: text - atribut nad vracenym objektem (napr od find), ktery vrati textovou reprezentaci/hodnotu mezi tagy
        
        root = ET.fromstring(self.feed_xml)
        channel = root.find("channel")
        title = channel.find("title").text
        description = channel.find("description").text
        language = channel.find("language").text
        result = (title,description,language)
        return result

    def items(self):
        # TODO 3:z XML dat vrati vsechny itemy, ktere feed obsahuje
        # generujte list tuplu (title, desc, guid)
        #for "item" in self.feed_xml:
        result = []
        root = ET.fromstring(self.feed_xml)
        channel = root.find("channel")
        for x in channel.findall("item"):
            #x = FeedItem(item)
            #x = FeedItem()
            title = x.find("title").text
            description = x.find("description").text
            guid = x.find("guid").text
            result.append((title,description,guid))
        return result
        
            
        # Pro TODO 5 generujte instance tridy FeedItem
        # hint: findall("nazev tagu") - metoda objektu ET, ktera najde vsechny tagy s danym nazvem.
        
class Reader(object):
    """
    Reprezentuje RSS ctecku, ktera umi cist vice RSS feedu.
    Pro jednoduchost budeme pouze cist jeden RSS feed.
    """
    def __init__(self, url):
        self.url = url
        self.feed = None

    def fetch_feed(self):
        conn = httplib.HTTPConnection(self.url)
        conn.request("GET", "/")
        r = conn.getresponse()
        #print type(r.status), type(r.reason)
        if r.status != 200:
            raise CannotRetrieveUrlError(self.url)

        xml = r.read()
        self.feed = Feed(xml)
        self.feed.print_info()
        # TODO 1: doplnit vytvoreni objektu Feed do promenne self.feed
        #pro overeni splneni TODO 2 zde take zavolat metodu feed.print_info()
        

        conn.close()

    def read_feed(self):
        # TODO 4, X:z feedu precist itemy pomoci funkce feed.items() 
        #a vytisknout na obrazovku
        #print(self.feed.items())
        for i in self.feed.items():
            print("=====================")
            print("Article info:")
            print("Title: {}".format(i[0]))
            print("Desc: {}".format(i[1]))
            print("Guid: {}".format(i[2]))
            print("=====================")
            print()  
        

def main():
    url = 'localhost:9000'
    reader = Reader(url)

    try:
        reader.fetch_feed()
        reader.read_feed()
    except CannotRetrieveUrlError as e:
        print(e)

if __name__ == '__main__':
    main()
