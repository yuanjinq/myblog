from django.shortcuts import render
from django.utils import timezone
from .models import Post

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_view(request):
    #return HttpResponse("Hello World! From Jerry Coding")
    return render(request, 'blog/index.html')
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})