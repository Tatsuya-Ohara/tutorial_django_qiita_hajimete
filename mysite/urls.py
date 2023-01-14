from django.contrib import admin
from django.urls import include, path
from django.views.generic import base
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('album/', include('album.urls')),
    path('admin/', admin.site.urls),
    # polls/loginにリダイレクトする
    path('accounts/login/', base.RedirectView.as_view(pattern_name="polls:login")),
    # polls/indexにリダイレクトする
    path('accounts/profile/', base.RedirectView.as_view(pattern_name="polls:index")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 開発用サーバーがMEDIA_URL起点でurlを共有できるようにするため