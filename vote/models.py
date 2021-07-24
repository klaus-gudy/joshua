from django.db import models

class vote(models.Model):
    text = models.TextField()
    option_one_count = models.IntegerField(default= 0)
    option_two_count = models.IntegerField(default= 0)
    option_three_count = models.IntegerField(default= 0)

    def __str__(self):
        return 'vote #{}'.format(self.id)

class option(models.Model):
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)

    def __str__(self):
        return 'option #{}'.format(self.id)
