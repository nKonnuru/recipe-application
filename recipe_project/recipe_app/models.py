from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100, db_index=True)  # Index for title searches
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)  # Index for date filtering

    def __str__(self):
        return self.title