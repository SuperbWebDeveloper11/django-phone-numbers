from django.urls import path
from . import views

app_name = 'phone'

urlpatterns = [
    # phone urls for crud operations
    path('phone/', views.PhoneList.as_view(), name='phone_list'),
    path('phone/add/', views.PhoneCreate.as_view(), name='phone_add'),
    path('phone/<int:pk>/detail/', views.PhoneDetail.as_view(), name='phone_detail'),
    path('phone/<int:pk>/update/', views.PhoneUpdate.as_view(), name='phone_update'),
    path('phone/<int:pk>/delete/', views.PhoneDelete.as_view(), name='phone_delete'),

    # datatable url
    path('phone/datatable/', views.PhoneDatatable.as_view(), name='phone_datatable'),
]
