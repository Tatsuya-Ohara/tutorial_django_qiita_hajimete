from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

def showall(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'album/showall.html', context)

def upload(request):
    if request.method == "POST":
        # 画像を取り扱うのでリクエストファイルも渡す！
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # ImageFormではsaveメソッド未定義だが、form.ModelFormを継承しているので機能する。
            form.save()
            return redirect('album:showall')
    else:
        form = ImageForm()
    
    context = {'form': form}
    return render(request, 'album/upload.html', context)