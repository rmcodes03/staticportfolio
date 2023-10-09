from django.urls import path
import projects.views

urlpatterns = [
    path('<int:project_id>/', projects.views.projectdetails, name='projectdetails')
]