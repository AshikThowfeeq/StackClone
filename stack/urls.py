from django.urls import path
from stack import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("signup/",views.SignUpView.as_view(),name="register"),
    path("",views.SignInView.as_view(),name="signin"),
    path("home/",views.IndexView.as_view(),name="home"),
    path("questions/<int:id>/answers/add",views.AddAnswerView.as_view(),name="add-answer"),
    path("answers/<int:id>/upvote/add",views.UpvoteView.as_view(),name="upvote"),
    path("profile/create",views.UserProfileCreateView.as_view(),name="profile-add"),
    path("profile/view",views.ProfileDetailView.as_view(),name="profile-view"),
    path("profile/<int:id>/update",views.ProfileUpdateView.as_view(),name="profile-update"),
    path("questions/<int:id>/remove",views.QuestionDeleteView.as_view(),name="question-delete"),
    path("answers/<int:id>/upvote/remove",views.UpvoteRemoveView.as_view(),name="upvote-remove"),
    path("logout",views.SignoutView,name="signout"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)