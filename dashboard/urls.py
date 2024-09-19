from django.urls import path
from dashboard.views import *
urlpatterns=[
    path('',home,name='home'),
    path('notes/',notes,name='notes'),
    path('delete_notes/<int:pk>/', Delete_Notes, name='delete_notes'),
    path('notes_detail/<int:pk>/',NotesDetailView.as_view(),name='notes_detail'),
   # path('accounts/', include('django.contrib.auth.urls')),
   path('homework/',homework,name="homework"),
   path('update_homework/<int:pk>/',update_homework,name='update_homework'),
   path('delete_homework/<int:pk>/', Delete_Homework, name='Delete_Homework'),
   path('youtube/',youtube,name='youtube'),
   path('todo/',To_do,name='Todo'),
   path('update_todo/<int:pk>/',update_todo,name='update_todo'),
   path('delete_todo/<int:pk>/', delete_todo, name='Delete_Todo'),
]

