# ruff: noqa: S101, S106
from typing import override

from django.forms.utils import ErrorDict
from django.test import TestCase

from fefu_lab.forms import RegistrationForm
from fefu_lab.models import User


class RegistrationFormTests(TestCase):
    @override
    def setUp(self) -> None:
        user = User(
            username="exist",
            email="exist@example.com",
            password="very_long_password",
        )
        user.save()

    @staticmethod
    def test_valid_data() -> None:
        form = RegistrationForm(
            data={
                "username": "not_exist",
                "email": "not_exist@example.com",
                "password": "very_long_password",
                "password_confirm": "very_long_password",
            },
        )
        assert form.is_valid()

    @staticmethod
    def test_password_mismatch() -> None:
        form = RegistrationForm(
            data={
                "username": "not_exist",
                "email": "not_exist@example.com",
                "password": "very_long_password",
                "password_confirm": "not_very_long_password",
            },
        )
        assert not form.is_valid()
        assert isinstance(form.errors, ErrorDict)
        assert "password_confirm" in form.errors

    @staticmethod
    def test_username_not_unique() -> None:
        form = RegistrationForm(
            data={
                "username": "exist",
                "email": "not_exist@example.com",
                "password": "very_long_password",
                "password_confirm": "very_long_password",
            },
        )
        assert not form.is_valid()
        assert isinstance(form.errors, ErrorDict)
        assert "username" in form.errors

    @staticmethod
    def test_email_not_unique() -> None:
        form = RegistrationForm(
            data={
                "username": "not_exist",
                "email": "exist@example.com",
                "password": "very_long_password",
                "password_confirm": "very_long_password",
            },
        )
        assert not form.is_valid()
        assert isinstance(form.errors, ErrorDict)
        assert "email" in form.errors
