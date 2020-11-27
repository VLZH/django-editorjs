import os
from os import path
from django.core.files import File
from django.core.files.storage import default_storage
from pydantic import BaseModel
from .settings import EDITORJS_FILES_DIR, EDITORJS_FILES_URL


class FileSaveResultFile(BaseModel):
    url: str
    size: int
    name: str
    extension: str


class FileSaveResult(BaseModel):
    success: int
    file: FileSaveResultFile


class FileSaver:
    destination: str

    def __init__(self, destination: str = EDITORJS_FILES_DIR) -> None:
        self.destination = destination

    def save(self, f: File) -> FileSaveResult:
        filepath = path.join(self.destination, f.name)
        created_filepath = default_storage.save(filepath, f)
        created_filename = path.basename(created_filepath)
        stat = os.stat(created_filepath)
        url = path.join(EDITORJS_FILES_URL, created_filename)
        (_, ext) = path.splitext(created_filepath)
        size = stat.st_size
        return FileSaveResult.parse_obj(
            {
                "success": 1,
                "file": {
                    "url": url,
                    "size": size,
                    "name": created_filename,
                    "extension": ext,
                },
            }
        )
