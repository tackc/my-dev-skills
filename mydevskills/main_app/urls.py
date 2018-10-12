from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    # skills paths
    path('skills/', views.SkillList.as_view(), name='skills'),
    path('skills/<int:skill_id>/', views.skills_detail, name='skills_detail'),
    path('skills/create/', views.SkillCreate.as_view(), name='skills_create'),
    path('skills/<int:pk>/update', views.SkillUpdate.as_view(), name='skills_update'),
    path('skills/<int:pk>/delete', views.SkillDelete.as_view(), name='skills_delete'),
    
    # path('user/<username>/', views.profile, name='profile'),
    # path('profile/', views.profile, name='profile'),
]