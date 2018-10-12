from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('user/<username>/', views.profile, name='profile'),
    path('skills/', views.myskills, name='myskills'),
    path('skills/detail/', views.skills_detail, name='skills_detail'),
    path('skills/addskill/', views.SkillCreate.as_view, name='skills_create'),
    path('skills/addskill/<int:pk>/', views.SkillDelete.as_view, name='skills_create'),
    path('profile/', views.profile, name='profile'),
]