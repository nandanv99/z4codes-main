from django.db import models

# Create your models here.
class newcodes(models.Model):
    user_id = models.AutoField
    fullname = models.CharField(max_length=200)
    codefile = models.FileField(upload_to ='programs/')
    description = models.CharField(max_length=2000,default='')
    codeurl = models.URLField(max_length=2000,default='')

    
    def __str__(self) -> str:
        return self.fullname


class exp(models.Model):
    user_id = models.AutoField
    fullname = models.CharField(max_length=200)
    image = models.ImageField(upload_to ='expimg/')


    def __str__(self) -> str:
        return self.fullname

class user1(models.Model):
    name = models.AutoField
    passwor = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name

class files(models.Model):
    files_id=models.AutoField
    files_name=models.CharField(max_length=200)
    files=models.FileField(upload_to='file_pdf/')
    files_desc=models.CharField(max_length=200)
    collage=models.CharField(max_length=200,default='')
    sem=models.CharField(max_length=5,default='')
    year=models.CharField(max_length=5,default='')
    def __str__(self) -> str:
        return self.files_name