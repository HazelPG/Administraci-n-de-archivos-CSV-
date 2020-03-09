from django.contrib import admin
from .models import *
# Register your models here.

class Files (admin.ModelAdmin):

        list_display = ['id_file','file_name','file_data','created_at','updated_at','deleted_at']
        list_filter = ['id_file','file_name']
        search_fields = ('id_file','file_name')
        class Meta:
		          model = File


admin.site.register(File,Files)