from django.db import models
from main.models import Book
from django.contrib.auth import get_user_model
from django.dispatch import receiver 
from django.db.models.signals import post_save 
User = get_user_model()


class Rentage(models.Model):
	user = models.ForeignKey(User, related_name='user_cart', on_delete=models.CASCADE)
	books = models.ForeignKey(Book, related_name='cart_product', on_delete=models.CASCADE)
	total = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)






	



