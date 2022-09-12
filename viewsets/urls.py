from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

#create router object
router=DefaultRouter()

#register  viewset with router
router.register('studentapi/',views.studentcrudapi)


urlpatterns=[
    path('',include(router.urls))
]