from django.urls import path
from .views import save_image, save_file, get_link_info

urlpatterns = [
    path("editorjs/image/", save_image),
    path("editorjs/file/", save_file),
    path("editorjs/link/", get_link_info),
]
