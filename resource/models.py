from django.db import models

# Create your models here.
from djongo import models

class Engineer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    skills = models.TextField(help_text="Comma-separated list of skills")
    certifications = models.TextField(help_text="Comma-separated list of certifications")
    availability = models.BooleanField(default=True, help_text="True if available for new projects")
    current_projects = models.TextField(help_text="Description of current project engagements")
    hire_date = models.DateField()
    contract_type = models.CharField(max_length=100)
    notes = models.TextField(blank=True, help_text="Additional notes about the engineer")
    salary = models.DecimalField(max_digits=10, decimal_places=2, help_text="Annual salary in USD")

    def __str__(self):
        return self.name
