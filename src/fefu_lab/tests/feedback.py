# ruff: noqa: S101

from django.forms.utils import ErrorDict
from django.test import TestCase

from fefu_lab.forms import FeedbackForm


class FeedbackFormTests(TestCase):
    @staticmethod
    def test_valid_data() -> None:
        form = FeedbackForm(
            data={
                "name": "some_user",
                "email": "some_user@example.com",
                "subject": "some subject",
                "message": "some message",
            },
        )
        assert form.is_valid()

    @staticmethod
    def test_name_min_size_mismath() -> None:
        form = FeedbackForm(
            data={
                "name": "u",
                "email": "some_user@example.com",
                "subject": "some subject",
                "message": "some message",
            },
        )
        assert not form.is_valid()
        assert isinstance(form.errors, ErrorDict)
        assert "name" in form.errors

    @staticmethod
    def test_name_max_size_mismath() -> None:
        form = FeedbackForm(
            data={
                "name": "u" * 100,
                "email": "some_user@example.com",
                "subject": "some subject",
                "message": "some message",
            },
        )
        assert not form.is_valid()
        assert isinstance(form.errors, ErrorDict)
        assert "name" in form.errors

    @staticmethod
    def test_subject_max_size_mismath() -> None:
        form = FeedbackForm(
            data={
                "name": "some_user",
                "email": "some_user@example.com",
                "subject": "some subject" * 50,
                "message": "some message",
            },
        )
        assert not form.is_valid()
        assert isinstance(form.errors, ErrorDict)
        assert "subject" in form.errors

    @staticmethod
    def test_message_min_size_mismath() -> None:
        form = FeedbackForm(
            data={
                "name": "some_user",
                "email": "some_user@example.com",
                "subject": "some subject",
                "message": "msg",
            },
        )
        assert not form.is_valid()
        assert isinstance(form.errors, ErrorDict)
        assert "message" in form.errors
