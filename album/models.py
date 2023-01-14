from django.db import models

class Image(models.Model):
    '''
    画像ファイル自体はディレクトリにアップロードされる。（実体がDataBaseに入るわけではない）
    '''
    # ImageFieldの使用にPillowのpip installが必要。相対パスはMEDIA_ROOTを起点としたもの。
    picture = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title