from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

tags = (
	('Entrepreneurship', 'Entrepreneurship'),
	('Politics', 'Politics'),
	('Personal development', 'Personal development'),
	('Startups','Startups'),
	('Religion', 'Religion')
	)


class Article(models.Model):
	slug = models.SlugField(unique=True, blank=True)
	title = models.CharField(max_length = 300)
	content = models.TextField()
	category = models.CharField(choices=tags, max_length=40)
	data_created = models.DateField(auto_now = True, blank = False, null=False)
	image = models.ImageField(upload_to='media')
	views = models.PositiveIntegerField(blank=True, default=0)
	shares = models.PositiveIntegerField(blank=True, default=0)
	likes = models.PositiveIntegerField(blank=True, default=0)

	def __str__(self):
		return self.title


class Comment(models.Model):
	message = models.TextField()
	article = models.ForeignKey(Article, null=False)



class Discussion(models.Model):
	slug = models.SlugField(unique=True)
	topic = models.TextField()
	category = models.CharField(choices=tags, max_length=40)

	def __str__(self):
		return self.topic

class Suggestion(models.Model):
	message = models.TextField()
	sender = models.CharField(max_length=100, blank = True, null = True)
	discussion = models.ForeignKey(Discussion, null=False)

class Subscriber(models.Model):
	email = models.EmailField(max_length=255, blank=False, null=False)


#function to generate slug field for better urls
def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Article.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=slug)
	return slug

def pre_save_article_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_article_receiver, sender=Article)