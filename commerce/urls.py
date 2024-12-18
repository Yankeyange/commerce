"""commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from auctions.views import CreateListing, Watchlist, Categories,details

urlpatterns = [
    path("admin/", admin.site.urls),
    # pour créer une nouvelle vente
    path("CreateListing",CreateListing, name="CreateListing"),
    # pour regarder toute les ventes actuelles
    path("Watchlist",Watchlist, name="Watchlist"),
    # les différentes catégories
    path("Categories",Categories, name="Categories"),
    # les détails de chaque ventes
    path("<int:details_id>/" , details, name="details"),
    # page pour ajouter des détails de chaque page
    #path("new_details/<int:rep>/", new_details, name="new_details"),
    path("", include("auctions.urls"))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)