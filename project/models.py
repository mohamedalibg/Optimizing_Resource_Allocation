from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    estimated_completion_time = models.PositiveIntegerField()  
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    assigned_engineers = models.ManyToManyField('resource.Engineer')
    skills_required = models.TextField()
    estimated_effort = models.PositiveIntegerField()  
    priority = models.PositiveIntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)  
    dependencies = models.ManyToManyField('self', blank=True, symmetrical=False)
    notes = models.TextField(blank=True)

    sprint_start_date = models.DateField(null=True, blank=True)
    sprint_end_date = models.DateField(null=True, blank=True)
    product_backlog = models.TextField(blank=True)
    sprint_backlog = models.TextField(blank=True)
    scrum_master = models.ForeignKey('resource.Engineer', on_delete=models.SET_NULL, null=True, blank=True, related_name='scrum_master_projects')
    product_owner = models.ForeignKey('resource.Engineer', on_delete=models.SET_NULL, null=True, blank=True, related_name='product_owner_projects')
    daily_standup_notes = models.TextField(blank=True)

    efficiency_ratio = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    client_satisfaction = models.IntegerField(default=0)
    historical_data_link = models.URLField(blank=True)
    forecast_accuracy = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    resource_overhead = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    skill_gap_notes = models.TextField(blank=True)
    risk_level = models.CharField(
        max_length=10, 
        choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], 
        default='low'
    )
    risk_mitigation_measures = models.TextField(blank=True)
    kpis = models.JSONField(default=dict)
    decision_impact_analysis = models.TextField(blank=True)
    compliance_status = models.TextField(blank=True)

    def __str__(self):
        return self.name
