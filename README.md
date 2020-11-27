# django-editorjs

[![GitHub version](https://badge.fury.io/gh/VLZH%2Fdjango-editorjs.svg)](https://badge.fury.io/gh/VLZH%2Fdjango-editorjs)
[![PyPi downloads](https://img.shields.io/pypi/dm/django-editorjs)](https://pypi.org/project/django-editorjs/)

Plugin for using [Editor.js](https://editorjs.io/) in django admin.

- [Supported tools](#supported-tools)
- [Installation](#installation)
- [Simple example](#simple-example)
- [Configuration](#configuration)
  - [Base configuration](#base-configuration)
  - [How to configure fields and tools](#how-to-configure-fields)
- [API](#api)
- [How to run demo](#how-to-run-demo)

# Supported tools

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

# Installation

1. First step is install plugin.
   ```bash
   pip install django-editorjs
   ```
2. Add plugin to INSTALLED_APPS in Django settings file.
   ```python
   # settings.py
   INSTALLED_APPS = [
       # some other apps
       'django_editorjs'
   ]
   ```
3. Register plugin's endpoints in in `urlpatterns`
   ```python
   # urls.py
   from django_editorjs.urls import urlpatterns
   urlpatterns = [
       # other urls
       *urlpatterns
   ]
   ```

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

# Configuration

## Base configuration

This plugin provides additional functionality for saving images and files + allow to get information about some link.
You can to configure some options in your `settings.py` file.

- `EDITORJS_IMAGES_FOLDER` - Default folder for keep images uploaded through EditorJs (_Default: `{MEDIA_ROOT}/editorjs`_)
- `EDITORJS_FILES_FOLDER` - Default folder for keep files uploaded through EditorJs (_Default: `{MEDIA_ROOT}/editorjs`_)

## How to configure fields

> #### ⚠️ Note (for plugin configuration)
>
> Usually in examples for Editor.js you will see tool names starts with lowercase, but for bypass potential conflicts i name tools with capital letters.

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

#### Config schema

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

# API

- `EditorJsField`

  Extends `TextField` and use `EditorJsWidget` as widget + have additional argument in constructor: `editorjs_config`.

- `EditorJsWidget`

  Widget that you can to use for using Editor.js in Django.

## Custom `ImageSaver`

`ImageSaver` is class for saving images on disk. You can to create custom saver. Custom saver must implement this interface:

```python
class ImageSaver:
  save(file: File) -> ImageSaveResult
```

after creating class you can to change option `EDITORJS_IMAGES_SAVER` in settings to somethink like:

```python
# settings.py
EDITORJS_IMAGES_SAVER = "your_app.your_module.YourImageSaverClass"
```

## Custom `FileSaver`

Similary to `ImageSaver` you can to create custom `FileSaver` class with this interface:

```python
class FileSaver:
  save(file: File) -> FileSaveResult
```

# How to run demo

```bash
poetry install
poetry run python ./demo/manage.py migrate
poetry run python ./demo/manage.py createsuperuser
poetry run python ./demo/manage.py runserver
```

# TODO

- load tool on demand
- more examples in README.md
- view-function for file uploading
- view-function for image uploading
- view-function for link info crawler
