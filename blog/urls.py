from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog, name = "blog"),#url이 ''이면 blog 함수를 실행 시켜라. 이름은 blog다.
    path('detail/<int:blog_id>/', views.detail, name = "detail"),#나는 blog_id도 같이 받을꺼다.
    path('new/',views.new, name="new"),
    path('create/',views.create, name="create"),#함수 실행이 주 목적임
] 
