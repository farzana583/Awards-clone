from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns=[  
     path('',views.home,name = 'home'),
     path('registration/login/',views.loginPage, name="login"),
     path('registration/registration_form.html/',views.registerPage, name="register"),
     path('logout/',views.logoutUser, name="logout"),
     path('accounts/profile/', views.profile, name = 'profile'),
     path('rate/<int:id>/',views.rate,name='rates'),
     url(r'^singleproject/(\d+)',views.single_project,name='singleproject'),
     path('postImage/', views.new_post, name = 'post_image'),

     
     
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)