from django.db import models


class Task(models.Model):
    taskTitle = models.CharField(max_length=300)
    taskDesc = models.TextField()

    def __str__(self):
        return self.taskTitle
