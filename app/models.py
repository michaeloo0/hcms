from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User

# patient records
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
)
class PatientRecords(models.Model):
    name = models.CharField(max_length=200, verbose_name='patient name')
    age = models.IntegerField(verbose_name='Age', default=0)
    attending = models.ForeignKey(User, on_delete=models.CASCADE,related_name='patient_record', blank=True, null=True)
    medical_history = models.ManyToManyField('MedicalHistory', related_name='medical_history')
    treatment_info = models.ManyToManyField('TreatmentInfo', related_name='treatment_info')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    health_status = models.CharField(max_length=200, verbose_name='Health Status')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
        
    class Meta:
        db_table = 'patient_records'
        
        
class MedicalHistory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    content = models.TextField(max_length=200, verbose_name='Content')
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='medical_history', blank=True, null=True)
    desc = models.CharField(max_length=200, verbose_name='Describe')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

        
    class Meta:
        db_table = 'medical_history'
        
        
class TreatmentInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    content = models.TextField(max_length=200, verbose_name='Content')
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='treatment_info', blank=True, null=True)
    desc = models.CharField(max_length=200, verbose_name='Describe')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
        
    class Meta:
        db_table = 'treatment_info'