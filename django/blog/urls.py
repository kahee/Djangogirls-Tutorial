from django.urls import path
# .은 현재 패키지 (상대경로) from blog import views (절대경로)
# 절대 경로는 추천하지 않음
from . import views

urlpatterns = [
    #
    path('', views.post_list),
    path('detail/', views.post_detail)

]
