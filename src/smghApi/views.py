from urllib.parse import quote
from django.shortcuts import render, get_object_or_404
from .models import Article, Subscriber, Comment
from django.http import HttpResponse
from .forms import CommentForm, ContactForm, SubscriberForm
from django.core.mail import send_mail, BadHeaderError
# Create your views here.

def index(request):
	#top-stories
	left_title = 'Reasons why Akuffo-Addo cannot save us'
	top_story_left = Article.objects.get(title=left_title)

	right_title = 'You are unemployed becasuse you lack skill'
	top_story_right = Article.objects.get(title = right_title)

	articles = Article.objects.all().exclude(title=left_title).exclude(title=right_title).order_by("-id")


	form = SubscriberForm
	subscriber_form_handler(request)

	context={
		'articles':articles,
		'subscriber_form':form,
		'top_story_left':top_story_left,
		'top_story_right':top_story_right,
	}
	return render(request, 'smgh/index.html', context)

def subscriber_form_handler(request):
	if request.method == 'POST':
		form = SubscriberForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']

			subscriber = Subscriber.objects.create(email=email)
			subscriber.save()

			form = SubscriberForm
		else:
			HttpResponse('Invalid form input')


def about_view(request):
	form = SubscriberForm
	subscriber_form_handler(request)

	context = {
		'subscriber_form':form,
	}
	return render(request, 'smgh/about.html', context)

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

	post_path = request.get_full_path()

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
		'post_path':post_path,
	}
	return render(request, 'smgh/post_detail.html', context)
