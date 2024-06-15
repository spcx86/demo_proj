from django.urls import path
from .views import HelloWorldView, callback
from .views import run_create_superuser


urlpatterns = [
    path('hello_world/', HelloWorldView.as_view(), name='hello_world'),
    path('callback/', callback, name='callback'),
    path('run-create-superuser/', run_create_superuser),

]
