from django.db import models
import base64
import struct


# url will be stored
class Url(models.Model):
    # urls longer than 2083 char don't work in some browsers anyway
    MAX_LENGTH = 2083
    url = models.CharField(max_length=MAX_LENGTH, unique=True)
    # the url will be shortened to http://domain.com/<short_string>
    short_string = models.CharField(max_length=200, unique=True)

    @staticmethod
    def shorten(url):
        if Url.objects.filter(url=url).exists():
            return Url.objects.get(url=url).short_string
        else:
            new = Url(url=url)
            new.save()
            new.short_string = Url.int_to_string(new.id)
            new.save()
            return new.short_string

    @staticmethod
    def int_to_string(int):
        # transform int in bytestring
        bytes = struct.pack(">i", int).lstrip(chr(0)) or chr(0)
        # convert the bytestring string to characters and numbers
        return base64.b32encode(bytes).strip('=').lower()