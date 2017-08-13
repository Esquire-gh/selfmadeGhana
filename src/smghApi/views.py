from urllib.parse import quote
from django.shortcuts import render, get_object_or_404
from .models import Article, Subscriber, Comment
from django.http import HttpResponse
from .forms import CommentForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
# Create your views here.

def index(request):
	articles = Article.objects.all()

	context={
		'articles':articles,
	}
	return render(request, 'smgh/index.html', context)

'''
def subscriber_view(request):
	if request.method == 'POST':
		form = SubscriberForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']

			subscriber = Subscriber.objects.Create(email=email)
			subscriber.save()

	return HttpResponse('Thanks for your subscriptioin')
'''

def about_view(request):
	return render(request, 'smgh/about.html')

def contact_view(request):
	form = ContactForm
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			sender = form.cleaned_data['sender']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']

		recipient = ['ackon.k.richar@gmail.com']

		try:
			send_mail(subject, message, sender, recipient)
		except BadHeaderError:
			return HttpResponse('invalid header found')

		form = ContactForm

	context = {
		'contact_form': form,
	}
	return render(request, 'smgh/contact.html', context)

def post_detail(request, slug):
	article = Article.objects.get(slug=slug)
	article_comments = Comment.objects.filter(article = article)
	comment_count = len(article_comments)
	share_string = quote(article.title)

	form  = CommentForm
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			message = form.cleaned_data['message']

			comment = Comment.objects.create(article =article, message=message)
			comment.save()
			
			# refresh context variables after save
			form = CommentForm
			article_comments = Comment.objects.filter(article = article)
			comment_count = len(article_comments)

	context = {
		'article':article,
		'commentForm':form,
		'article_comments':article_comments,
		'comment_count': comment_count,
		'share_string':share_string,
	}
	return render(request, 'smgh/post_detail.html', context)