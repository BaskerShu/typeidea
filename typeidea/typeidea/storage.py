# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.conf import settings
from django.utils.six import StringIO
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image, ImageDraw, ImageFont


class MyFileSystemStorage(FileSystemStorage):
    def save(self, name, content, max_length=None):
        if 'image' in content.content_type:
            image = self.watermark_with_text(content, 'test', 'red')
            content = self.convert_image_to_file(name, image)

        return super(FileSystemStorage, self).save(name, content, max_length)

    def convert_image_to_file(self, name, image):
        temp = StringIO()
        image.save(temp, format='PNG')
        return InMemoryUploadedFile(temp, None, name, 'image/png', temp.len, None)

    def watermark_with_text(self, file_obj, text, color, font='/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf'):
        image = Image.open(file_obj).convert('RGBA')
        watermark_image = Image.new('RGBA', image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(watermark_image)
        width, height = image.size
        margin = 10
        font = ImageFont.truetype(font, height / 20)

        text_width, text_height = draw.textsize(text, font)
        x = width - text_width - margin
        y = height - text_height - margin
        draw.text((x, y), text, color, font=font)

        return Image.alpha_composite(image, watermark_image)


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
