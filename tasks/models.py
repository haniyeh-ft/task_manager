from django.db import models

# Create your models here.


# status


class Tasks(models.Model):
    STATUS_CHOICES=(
        ('in_progress' , 'In Progress'),
        ('completed' , 'Completed')
    )
    title = models.CharField(max_length=300, blank=False) #index
    detail = models.TextField( blank=True )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    # signe = user

    def __str__(self) -> str:
        return f'{self.title} - {self.status}'