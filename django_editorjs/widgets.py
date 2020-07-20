import json
from django.forms import widgets, Media
from django.template.loader import render_to_string


class EditorJsWidget(widgets.Textarea):
    def __init__(self, editorjs_config, *args, **kwargs):
        super(EditorJsWidget, self).__init__(*args, **kwargs)
        self._editorjs_config = editorjs_config

    @property
    def media(self):
        return Media(
            css={"all": ["django-editorjs.css"]},
            js=(
                "https://cdn.jsdelivr.net/combine/npm/@editorjs/editorjs@2.18.0,npm/@editorjs/paragraph@2.7.0,npm/@editorjs/image@2.4.2,npm/@editorjs/header@2.5.0,npm/@editorjs/list@1.5.0,npm/@editorjs/checklist@1.1.0,npm/@editorjs/quote@2.3.0,npm/@editorjs/raw@2.1.2,npm/@editorjs/embed@2.3.1,npm/@editorjs/delimiter@1.1.0,npm/@editorjs/warning@1.1.1,npm/@editorjs/link@2.2.1,npm/@editorjs/marker@1.2.2,npm/@editorjs/attaches@1.0.1,npm/@editorjs/table@1.2.2",
                "django-editorjs.js",
            ),
        )

    def render(self, name, value, **kwargs):
        ctx = {
            "name": name,
            "id": kwargs["attrs"]["id"],
            "value": value,
            "editorjs_config": json.dumps(self._editorjs_config),
        }
        return render_to_string("editorjs.html", ctx)
