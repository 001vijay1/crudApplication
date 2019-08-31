from django.conf.urls import url
from .import views
urlpatterns = [
    url(r'^add/$',views.add_book ,name='add'),
    url(r'^show/$',views.show_book ,name='show'),
    url(r'^delete/(?P<book_id>\d+)/$',views.delete_book),
    url(r'^edit/(?P<book_id>\d+)/$',views.edit_record),
    url(r'^update/(?P<book_id>\d+)/$',views.update_record),
    url(r'^profile/(?P<book_id>\d+)/$',views.profile),
    url(r'^contact/$',views.contact,name='contact'),
]