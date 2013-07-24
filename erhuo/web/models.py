from django.db import models

# Create your models here.
# user table
class User(models.Model):
	nickName = models.CharField(max_length = 50)
	email = models.EmailField()
	school = models.CharField(max_length = 50)
	telephone = models.CharField(max_length = 50)
	qq = models.CharField(max_length = 50)
	headUrl = models.CharField(max_length = 200)
	buyRating = models.IntegerField()
	sellRating = models.IntegerField()
	createdTime = models.DateTimeField()

# comment table
class Comment(models.Model):
	itemId = models.IntegerField()
	commentatorId = models.IntegerField()
	replayCommentId = models.IntegerField()
	createdTime = models.DateTimeField()

# bid table
class Bid(models.Model):
	itemId = models.IntegerField()
	buyerId = models.IntegerField()
	bidPrice = models.DecimalField(max_digits=10,decimal_places=2)
	createdTime = models.DateTimeField()
	
# chat table
class Chat(models.Model):
	speakerId = models.IntegerField()
	listenerId = models.IntegerField()
	content = models.TextField()
	createdTime = models.DateTimeField()
	
# order table
class Order(models.Model):
	itemId = models.IntegerField()
	buyerId = models.IntegerField()
	sellerId = models.IntegerField()
	dealPrice = models.DecimalField(max_digits=10,decimal_places=2)
	dealTime = models.DateTimeField()

# rating table
class Rating(models.Model):
	orderId = models.IntegerField()
	buyId = models.IntegerField()
	sellerId = models.IntegerField()
	content = models.TextField()
	mark = models.IntegerField()
	createdTime = models.DateTimeField()

# item table
class Item(models.Model):
	itemName = models.CharField(max_length = 100)
	itemDescription = models.TextField()
	expectedPrice = models.DecimalField(max_digits=10,decimal_places=2)
	sellerId = models.IntegerField()
	firstType = models.CharField(max_length = 50)
	secondType = models.CharField(max_length = 50)
	highestPrice = models.DecimalField(max_digits=10,decimal_places=2)
	createdTime = models.DateTimeField()
	itemSold = models.BooleanField()


 