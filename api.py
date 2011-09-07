from tastypie.resources import ModelResource
from models import Company, Project, Client, Resource, Assignment

class CompanyResource(ModelResource):
    class Meta:
        queryset = Company.objects.all()
        resource_name = 'company'

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'

class ClientResource(ModelResource):
    class Meta:
        queryset = Client.objects.all()
        resource_name = 'client'

class ResourceResource(ModelResource):
    class Meta:
        queryset = Resource.objects.all()
        resource_name = 'resource'

class AssignmentResource(ModelResource):
    class Meta:
        queryset = Assignment.objects.all()
        resource_name = 'assignment'
