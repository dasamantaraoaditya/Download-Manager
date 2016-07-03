import urllib2
import threading

def get_file_name(url):
    url = url.split("/")
    return url[url.__len__() - 1]

def write_into_file(file_name,response):
    with open(file_name, 'wb+') as f: f.write(response.read())
    f.close()

def join_thread_images(url):
    fp_main_image=open(get_file_name(url),'ab+')

    for i in xrange(5):
        file_name = "test" + str(i)
        with open(file_name, 'rb') as fp_inter_image: fp_main_image.write(fp_inter_image.read())

    fp_main_image.close()

def download(url):
    response = urllib2.urlopen(url)
    file_name=get_file_name(url)
    length= int(response.info()['Content-Length'])

    threads = []
    for i in range(5):
        t = threading.Thread(target=parts, args=(url, i*(length/4),(i+1)*(length/4),i))
        threads.append(t)
        t.start()
        t.join()

    response.close()  # best practice to close the file
    join_thread_images(url)

def parts(url,start,end,index):
    req = urllib2.Request(url)
    req.headers['Range'] = 'bytes=%s-%s' % (start, end)
    f = urllib2.urlopen(req)
    file_name = "test"+str(index)
    write_into_file(file_name, f)
    f.close()



if __name__=="__main__":
    url = 'https://www.apple.com/osx/all-features/pdf/osx_elcapitan_core_technologies_overview.pdf'
    download(url)
    print "successfully Downloaded"
