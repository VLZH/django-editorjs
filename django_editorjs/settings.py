import os

from django.conf import settings

EDITORJS_IMAGES_SAVER = "django_editorjs.image_saver.ImageSaver"
EDITORJS_FILES_SAVER = "django_editorjs.file_saver.FileSaver"

EDITORJS_IMAGES_DIR = getattr(
    settings,
    "EDITORJS_IMAGES_DIR",
    os.path.join(getattr(settings, "MEDIA_ROOT"), "editorjs"),
)

EDITORJS_IMAGES_URL = getattr(
    settings,
    "EDITORJS_IMAGES_URL",
    os.path.join(getattr(settings, "MEDIA_URL"), "editorjs"),
)

EDITORJS_FILES_DIR = getattr(
    settings,
    "EDITORJS_FILES_DIR",
    os.path.join(getattr(settings, "MEDIA_ROOT"), "editorjs"),
)


EDITORJS_FILES_URL = getattr(
    settings,
    "EDITORJS_FILES_URL",
    os.path.join(getattr(settings, "MEDIA_URL"), "editorjs"),
)
