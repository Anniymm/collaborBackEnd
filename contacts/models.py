from django.db import models

class contactsUs(models.Model):
    phone = models.CharField(max_length=40)
    email = models.EmailField()
    time = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.phone