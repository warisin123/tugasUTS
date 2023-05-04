from django.db import models

# Create your models here.
class JADWAL_IMSAKIYAH_1444_H(models.Model):
    tanggal = models.CharField(max_length=50)
    imsak   = models.TimeField(auto_created=False)
    subuh   = models.TimeField(auto_created=False)
    terbit  = models.TimeField(auto_created=False)
    duha    = models.TimeField(auto_created=False)
    zuhur   = models.TimeField(auto_created=False)
    Asar    = models.TimeField(auto_created=False)
    magrib  = models.TimeField(auto_created=False)
    isya    = models.TimeField(auto_created=False)

    def __str__(self):
        return self.tanggal