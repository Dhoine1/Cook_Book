import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from urllib.parse import urljoin
from datetime import datetime


class CkeditorCustomStorage(FileSystemStorage):
    def get_folder_name(self):
        return datetime.now().strftime('%Y/%m/%d')

    def _save(self, name, content):
        folder_name = self.get_folder_name()
        name = os.path.join(folder_name, name)
        return super()._save(name, content)

    location = os.path.join(settings.MEDIA_ROOT, 'uploads/')
    base_url = urljoin(settings.MEDIA_URL, 'uploads/')
