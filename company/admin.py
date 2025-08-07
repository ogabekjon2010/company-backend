from django.contrib import admin
from .models import Blog,Project,Company,TeamMember

admin.site.register(Blog)
admin.site.register(Project)
admin.site.register(Company)
admin.site.register(TeamMember)