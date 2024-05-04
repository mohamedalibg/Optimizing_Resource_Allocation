from django.db import models
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255, help_text="The name of the company.")
    email = models.EmailField(help_text="The company's primary contact email address.")
    phone = models.CharField(max_length=20, blank=True, help_text="The company's primary contact phone number.")
    address = models.TextField(blank=True, help_text="The mailing address for the company.")
    industry = models.CharField(max_length=100, blank=True, help_text="The industry sector the company operates within.")
    representative_name = models.CharField(max_length=255, blank=True, help_text="The name of the primary contact person for the company.")
    notes = models.TextField(blank=True, help_text="Any additional notes or important information about the company.")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
