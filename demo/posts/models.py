from django.db import models
from django_editorjs import EditorJsField


class Post(models.Model):
    title = models.TextField()
    body = EditorJsField(
        editorjs_config={
            "tools": {
                "Table": {
                    "disabled": False,
                    "inlineToolbar": True,
                    "config": {"rows": 2, "cols": 3,},
                }
            }
        }
    )
