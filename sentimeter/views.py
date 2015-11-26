# -*- coding: utf-8 -*-
import datetime
from django.utils.timezone import now
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    today = datetime.date.today()
    return render(request, "sentimeter/index.html",
                  {'today': today, 'now': now()})


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")


def display_meta(request):
    values = request.META.items()
    values = sorted(values)
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def search(request):
        # Dummy sentiment finder
    import random
    sentiment = ['positive', 'negative']
    if 'q' in request.GET:
        message = 'The sentiment of this document is {0}'.format(
            random.choice(sentiment))
    else:
        message = 'You submitted an empty form.'
    return render(request,
                  'sentimeter/result.html',
                  {'result': message, })


def feedback_thanks(request):
    message = 'Thank you for your feedback'
    return render(request,
                  'sentimeter/success.html',
                  {'success': message})
