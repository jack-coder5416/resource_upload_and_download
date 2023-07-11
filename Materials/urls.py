
from django.urls import path
from Materials.views import upload_material, material_list, download_material

urlpatterns = [
   
    path('', upload_material, name='upload_material'),
    path('Materials', material_list, name='material_list'),
    path('Materials/download/<int:material_id>/', download_material, name='download_material'),

]