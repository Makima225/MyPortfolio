from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to= 'project_images/', blank=True)

    def  __str__(self):
        return self.name
    

class Experience(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    enterprise = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    

class Education(models.Model):
    level = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    school = models.CharField(max_length=100)

    def __str__(self):
        return self.level    
    

class Skill(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Language(models.Model):
    title = models.CharField(max_length=100)   

    def __str__(self):
        return self.title
    


class UserContact(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name+" "+self.email 
    

class Framework(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name   
    

class MyProfil(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to= 'my_profile_images/', blank=True)
     
    def __str__(self):
        return self.first_name  

