from typing import Type
import logging
from django.utils.module_loading import import_string
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django_editorjs.image_saver import ImageSaver
from django_editorjs.file_saver import FileSaver
from .settings import EDITORJS_IMAGES_SAVER, EDITORJS_FILES_SAVER

logger = logging.getLogger(__name__)

@csrf_exempt
@require_http_methods(["POST"])
def save_image(request: HttpRequest):
    logger.debug("Start saving image")
    file = request.FILES.get("image")
    if not file:
        return HttpResponseBadRequest()
    ImageSaverCls: Type[ImageSaver] = import_string(EDITORJS_IMAGES_SAVER)
    saver = ImageSaverCls()
    result = saver.save(file)
    return JsonResponse(result.dict())


@csrf_exempt
@require_http_methods(["POST"])
def save_file(request: HttpRequest):
    logger.debug("Start saving file")
    file = request.FILES.get("file")
    if not file:
        return HttpResponseBadRequest()
    FileSaverCls: Type[FileSaver] = import_string(EDITORJS_FILES_SAVER)
    saver = FileSaverCls()
    result = saver.save(file)
    return JsonResponse(result.dict())


@csrf_exempt
@require_http_methods(["POST"])
def get_link_info(request: HttpRequest):
    logger.debug("Start getting information about link")
    return HttpResponse()
