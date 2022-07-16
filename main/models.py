from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=250, blank=False)

	def __str__(self):
		return self.name

class Book(models.Model):
	category = models.ForeignKey(Category, related_name='book', on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=False)
	description = models.TextField(max_length=250, blank=True)
	ISBN = models.TextField(max_length=15, blank=False)
	available = models.BooleanField(default=True)
	image  = models.ImageField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	

	def __str__(self):
		return self.name
