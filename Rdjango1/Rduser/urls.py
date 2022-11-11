
from Rduser import views 
from django.contrib import admin
from django.urls import path,include               
from rest_framework import routers  


router = routers.SimpleRouter()                   
router.register(r'todos', views.TodoView, 'todo')  
 
urlpatterns = [
     path('api/', include(router.urls) ),
       path('hello_world/', views.hello_world ),
              path('register/', views.pos.as_view()),
               path('update/<str:namee>', views.UserEdit.as_view()),
               path('admin_api/', views.admin_api),
               path('demo/', views.jwtCheck.as_view()),
                # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
                path('usser/', views.UserView.as_view()),
    path('logout/',views.LogoutView.as_view()),

                 path('delete_api/<str:name>', views.DeleteUser.as_view()),
                     path('search/<str:name>', views.searchh),
    #                   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
         

   
]