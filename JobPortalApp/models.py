from django.db import models
import datetime

# Create your models here.
class Company(models.Model):
    company_email = models.EmailField(max_length=50, default="")
    company_password = models.CharField(max_length=20, default="")
    company_name = models.CharField(max_length=50)
    company_id = models.AutoField(primary_key=True)
    company_about = models.TextField(max_length=255)
    website_link = models.URLField(max_length=200)

    def __str__(self):
        return self.company_name

class JobRole(models.Model):
    job_role_name = models.CharField(max_length=50)
    job_role_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_role_id = models.AutoField(primary_key=True)
    job_role_desc = models.TextField(max_length=255)
    job_role_location = models.CharField(max_length=50)
    job_role_salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_role_qualifications = models.CharField(max_length=50)
    job_role_type = models.CharField(max_length=3, choices=[("FT", "Full Time"), ("PT", "Part Time"), ("INT", "Internship")])
    job_role_mode = models.CharField(max_length=2, choices=[("R", "Remote"), ("H", "Hybrid"), ("IP", "In Person")])
    job_role_skills = models.TextField(max_length=50)
    job_role_posted = models.DateTimeField(default=datetime.datetime.now)
    job_role_deadline = models.DateTimeField()

    def __str__(self):
        return self.job_role_name
    
class Skills(models.Model):
    skill_name = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name

class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_id = models.AutoField(primary_key=True)
    user_email = models.EmailField(max_length=50, unique=True)
    user_pass = models.CharField(max_length=20)
    user_resume = models.FileField(upload_to='resumes/')
    user_skills = models.CharField(max_length=100, default="")
    user_desc = models.TextField(max_length=255)
    user_education = models.TextField(max_length=255)

    def __str__(self):
        return self.user_name