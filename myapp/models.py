from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    calories = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
