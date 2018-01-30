import re

from django.urls import path, re_path
# .은 현재 패키지 (상대경로) from blog import views (절대경로)
# 절대 경로는 추천하지 않음
from . import views

urlpatterns = [
    #
    path('', views.post_list),
    # path('', views.post_detail)
    # 숫자가 1개이상 반복되는 경우를 정규표현식으로 구현하되
    # 해당 반복구간을 그룹으로 묶고, 그룹이름을 'pk'로 지정
    re_path(r'(?P<pk>\d+)/$', views.post_detail)

]
