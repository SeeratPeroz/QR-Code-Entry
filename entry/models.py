from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField("Date of Birth")
    created_at = models.DateTimeField(auto_now_add=True)  
    is_active = models.BooleanField(default=False)  # New boolean field with default=False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Entry(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    entry_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} - {self.entry_time}"

class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
