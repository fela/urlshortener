from django.db import models


# url will be stored
class Url(models.Model):
    # urls longer than 2083 char don't work in some browsers anyway
    MAX_LENGTH = 2083
    url = models.CharField(max_length=MAX_LENGTH)
    # the url will be shortened to http://domain.com/<short_string>
    short_string = models.CharField(max_length=200)