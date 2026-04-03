from django.db import models

class TableGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MainWord(models.Model):
    serial_number = models.IntegerField()
    ultimish_word = models.CharField(max_length=100)
    english_translation = models.CharField(max_length=100)
    table = models.ForeignKey(TableGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.ultimish_word


class Submission(models.Model):
    TYPE_CHOICES = (
        ('new', 'New'),
        ('edit', 'Edit'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    ultimish_word = models.CharField(max_length=100)
    suggested_translation = models.CharField(max_length=100)
    target_word = models.ForeignKey(MainWord, null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')