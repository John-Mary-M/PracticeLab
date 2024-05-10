from django.db import models

# Create your models here.
class TodoItem(models.Model):
    '''represents a todo list'''
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        '''returns string representation of 
        TodoItems model
        '''
        return f'Activity: {self.title} Status: {self.completed}'