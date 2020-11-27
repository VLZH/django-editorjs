from os import path
from hashlib import md5
from django.core.files import File
from django.core.files.storage import default_storage
from pydantic import BaseModel
from .settings import EDITORJS_IMAGES_DIR, EDITORJS_IMAGES_URL


class ImageSaveResultFile(BaseModel):
    url: str


class ImageSaveResult(BaseModel):
    success: int
    file: ImageSaveResultFile


class ImageSaver:
    destination: str

    def __init__(self, destination: str = EDITORJS_IMAGES_DIR) -> None:
        self.destination = destination

    def _get_hash(self, f: File) -> str:
        """
        For hiding original name of image and bypassing duplicating
        we generate new name using md5 hash function.
        """
        hash = md5()
        while chunk := f.read(1000):
            hash.update(chunk)
        return hash.hexdigest()

    def save(self, f: File) -> ImageSaveResult:
        filename = self._get_hash(f)
        f.seek(0)
        _, ext = path.splitext(f.name)
        filepath = path.join(self.destination, f"{filename}{ext}")
        created_filepath = default_storage.save(filepath, f)
        created_filename = path.basename(created_filepath)
        url = path.join(EDITORJS_IMAGES_URL, created_filename)
        return ImageSaveResult.parse_obj({"success": 1, "file": {"url": url}})
