from django.urls import path

from .views import (
    ChatAPIView,
    ConversationCreateAPIView,
    ConversationListAPIView,
    ConversationDetailAPIView,
    ConversationDeleteAPIView,
)


urlpatterns = [

    path(
        "",
        ChatAPIView.as_view(),
        name="chat"
    ),
    path(
        "conversations/",
        ConversationListAPIView.as_view(),
    ),

    path(
        "conversation/create/",
        ConversationCreateAPIView.as_view(),
    ),
    path(
        "conversations/<uuid:pk>/",
        ConversationDetailAPIView.as_view(),
    ),
    path(
        "conversation/<uuid:pk>/delete/",
        ConversationDeleteAPIView.as_view(),
        name="delete-conversation",
    ),

]