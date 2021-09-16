from django.urls import path

from .views import (EventsCreateView,
                    EventsDetailView,
                    EventsManageListView,
                    EventsUpdateView,
                    EventsUpcomingListView,

                    LocationManageListView,
                    LocationsCreateView,
                    LocationsDetailView,
                    LocationsUpdateView,)

app_name = "events"
urlpatterns = [
    path("", EventsUpcomingListView.as_view(), name="upcoming"),
    path("manage/", EventsManageListView.as_view(), name="manage"),
    path("create/", EventsCreateView.as_view(), name="create"),

    path("locations/", LocationManageListView.as_view(), name="locations"),
    path("locations/create/", LocationsCreateView.as_view(), name="location-create"),
    path("locations/<slug:slug>", LocationsDetailView.as_view(), name="location-detail"),
    path("locations/<slug:slug>/update/", LocationsUpdateView.as_view(), name="location-update"),

    path("<slug:slug>/", EventsDetailView.as_view(), name="detail"),
    path("<slug:slug>/update/", EventsUpdateView.as_view(), name="update"),
]
