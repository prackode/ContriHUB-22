from django import forms
from .models import Issue, PullRequest


class PRSubmissionForm(forms.ModelForm):

    class Meta:
        model = PullRequest
        fields = ('pr_link',)


class PRJudgeForm(forms.ModelForm):

    class Meta:
        model = PullRequest
        fields = ('bonus', 'penalty', 'remark',)


class CreateIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'description', 'mentor', 'project', 'level', 'points', 'is_restricted')
