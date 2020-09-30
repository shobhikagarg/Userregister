from django.urls import path,include
#noinspection PyUnresolvedReferences
from .views import AccountViewset,UserLoginAPIView,ProfileAPI,Profilegenericview
from rest_framework.routers import DefaultRouter
#noinspection PyUnresolvedReferences

router=DefaultRouter()

router.register('account',AccountViewset,basename='account')
router.register('profile/', ProfileAPI, basename='profile')
urlpatterns = [
	#path('register/', AccountViewset.as_view()),
path('viewset/',include(router.urls)),                                 #http://127.0.0.1:8000/api/viewset/profile/profile//
    path('viewset/profile/',include(router.urls)),
    #path('generic/account/',Accountgenericview.as_view()),
    path('login/',UserLoginAPIView.as_view()),
    path('profilegeneric/<int:id>/',Profilegenericview.as_view()),
path('profilegeneric/',Profilegenericview.as_view()),

]