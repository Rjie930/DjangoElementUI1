from django.contrib import admin

# Register your models here.
admin.site.site_header = '活动管理后台'  # 设置header
admin.site.site_title = '活动管理后台'   # 设置title
admin.site.index_title = '活动管理后台'

from .models import Task
admin.site.register(Task)

