import os
from uuid import uuid4

from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndRename(object):

    def __init__(self, folder_path):
        self.path = folder_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{str(uuid4())}.{ext}'

        return os.path.join(self.path, filename)
