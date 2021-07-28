from django.urls import path

from .views import StoriesListView, StoryDetailsView

urlpatterns = [
    path('', StoriesListView.as_view(), name='stories_api'),
    path('<int:pk>', StoryDetailsView.as_view(), name='story_details_api'),
]
