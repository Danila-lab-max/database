from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.main, name='main'),
                  path('home', views.home, name='home'),
                  path('create_soch', views.create, name='create_soch'),
                  path('regist_teacher', views.regist_teacher, name='reg_teacher'),
                  path('regist_student', views.regist_student, name='reg_student'),
                  path('entrance', views.entrance, name='entrance'),
                  path('create_comment', views.create_comment, name='create_comment'),
                  path('<int:pk>', views.SochDetailView.as_view(), name='soch_detail')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
