from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields
from models import Company, Project, Client, Resource, Assignment

class CompanyResource(ModelResource):
    class Meta:
        queryset = Company.objects.all()
        resource_name = 'company'
        authorization= Authorization()

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
        authorization= Authorization()

class ClientResource(ModelResource):
    company = fields.ForeignKey(CompanyResource, 'company')
    class Meta:
        queryset = Client.objects.all()
        resource_name = 'client'
        authorization= Authorization()

class ResourceResource(ModelResource):
    class Meta:
        queryset = Resource.objects.all()
        resource_name = 'resource'
        authorization= Authorization()

class AssignmentResource(ModelResource):
    class Meta:
        queryset = Assignment.objects.all()
        resource_name = 'assignment'
        authorization= Authorization()
