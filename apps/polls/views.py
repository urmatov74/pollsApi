# Create your views here.
import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Poll, Question, Vote, Variant, Report
from .serializers import PollSerializer, QuestionSerializer, VoteSerializer, VariantSerializer


class PollsViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get_permissions(self):
        if self.action in ('active_polls', 'my_polls', 'retrieve'):
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['GET'])
    def poll_question(self, request, pk):
        poll = self.get_object()
        queryset = Question.objects.filter(poll=poll.id)
        serializer = QuestionSerializer(queryset, many=True)
        return Response(
            serializer.data
        )

    @action(detail=False, methods=['GET'])
    def my_polls(self, request):
        user = request.user
        polls = Poll.objects.filter(report_poll__user=user)
        serializer = PollSerializer(polls, many=True)
        return Response(
            serializer.data
        )

    # @action(detail=True, methods=['POST'], serializer_class=QuestionSerializer)
    # def add_question(self, request, pk):
    #     serializer = QuestionSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def active_polls(self, request):
        now = datetime.datetime.now()
        queryset = Poll.objects.filter(end_date__gte=now, start_date__lt=now)
        serializer = PollSerializer(queryset, many=True)
        return Response(serializer.data)


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAdminUser]

    # @action(detail=True, methods=['POST'], serializer_class=VariantSerializer)
    # def add_variant(self, request, pk):
    #     serializer = VariantSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)


class VariantViewSet(viewsets.ModelViewSet):
    serializer_class = VariantSerializer
    queryset = Variant.objects.all()

    def get_permissions(self):
        if self.action in ('vote', 'list'):
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['POST'], serializer_class=VoteSerializer, permission_classes=[IsAuthenticated])
    def vote(self, request, pk):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class VoteViewSet(viewsets.ModelViewSet):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = PollSerializer
    queryset = Poll.objects.filter()
    permission_classes = [IsAdminUser]
