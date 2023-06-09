from django.urls import path

from onepiece import views

app_name = "onepiece"
urlpatterns = [
    path("<int:character_id>/", views.characterView, name="characterView"),
    path("detail/<int:character_id>/",views.detail,name="detail"),
    path('characters/',views.CharacterList.as_view(),name='character_list'),
]
