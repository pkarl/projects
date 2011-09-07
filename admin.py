from django.contrib import admin
from models import Company, Project, Client, Resource, Assignment

class CompanyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Company, CompanyAdmin)

class ProjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Project, ProjectAdmin)

class ClientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Client, ClientAdmin)

class ResourceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Resource, ResourceAdmin)

class AssignmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Assignment, AssignmentAdmin)