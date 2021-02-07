from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    path('administration/', AdministrationListView.as_view(), name='administration_list'),
    path('administration/<int:pk>/', AdministrationDetailView.as_view(), name='administration_detail'),

    path('teacher/', TeacherListView.as_view(), name='teacher_list'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),

    path('our_prides/', OurPrideListView.as_view(), name='our_pride_list'),
    path('our_prides/<int:pk>/', OurPrideDetailView.as_view(), name='our_pride_detail'),

    path('honour/', HonourListView.as_view(), name='honour_list'),
    path('honour/<int:pk>/', HonourDetailView.as_view(), name='honour_detail'),

    path('about/', views.about, name='about'),
]
