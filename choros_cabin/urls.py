from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<str:username>/profile/', views.profile, name='profile'),
    path('newtrip/', views.new_trip, name='new_trip'),
    path('newlog/', views.new_log, name='new_log'),
    path('newprofile/', views.new_profile, name='new_profile'),
    path('edittrip/<int:trip_id>', views.edit_trip, name='edit_trip'),
    path('editlog/<int:log_id>', views.edit_log, name='edit_log'),
    path('editprofile/<int:profile_id>', views.edit_profile, name='edit_profile'),
    path('deletetrip/<int:trip_id>', views.delete_trip, name='delete_trip'),
    path('deletelog/<int:log_id>', views.delete_log, name='delete_log')
]
