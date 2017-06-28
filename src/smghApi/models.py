from django.db import models

tags = (
	('Entrepreneurship', 'Entrepreneurship'),
	('Politics', 'Politics'),
	('Personal development', 'Personal development'),
	('Startups','Startups'),
	('Religion', 'Religion')
	)

class Article(models.Model):
	title = models.CharField(max_length = 300)
	content = models.TextField()
	category = models.CharField(choices=tags, max_length=40)
	data_created = models.DateField(auto_now_add = True)
	image = models.FileField(upload_to='media/')
	views = models.PositiveIntegerField(blank=True, default=0)
	shares = models.PositiveIntegerField(blank=True, default=0)

	def __str__(self):
		return self.title


class Comment(models.Model):
	message = models.TextField()
	sender = models.CharField(max_length=100, blank = True, null = True)
	article = models.ForeignKey(Article, null=False)



class Discussion(models.Model):
	topic = models.TextField()
	category = models.CharField(choices=tags, max_length=40)

	def __str__(self):
		return self.topic

class Suggestion(models.Model):
	message = models.TextField()
	sender = models.CharField(max_length=100, blank = True, null = True)
	discussion = models.ForeignKey(Discussion, null=False)
