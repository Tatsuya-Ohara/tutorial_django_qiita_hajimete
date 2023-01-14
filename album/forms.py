from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    '''モデルの定義を利用してフォームを定義する'''
    class Meta:
        '''Imageクラスに対応: pictureとtitleを取得する'''
        model = Image
        fields = ['picture', 'title']