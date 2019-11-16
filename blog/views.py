from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.template.context import RequestContext
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})