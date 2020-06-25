from django.shortcuts import render
from .models import RequestItem
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def requests(request):
    all_requests = RequestItem.objects.all()
    context = {'all_requests': all_requests}
    return render(request, 'requests/main.html', context)

def addReq(request):
        req = request.POST['content']
        all_req = RequestItem.objects.all()
        if req in all_req:
            new_req = RequestItem(content = req)
            new_req.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Request already present please upvote it or add a new request.')

def upvote(request, request_id):
    upvote_req = RequestItem.objects.get(id = request_id)
    upvote_req.votes += 1
    upvote_req.save()
    return HttpResponseRedirect('/')