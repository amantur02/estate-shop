from django.db import models

from users.models import Profile


class Estate(models.Model):
    PROPERTY_TYPE = (
        ('Land house', 'Land house'),
        ('Apartment', 'Apartment'),
    )
    ESTATE_STATUS = (
        ('Sale', 'Sale'),
        ('Sold', 'Sold'),
        ('Rent', 'Rent'),
    )
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                               blank=True, null=True, related_name='author_posts')
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.FloatField()
    location = models.CharField(max_length=255)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE, blank=True)
    status = models.CharField(max_length=10, choices=ESTATE_STATUS, blank=True)
    area = models.FloatField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    garage = models.IntegerField()
    main_image = models.ImageField(upload_to='estates')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    chosen = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField(upload_to='estates', null=True)
    estate_image = models.ForeignKey(Estate, on_delete=models.CASCADE)
