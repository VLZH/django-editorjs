from django.conf import settings

UPLOAD_IMAGE_ENDPOINT = (
    getattr(settings, "EDITORJS_UPLOAD_IMAGE_URL", None) or "/editorjs/image/"
)
UPLOAD_IMAGE_PATH = (
    getattr(settings, "EDITORJS_UPLOAD_IMAGE_PATH", None) or "editorjs/images/"
)

IMAGE_AVAILABLE_TYPES = getattr(settings, "EDITORJS_IMAGE_TYPES", None) or (
    "image/png",
    "image/jpg",
    "image/jpeg",
    "image/pjpeg",
    "image/gif",
)

MAX_IMAGE_UPLOAD_SIZE = getattr(settings, "EDITORJS_MAX_IMAGE_UPLOAD_SIZE", None) or 1048576
