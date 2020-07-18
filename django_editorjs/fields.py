from django.db.models import Field
from urllib.parse import unquote

from django_editorjs.widgets import EditorJsWidget


class EditorJsField(Field):
    def __init__(self, editorjs_config=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._editorjs_config = editorjs_config

    def get_internal_type(self):
        return "TextField"

    def clean(self, value, model_instance):
        if value is not None:
            return unquote(super().clean(value, model_instance))
        else:
            return None

    def formfield(self, *args, **kwargs):
        kwargs["widget"] = EditorJsWidget(editorjs_config=self._editorjs_config)
        return super().formfield(*args, **kwargs)
