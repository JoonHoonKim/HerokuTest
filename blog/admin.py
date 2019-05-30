from django.contrib import admin
from .models import Blog #같은 폴더 안에 있는 models 파일에 블로그 클래스를 불러와라
from .models import Image
# Register your models here.
admin.site.register(Blog)#admin사이트에 보여줘
admin.site.register(Image)#admin사이트에 보여줘