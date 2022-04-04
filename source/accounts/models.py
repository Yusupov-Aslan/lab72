from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    def get_favorite_photos(self):
        return self.favorite_photos.all().values_list('photo', flat=True)

    def get_favorite_albums(self):
        return self.favorite_albums.all().values_list('album', flat=True)
