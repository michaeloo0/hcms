from django.db import models

# patient records

class PatientRecords(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    content = models.TextField(max_length=200, verbose_name='Title')
    desc = models.CharField(max_length=200, verbose_name='Title')
    
    class Meta:
        db_table = 'patient_records'
        
class MedicalHistory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    content = models.TextField(max_length=200, verbose_name='Content')
    desc = models.CharField(max_length=200, verbose_name='Describe')
    
    class Meta:
        db_table = 'medical_history'
        
class TreatmentInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    content = models.TextField(max_length=200, verbose_name='Content')
    desc = models.CharField(max_length=200, verbose_name='Describe')
    
    class Meta:
        db_table = 'treatment_info'