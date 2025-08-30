from django.db import models

CHOICES_NATIONALITH = (
    ('USA', 'Estados Unidos'),
    ('RU', 'Rússia'),
    ('BRA', 'Brasil'),
    ('IT', 'Itália'),
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=CHOICES_NATIONALITH,
        blank=True,
        null=True,
        )
    
    def __str__(self):
        return self.name
    