from django.shortcuts import render
from mnogo import classify


def index(request):

    classified_tweet = "hello world"

    return render(request, "sent_app/index.html",
                  {'today': classified_tweet})

def classify_tweet(request):

    if request.GET['q']:
        message = 'The sentiment of this document is {0}'.format(
            classify(request.GET['q']))
    else:
        message = 'You submitted an empty form.'
    return render(request,
                  'sentimeter/result.html',
                  {'result': message, })


