from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
	articles = Article.objects.all()

	context={
		'articles':articles
	}
	return render(request, 'smgh/index.html', context)

def about(request):
	return render(request, 'smgh/about.html')

def post_detail(request, pk):
	article = Article.objects.get(pk=pk)
	context = {
		'article':article
	}
	return render(request, 'smgh/post_detail.html', context)