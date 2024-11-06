from django.db import models

class Stage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    progress = models.DecimalField(max_digits=5, decimal_places=2)  # Percentage

    def __str__(self):
        return self.name

class Task(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name="tasks")
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    assigned_to = models.CharField(max_length=100)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.stage.name})"

class Preference(models.Model):
    paper_type = models.CharField(max_length=50)  # e.g., "Technical", "General"
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name="preferences")
    other_criteria = models.TextField()  # Additional filtering criteria
