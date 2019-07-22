from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import Template
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from . import forms
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urlparse
from .models import BaseUrl
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.


def index(request):
    form=forms.UrlForm
    return render(request, "CrawlerApp/index.html", {'form': form})


class MyHtmlParser(HTMLParser):
    url_set=set()

    def handle_starttag(self,tag,attrs):
        if tag == 'a':
            for name,value in attrs:
                if name == "href":
                    url = value
                    self.url_set.add(url)


class ImgParser(HTMLParser):
    image_set = set()

    def handle_startendtag(self, tag, attrs):
        if tag == 'img':
            for name, value in attrs:
                if name == 'src':
                    img=value
                    self.image_set.add(img)


def find_image(url):
    print("url in finding imgfun", url)
    img_parse=ImgParser()
    img_parse.image_set.clear()
    print("url in finding image", url)
    url_data=urlopen(url)
    data_read = url_data.read()
    html_data = data_read.decode('utf-8')
    img_parse.feed(html_data)
    return img_parse.image_set


def find_page(url):
    print("url in finding page", url)
    page_parse=MyHtmlParser()
    page_parse.url_set.clear()
    url_data=urlopen(url)
    data_read = url_data.read()
    html_data = data_read.decode('utf-8')
    page_parse.feed(html_data)
    return page_parse.url_set


def home_page(data):
    page_url=find_page(data)
    for page in page_url:
        url_parse = urlparse(page).netloc
        url_split = url_parse.split('.')
        if url_split[-1] and url_split[-2] in url_split:
            continue
        else:
            if '@' in page:
                continue
        if data.endswith('/') and page.startswith('/'):
            sup_page=data+page[1:]
        elif data.endswith('/') or page.startswith('/'):
            sub_page=data+page
        else:
            sub_page=data+"/"+page
        url=PageUrl(page=sub_page, pk=None)
        url.save()

def home_image(data):
    image_set=set()
    if data.endswith('/'):
        data=data
    else:
        data=data+"/"
    page_url=find_image(data)
    for image in page_url:
        if image.startswith('/'):
            image=image[1:]
        img_parse = urlparse(image).scheme
        if img_parse != "":
            sub_page_image=image
        else:
            sub_page_image=data+image
        image_set.add(sub_page_image)    
    return image_set  
        


