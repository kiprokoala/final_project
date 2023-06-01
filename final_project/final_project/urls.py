"""
URL configuration for one_piece project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from crews import views
from django.conf import settings  # new
from django.conf.urls.static import static  # new

urlpatterns = [
    path('admin/', admin.site.urls),

    path('crews/', views.crews),
    path('crews/<int:crew_id>/', views.crew),
    path('crews/add/', views.formulaireCreationCrew),
    path('crews/create/', views.creerCrew),
    path('crews/<int:crew_id>/addIsland/', views.ajouterIslandAuCrew),
    path('crews/<int:crew_id>/delete/', views.supprimerCrew),
    path('crews/<int:crew_id>/update/', views.formulaireModificationCrew),
    path('crews/<int:crew_id>/updated/', views.modifierCrew),

    path('islands/', views.islands),
    path('islands/<int:island_id>/', views.island),
    path('islands/add/', views.formulaireCreationIsland),
    path('islands/create/', views.creerIsland),
    path('islands/<int:island_id>/delete/', views.supprimerIsland),
    path('islands/<int:island_id>/update/', views.formulaireModificationIsland),
    path('islands/<int:island_id>/updated/', views.modifierIsland),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)