import urllib2

def get_file_name(url):
    url = url.split("/")
    return url[url.__len__() - 1]

def write_into_file(file_name,response):
    with open(file_name, 'wb+') as f: f.write(response.read())
    f.close()

def download(url):
    response = urllib2.urlopen(url)
    file_name=get_file_name(url)
    print response.info()
    write_into_file(file_name,response)
    response.close()  # best practice to close the file

if __name__=="__main__":
    url ='http://rohinibarla.github.io/heros/01AlanKay.jpg'
    download(url)


