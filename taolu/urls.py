from django.urls import path
from . import views

urlpatterns = [
    path('', views.taolu, name='taolu'),
    #path('search', views.Search.as_view(), name='search'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.TaoluDetailView.as_view(), name='taoludetail'),
    path('<int:pk>/update>', views.TaoluUpdateView.as_view(), name='taoluupdate'),
    path('<int:pk>/delete>', views.TaoluDeleteView.as_view(), name='taoludelete'),
    path('search', views.SearchResultsView.as_view(), name='search_results_taolu'),
]
handler404 = "taolu.views.page_not_found_view"