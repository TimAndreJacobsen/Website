from django.utils import timezone
from django.db import models


class Category(models.Model): # The Category table, used to save our categories in a table
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name # name to be shown when called

class TodoList(models.Model): # Todolist table name, used to hold the todo list
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"] # ordering by newest first
        #alt_ordering = ["-due_date"] # ordering by due_date

    def __str__(self):
        return self.title # name to be shown when called
