# django-editorjs

[![GitHub version](https://badge.fury.io/gh/VLZH%2Fdjango-editorjs.svg)](https://badge.fury.io/gh/VLZH%2Fdjango-editorjs)
[![PyPi downloads](https://img.shields.io/pypi/dm/django-editorjs)](https://pypi.org/project/django-editorjs/)

Plugin for using [Editor.js](https://editorjs.io/) in django admin.

# Supported plugins/tools

- `@editorjs/paragraph` - [![npm version](https://badge.fury.io/js/%40editorjs%2Fparagraph.svg)](https://badge.fury.io/js/%40editorjs%2Fparagraph)
- `@editorjs/image` - [![npm version](https://badge.fury.io/js/%40editorjs%2Fimage.svg)](https://badge.fury.io/js/%40editorjs%2Fimage)
- `@editorjs/header` - [![npm version](https://badge.fury.io/js/%40editorjs%2Fheader.svg)](https://badge.fury.io/js/%40editorjs%2Fheader)
- `@editorjs/checklist` - [![npm version](https://badge.fury.io/js/%40editorjs%2Fchecklist.svg)](https://badge.fury.io/js/%40editorjs%2Fchecklist)
- `@editorjs/list` - [![npm version](https://badge.fury.io/js/%40editorjs%2Flist.svg)](https://badge.fury.io/js/%40editorjs%2Flist)
- `@editorjs/quote` - [![npm version](https://badge.fury.io/js/%40editorjs%2Fquote.svg)](https://badge.fury.io/js/%40editorjs%2Fquote)
- `@editorjs/raw` - [![npm version](https://badge.fury.io/js/%40editorjs%2Fraw.svg)](https://badge.fury.io/js/%40editorjs%2Fraw)
- `@editorjs/embed` - [![npm version](https://badge.fury.io/js/%40editorjs%2Fembed.svg)](https://badge.fury.io/js/%40editorjs%2Fembed)
- `@editorjs/delimiter` - [![npm version](https://badge.fury.io/js/%40editorjs%2Fdelimiter.svg)](https://badge.fury.io/js/%40editorjs%2Fdelimiter)
- `@editorjs/warning` - [![npm version](https://badge.fury.io/js/%40editorjs%2Fwarning.svg)](https://badge.fury.io/js/%40editorjs%2Fwarning)
- `@editorjs/link` - [![npm version](https://badge.fury.io/js/%40editorjs%2Flink.svg)](https://badge.fury.io/js/%40editorjs%2Flink)
- `@editorjs/marker` - [![npm version](https://badge.fury.io/js/%40editorjs%2Fmarker.svg)](https://badge.fury.io/js/%40editorjs%2Fmarker)
- `@editorjs/attaches` - [![npm version](https://badge.fury.io/js/%40editorjs%2Fattaches.svg)](https://badge.fury.io/js/%40editorjs%2Fattaches)
- `@editorjs/table` - [![npm version](https://badge.fury.io/js/%40editorjs%2Ftable.svg)](https://badge.fury.io/js/%40editorjs%2Ftable)

> #### ⚠️ Note (for plugin configuration)
>
> Usually in examples for Editor.js you will see tool names starts with lowercase, but for bypass potential conflicts i use uppercase.

# Installation

```bash
pip install django-editorjs
```

Add django_editorjs to your INSTALLED_APPS setting.

# Simple example

```python
# models.py
from django.db import models
from django_editorjs import EditorJsField

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = EditorJsField()

    def __str__(self):
        return self.title
```

# How to configure

You can provide field specific configuration options to `EditorJsField` by argument `editorjs_config`.

#### Example

```python
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

```

## Config schema

- `tools`
  - `Image` - (`dict`) configuration for tool `ImageTool`. (_For more info see official documentation for tool_).
  - `Header` - (`dict`) configuration for tool `Header`. (_For more info see official documentation for tool_).
  - `Checklist` - (`dict`) configuration for tool `Checklist`. (_For more info see official documentation for tool_).
  - `List` - (`dict`) configuration for tool `List`. (_For more info see official documentation for tool_).
  - `Quote` - (`dict`) configuration for tool `Quote`. (_For more info see official documentation for tool_).
  - `Raw` - (`dict`) configuration for tool `RawTool`. (_For more info see official documentation for tool_).
  - `Embed` - (`dict`) configuration for tool `Embed`. (_For more info see official documentation for tool_).
  - `Delimiter` - (`dict`) configuration for tool `Delimiter`. (_For more info see official documentation for tool_).
  - `Warning` - (`dict`) configuration for tool `Warning`. (_For more info see official documentation for tool_).
  - `Link` - (`dict`) configuration for tool `LinkTool`. (_For more info see official documentation for tool_).
  - `Marker` - (`dict`) configuration for tool `Marker`. (_For more info see official documentation for tool_).
  - `Attaches` - (`dict`) configuration for tool `AttachesTool`. (_For more info see official documentation for tool_).
  - `Table` - (`dict`) configuration for tool `Table`. (_For more info see official documentation for tool_).

## For file upload

1. Add `EditorjsImageUploaderView` view to your project's `urls.py` file:

```python
from django_editorjs.views import EditorjsImageUploader

...

urlpatterns += [
    path("editorjs/image/", EditorjsImageUploaderView.as_view())
]
```

2. Setting Configurations `settings.py`
   
```python
# EditorjsImageUploaderView absolute url
EDITORJS_UPLOAD_IMAGE_URL = "/editorjs/image/"

# Relative path to your editorjs media upload directory
EDITORJS_UPLOAD_IMAGE_PATH = "editorjs/images/"

# Images types that available for upload
EDITORJS_IMAGE_TYPES = (
    "image/png",
    "image/jpg",
    "image/jpeg",
    "image/pjpeg",
    "image/gif",
)

# Maximum Upload Image
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
EDITORJS_MAX_IMAGE_UPLOAD_SIZE = 1024 * 1024  # Default 10MB
```

# API

- `EditorJsField`

  Extends `TextField` and use `EditorJsWidget` as widget + have additional argument in constructor: `editorjs_config`.

- `EditorJsWidget`

  Widget that you can to use for using Editor.js in Django.

# TODO

- load tool on demand
- more examples in README.md
- view-function for file uploading
- view-function for link info crawler
