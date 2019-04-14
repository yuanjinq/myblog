from django.shortcuts import render
from django.utils import timezone
from .models import Post
from comment.models import Comment
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Post.objects.filter(
            published_date__lte=timezone.now()
        ).order_by('-published_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id=context['post'].id;
        post=Post.objects.get(id=id)
        comments=Comment.objects.filter(post=id)
        context['comments'] = comments
        return context
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Post.objects.filter(published_date__lte=timezone.now())
    
class PostListView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Post.objects.filter(
            published_date__lte=timezone.now()
        ).order_by('-published_date')   
    
def about_view(request):
    return render(request, 'blog/about.html')
def contact_view(request):
    return render(request, 'blog/contact.html')
