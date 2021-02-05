import os
import json
import uuid

from django.conf import settings
from django.views import View
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from .app_settings import (
    IMAGE_AVAILABLE_TYPES,
    MAX_IMAGE_UPLOAD_SIZE,
    UPLOAD_IMAGE_PATH,
)


class EditorjsImageUploaderView(View):
    def post(self, request, *args, **kwargs):
        if "image" in request.FILES:
            image = request.FILES["image"]
            if image.content_type not in IMAGE_AVAILABLE_TYPES:
                data = json.dumps({"success": 0, "error": "Bad image format."})
                return HttpResponse(data, content_type="application/json", status=405)
            if image.size > MAX_IMAGE_UPLOAD_SIZE:
                to_MB = MAX_IMAGE_UPLOAD_SIZE / (1024 * 1024)
                data = json.dumps(
                    {
                        "success": 0,
                        "error": "Maximum image file is %(size)s MB." % {"size": to_MB},
                    },
                )
                return HttpResponse(data, content_type="application/json", status=405)

            img_uuid = "{0}-{1}".format(
                uuid.uuid4().hex[:10], image.name.replace(" ", "-")
            )
            tmp_file = os.path.join(UPLOAD_IMAGE_PATH, img_uuid)
            def_path = default_storage.save(tmp_file, ContentFile(image.read()))
            img_url = os.path.join(settings.MEDIA_URL, def_path)

            data = json.dumps(
                {
                    "success": 1,
                    "file": {
                        "url": request.build_absolute_uri(img_url),
                        "name": image.name,
                        "size": image.size,
                        "content_type": image.content_type,
                    },
                }
            )
            return HttpResponse(data, content_type="application/json", status=201)

        data = json.dumps({"success": 0, "error": _("No 'image' in files")})
        return HttpResponse(data, content_type="application/json", status=400)
