from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    ActorDetail,
    ActorList,
    CinemaHallViewSet,
    GenreDetail,
    GenreList,
    MovieViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinema_halls = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)
urlpatterns = [
    path(
        "genres/",
        GenreList.as_view(),
        name="genres",
    ),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail",
    ),
    path(
        "actors/",
        ActorList.as_view(),
        name="actors",
    ),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail",
    ),
    path(
        "cinema_halls/",
        cinema_halls,
        name="cinema_hall-list",
    ),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema_hall-detail",
    ),
    path("", include(router.urls)),
]

app_name = "cinema"
