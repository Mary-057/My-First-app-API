from django.db import models

# Create your models here.
class guests_registration(models.Model):
    date_recorded = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    room_number= models.IntegerField()
    number_of_days = models.IntegerField()
    number_of_nights = models.IntegerField()
    check_in_date = models.DateField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name} (Room {self.room_number})"
    # In guests_site/models.py
