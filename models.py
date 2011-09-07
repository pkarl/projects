from django.db import models

class Company(models.Model):
  name = models.CharField(max_length=50)
  
  def __unicode__(self):
    return self.name
    
  class Meta:
    verbose_name_plural = "Companies"
    
class Client(models.Model):
  name = models.CharField(max_length=50)
  company = models.ForeignKey(Company)

  def __unicode__(self):
      return self.name

class Project(models.Model):
  name = models.CharField(max_length=50)
  client = models.ForeignKey(Client)
  company = models.ForeignKey(Company)

  def __unicode__(self):
      return self.name
      
class Resource(models.Model):
  name = models.CharField(max_length=50)
  company = models.ForeignKey(Company)

  def __unicode__(self):
      return self.name
            
class Assignment(models.Model):
  resource = models.ForeignKey(Resource)
  project = models.ForeignKey(Project)
  company = models.ForeignKey(Company)
  