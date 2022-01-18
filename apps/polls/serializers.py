from rest_framework import serializers

from .models import Poll, Question, Vote, Variant, Report
from apps.auth.serializers import UserSerializer


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data):
        question = Question.objects.create(**validated_data)
        return question


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        # fields = '__all__'
        fields = ('id', 'poll', 'text', 'question', 'variant')

    def create(self, validated_data):
        user = self.context['request'].user
        vote = Vote.objects.create(user=user, **validated_data)
        report = Report.objects.create(user=user, poll=validated_data['poll'])
        return vote


class ReportSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer
    user = UserSerializer

    class Meta:
        model = Poll
        fields = ('user', 'questions', 'poll')
