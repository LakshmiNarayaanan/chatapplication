from django.conf.urls import url,include


from . import views

urlpatterns = [
    url(r'^$', views.register, name='register'),
	url(r'^login/', views.login,name='login'),
	url(r'^success/', views.success,name='success'),
	url(r'^home/$', views.home,name='home'),
	url(r'^home/(.*)/$', views.chat,name='chat'),
	url(r'^check/', views.home,name='check'),




	# path('login/',views.login,name='login'),

]
