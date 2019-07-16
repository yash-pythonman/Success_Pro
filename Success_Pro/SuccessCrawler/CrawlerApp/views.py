from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import Template
from datetime import datetime
from django.views import View
from . import forms
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urlparse
# Create your views here.


def index(request):
    t = datetime
    time = t.now()
    form=forms.UrlForm
    return render(request, "CrawlerApp/index.html", {'form':form})


class MyHtmlParser(HTMLParser):
    s=set()

    def handle_starttag(self,tag,attrs):
        if tag == 'a':
            for name,value in attrs:
                if name == "href":
                    url = value
                    self.s.add(url)


class ImgParser(HTMLParser):
    image_list = set()

    def handle_startendtag(self, tag, attrs):
        if tag == 'img':
            for name, value in attrs:
                if name == 'src':
                    img=value
                    self.image_list.add(img)


class Crawler(View):
    list_of_link = []
    list_of_page = []
    sub_page = set()
    sub_links = set()
    links = set()
    page = set()
    list_of_image = []
    parser = MyHtmlParser()
    url = ''

    def get(self, request):
        if request.method == 'GET':
            self.list_of_link.clear()
            self.list_of_page.clear()
            self.links.clear()
            self.page.clear()
            self.parser.s.clear()
            data = request.GET
            Crawler.url = data.get('url')
            data=urlopen(self.url)
            url_data = data.read()
            html_data=url_data.decode("utf-8")
            self.parser.feed(html_data)
            final_data=self.parser.s
            for page in final_data:
                d1 = urlparse(page).netloc
                r1 = d1.split('.')
                if r1[-1] and r1[-2] in r1:
                    self.links.add(r1[-2]+'.'+r1[-1])
                else:
                    self.page.add(page)
            for page_url in self.page:
                self.page_crawler(page_url, self.url)
            content = {'final_data': final_data, 'links': self.links, 'page': self.page, 'url': self.url,
                       'list_of_page': self.list_of_page, 'list_of_link': self.list_of_link}
            return render(request, 'CrawlerApp/crawler.html',content)

    def page_crawler(self, page_url, home_url):
        self.sub_page.clear()
        self.list_of_page.clear()
        try:
            if home_url[-1] and page_url[0] == '/':
                home_url = home_url[:-1]
            data = urlopen(home_url+page_url)
            url_data=data.read()
            html_data=url_data.decode("utf-8")
            self.parser.feed(html_data)
        except:
            pass
        final_data = self.parser.s
        for page1 in final_data:
            d1 = urlparse(page1).netloc
            r1 = d1.split('.')
            if r1[-1] and r1[-2] in r1:
                self.sub_links.add(r1[-2] + '.' + r1[-1])
            else:
                if page1 in self.page:
                    pass
                else:
                    self.sub_page.add(page1)
        self.list_of_page.append(self.sub_page)


def find_image(url):
    img_parse=ImgParser()
    img_parse.image_list.clear()
    url_data=urlopen(url)
    data_read=url_data.read()
    html_data=data_read.decode('utf-8')
    img_parse.feed(html_data)
    print(type(url_data))
    return img_parse.image_list


def image_view(request):
    src_value = set()
    url = Crawler.url
    image = find_image(url)
    for src in image:
        img_prs = urlparse(src).scheme
        if img_prs != "":
            src_value.add(src)
        else:
            src_value.add(url+src)
    content = {'image': image, 'url': src_value}
    return render(request, 'CrawlerApp/image.html', content)


class ImageInUrl(View):
    pass




