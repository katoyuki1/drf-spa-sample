from django.contrib import admin # Djangoの管理サイト機能を利用するためのモジュールをインポート
from django.urls import path, include # URLパスを定義するためのpath関数と、他のURLconfを参照するためのinclude関数をインポート
from rest_framework.routers import DefaultRouter # DRFから、デフォルトのルータークラスDefaultRouterをインポート。ViewSetとURLの自動マッピングを可能にする
from api.views import ItemViewSet # api/views.pyからItemViewSetクラスをインポート

# DefaultRouterのインスタンスを作成
router = DefaultRouter()
# ItemViewSetをitemsパスでルーターに登録している。これにより、ItemViewSetに定義された操作に基づいて、自動的にURLが生成される
router.register(r'items', ItemViewSet)

# Djangoプロジェクト全体のURLパターンを定義するリスト
urlpatterns = [
    # Djangoの管理サイトへのURLパスを定義
    path('admin/', admin.site.urls),
    # routerで生成されたすべてのURLを/api/パス以下に含めるように定義。
    # これにより、ItemViewSetの操作に対応するURLが/api/items/のようにアクセスできるようにする
    path('api/', include(router.urls)),
]
