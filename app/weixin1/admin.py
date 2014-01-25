from django.contrib import admin
from app.yijian.models import Yijian

class YijianAdmin(admin.ModelAdmin):
    list_display = ('id', 'brief', 'content')

admin.site.register(Yijian,YijianAdmin)