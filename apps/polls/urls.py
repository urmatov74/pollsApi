from rest_framework import routers
from . import views

polls_router = routers.DefaultRouter()
question_router = routers.DefaultRouter()
polls_router.register(r'polls', views.PollsViewSet, basename='polls')
polls_router.register(r'questions', views.QuestionViewSet, basename='questions')
polls_router.register(r'variant', views.VariantViewSet, basename='variants')
polls_router.register(r'voting', views.VoteViewSet, basename='votes')
polls_router.register(r'reports', views.ReportViewSet, basename='reports')
