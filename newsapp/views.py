from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient

query = ''


def index(request):
    try:
        newsapi = NewsApiClient(api_key="d216e0827bec4110ab62ce195ed5e61e")
        top = newsapi.get_top_headlines(q=query)

        l = top['articles']
        desc = []
        news = []
        img = []

        for i in range(len(l)):
            f = l[i]
            news.append(f['title'])
            desc.append(f['description'])
            img.append(f['urlToImage'])
        mylist = zip(news, desc, img)
        if len(l) == 0:
            return render(request, 'empty.html', context={"q": query})
        else:
            return render(request, 'index.html', context={"mylist": mylist})
    except Exception as e:
        return render(request, template_name="error.html", context={"e": e})
