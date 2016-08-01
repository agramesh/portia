from django.apps import AppConfig
from django.conf import settings


class StorageConfig(AppConfig):
    name = 'storage'

    def ready(self):
        if settings.PORTIA_STORAGE_BACKEND == 'storage.storage.GitStorage':
            from .repoman import Repoman
            Repoman.setup(getattr(settings, 'GITSTORAGE_REPO_BACKEND',
                                  'dulwich.repo.Repo'))
