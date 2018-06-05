# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


from django.http import HttpResponse, Http404
import datetime as dt
from models import Article

# Create your views here.
def welcome(request):
    # return HttpResponse('Welcome to the Moringa Tribune')
    return render (request, 'welcome.html')

# def news_of_day(request):
#     date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    # day = convert_dates(date)
    # html = f'''
    #     <html>
    #         <body>
    #             <h1> News for {day} {date.day}-{date.month}-{date.year} <h1>
    #     </html>
    #         '''
    # return HttpResponse(html)

# def convert_dates(dates):

    # Function that gets the weekday number for the date.
    # day_number = dt.date.weekday(dates)
    # days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    # Returning the actual day of the week
    # day = days[day_number]
    # return day


# View Function to present news from past days
def past_days_news(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    return render(request, 'all-news/past-news.html', {"date": date,"news":news})

    # day = convert_dates(date)
    # html = f'''
    #     <html>
    #         <body>
    #             <h1> News for {day} {date.day}-{date.month}-{date.year} <h1>
    #     </html>
    #         '''
    # return HttpResponse(html)


def news_today(request):
    date = dt.date.today()
    news = Article.today_news()

    return render(request, 'all-news/today-news.html', {"date":date,"news":news})