@api_view(['GET', 'POST'])
def UrlDepthView(request):
    if request.method == 'POST':
        UrlDepth.objects.all().delete()
        seriazedata=UrlDepthSerializer(data=request.data)
        if seriazedata.is_valid():
            seriazedata.save()
            return Response("Data is created", status=status.HTTP_201_CREATED)
        return Response("method post but not workig", status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='GET':
        HttpResponse ("method is post")
    return HttpResponse("method is not get and not post", status.HTTP_400_BAD_REQUEST)


class PageUrlView(APIView):
    def post(self, request):
        PageUrl.objects.all().delete()
        data=UrlDepth.objects.values_list('url', flat=True)
        data=data[0]
        home_page(data)            
        urls = PageUrl.objects.all()
        serializeurl=PageUrlSerializers(urls, many=True)
        return Response(serializeurl.data, status=status.HTTP_200_OK)


class BaseUrlImageView(APIView):
    def post(self, request):
        BaseUrlImages.objects.all().delete()
        data=UrlDepth.objects.values_list('url', flat=True)
        data=data[0]
        image_set=home_image(data)
        for sub_page_image in image_set:
            url=BaseUrlImages(home_image=sub_page_image, pk=None)
            url.save()
        image = BaseUrlImages.objects.all()
        serializeimage=BaseUrlImagesSerializer(image, many=True)
        return Response(serializeimage.data, status=status.HTTP_200_OK)


class SubPageView(APIView):
    def post(self, request):
        page = SubPage.objects.all()
        serializpage=SubPageSerializer(page, many=True)
        return Response(serializpage.data, status.HTTP_200_OK)


class PageImagesView(APIView):
    def post(self, request):
        PageImages.objects.all().delete()
        data = PageUrl.objects.values_list('page', flat=True)
        for url in data:
            image_set=home_image(url)
            for sub_page_image in image_set:
                image=PageImages(page_image=sub_page_image, pk=None)
                image.save()
        image=PageImages.objects.all()
        serializimage=PageImagesSerializer(image, many=True)
        return Response(serializimage.data, status.HTTP_200_OK)



class Crawler(View):
    list_of_link = []
    list_of_page = []
    sub_page = set()
    sub_links = set()
    links = set()
    page = set()
    sub_page_url = set()
    list_of_image = set()
    parser = MyHtmlParser()
    url = ''
    depth = 0


    def get(self, request):
        if request.method == 'GET':
            self.list_of_link.clear()
            self.list_of_page.clear()
            self.sub_page.clear()
            self.sub_page_url.clear()
            self.links.clear()
            self.page.clear()
            self.list_of_image.clear()
            self.parser.url_set.clear()
            data = request.GET
            Crawler.url = data.get('url')
            Crawler.depth = data.get('depth')
            print(type(Crawler.depth))
            final_data=find_page(Crawler.url)
            print(Crawler.url)
            for page in final_data:
                url_parse = urlparse(page).netloc
                url_split = url_parse.split('.')
                if url_split[-1] and url_split[-2] in url_split:
                    self.links.add(url_split[-2]+'.'+url_split[-1])
                else:
                    if '@' in page:
                        continue
                    self.page.add(page)
            if self.depth == '1':
                final_image_data=find_image(Crawler.url)
                for image in final_image_data:
                    img_prs = urlparse(image).scheme
                    if img_prs != "":
                        self.list_of_image.add(image)
                    else:
                        self.list_of_image.add(Crawler.url+image)
            content = {'links': self.links, 'page': self.page, 'url': self.url,
                       'list_of_page': self.list_of_page, 'list_of_link': self.list_of_link,
                       'list_of_image': self.list_of_image}
            if Crawler.depth == '2':
                self.list_of_image.clear()
                for page_url in self.page:
                    if Crawler.url.endswith('/') and page_url.startswith('/'):
                        Crawler.url = Crawler.url[:-1]
                    self.sub_page_url.add(Crawler.url+page_url)
                for sub_page in self.sub_page_url:
                    if '@' in sub_page:
                        continue
                    print(sub_page)
                    final_image_data = find_image(sub_page)
                    for image in final_image_data:
                        img_prs = urlparse(image).scheme
                        if img_prs != "":
                            self.list_of_image.add(image)
                        else:
                            self.list_of_image.add(sub_page+image)
                    self.list_of_page.append(find_page(sub_page))
                for item in self.list_of_page:
                    if '@' in item:
                        continue
                    self.list_of_page.append(item)
                print(self.list_of_page)
                print(self.list_of_image)
                content = {'links': self.links, 'page': self.page, 'url': self.url,
                        'list_of_page': self.list_of_page, 'list_of_link': self.list_of_link, 'list_of_image':self.list_of_image}
            return render(request, 'CrawlerApp/crawler.html',content)


'''
def find_image(url):
    img_parse=ImgParser()
    img_parse.image_set.clear()
    for url in url:
        url_data=urlopen(url)
        data_read = url_data.read()
        html_data = data_read.decode('utf-8')
        img_parse.feed(html_data)
    return img_parse.image_set
'''


'''
def image_view(request):
    src_value = set()
    sub_page_url= set()
    sub_page_image=set()
    url = Crawler.url
    image = find_image(url)
    for src in image:
        img_prs = urlparse(src).scheme
        if img_prs != "":
            src_value.add(src)
        else:
            src_value.add(url+src)
    for page_url in Crawler.page:
        if Crawler.url.endswith('/') and page_url.startswith('/'):
            Crawler.url=Crawler.url[:-1]
        sub_page_url.add(Crawler.url+page_url)
    sub_page_image=map(find_image, sub_page_url)
    sub_page_image_list=list(sub_page_image)
    content = {'image': image, 'home_url': Crawler.url, 'url': src_value, 'sub_page_image':sub_page_image_list[0]}
    return render(request, 'CrawlerApp/image.html', content)
'''


'''
class BaseUrlView(APIView):
    queryset = BaseUrl.objects.all()
    serializer_class=BaseUrlImagesSerializer
'''



'''
class UrlDepthView(generics.ListCreateAPIView):

    queryset = UrlDepth.objects.all()
    serializer_class = UrlDepthSerializer
    def get_queryset(self,):
        print("this is queryset method")
'''


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['GET', 'POST'])
def BaseUrlView(request):
    if request.method == 'POST':
        data1=UrlDepth.objects.all()
        seriazedata=UrlDepthSerializer(data1, many=True)
        return Response(seriazedata.data, status=status.HTTP_200_OK)
    elif request.method == 'GET':
        Response("not workig properly", status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("method is not get and not post", status.HTTP_400_BAD_REQUEST)
