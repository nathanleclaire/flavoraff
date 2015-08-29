from django.db import models
from django.contrib import admin

class Taste(models.Model):
    CHOICES = (
        ('SW', 'sweet'),
        ('AS', 'astringent'),
        ('SO', 'sour'),
        ('SA', 'salty'),
        ('BI', 'bitter'),
        ('UM', 'umami'),
    )
    name = models.CharField(max_length=2, choices=CHOICES)

    def __str__(self):
        return self.get_name_display()

class Function(models.Model):
    CHOICES = (
        ('HE', 'heating'),
        ('CO', 'cooling'),
    )
    name = models.CharField(max_length=2, choices=CHOICES)

    def __str__(self):
        return self.get_name_display()

class Weight(models.Model):
    CHOICES = (
        ('LI', 'light'),
        ('ME', 'medium'),
        ('HE', 'heavy'),
    )
    name = models.CharField(max_length=2, choices=CHOICES)

    def __str__(self):
        return self.get_name_display()

class Volume(models.Model):
    CHOICES = (
        ('QU', 'quiet'),
        ('ME', 'moderate'),
        ('LO', 'loud'),
    )
    name = models.CharField(max_length=2, choices=CHOICES)

    def __str__(self):
        return self.get_name_display()

class Technique(models.Model):
    CHOICES = (
        ('BA', 'bake'),
        ('BR', 'braise'),
        ('BO', 'boil'),
        ('DE', 'deep-fry'),
        ('GR', 'grill'),
        ('PA', 'pan roast'),
        ('PO', 'poach'),
        ('RA', 'raw'),
        ('RO', 'roast'),
        ('SI', 'simmer'),
        ('SF', 'stir-fry'),
        ('SA', 'saute'),
        ('SE', 'sear'),
        ('ST', 'steam'),
        ('SI', 'simmer'),
        ('PU', 'puree'),
    )
    name = models.CharField(max_length=2, choices=CHOICES)

    def __str__(self):
        return self.get_name_display()

class Season(models.Model):
    CHOICES = (
        ('AU', 'autumn'),
        ('WI', 'winter'),
        ('SP', 'spring'),
        ('SU', 'summer'),
    )
    name = models.CharField(max_length=2, choices=CHOICES)

    def __str__(self):
        return self.get_name_display()

class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    taste = models.ManyToManyField(Taste, blank=True)
    function = models.ManyToManyField(Function, blank=True)
    weight = models.ManyToManyField(Weight, blank=True)
    volume = models.ManyToManyField(Volume, blank=True)
    technique = models.ManyToManyField(Technique, blank=True)
    season = models.ManyToManyField(Season, blank=True)
    tips = models.CharField(max_length=200, blank=True)
    pairings = models.ManyToManyField('self', symmetrical=False, through='Pairing')

    def __str__(self):
        return self.name

class Pairing(models.Model):
    types = models.CharField(max_length=20) # e.g. "stock" ingredient might have listed types of "chicken", "fish", "beef"

    STRENGTH_CHOICES = (
        ('NO', 'normal'),
        ('ST', 'strong'),
        ('XS', 'extra-strong'),
    )

    # in the book some fields are bold and others are BOLD_ALL_CAPS, to indicate multiple chefs recommending the pairing.
    strength = models.CharField(max_length=2, choices=STRENGTH_CHOICES)

    def __str__(self):
        return self.get_strength_display()
