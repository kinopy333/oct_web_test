from django.urls import path, include
from .views import listview, rel, showvideo, review_input, review_process, rev_list, rev_new
from .views import signupview, loginview, logoutview, review_edit, review_update, review_delete, rev_list2

app_name = 'video'
urlpatterns = [
    path('', listview, name='list'),
    path('show/', showvideo, name='show'), 
    path('rev_input/<int:id>/', review_input, name='rev_input'),
    path('rev_edit/<int:id>/', review_edit, name='rev_edit'),
    path('rev_update/<int:id>/', review_update, name='rev_update'),
    path('rev_delete/<int:id>/', review_delete, name='rev_delete'),
    path('rev_new/', rev_new, name='rev_new'),
    path('rev_list/<int:id>',rev_list, name='rev_list'),
    path('rev_list/',rev_list2, name='rev_list2'),
    path('rev_process<int:id>/', review_process, name='rev_process'),
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('video/<int:id>', rel, name='review')
]