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
            password="V3ry_l0ng_p4Ssword",
        )
        user.save()

    @staticmethod
    def test_valid_data() -> None:
        form = RegistrationForm(
            data={
                "username": "not_exist",
                "email": "not_exist@example.com",
                "password": "V3ry_l0ng_p4Ssword",
                "password_confirm": "V3ry_l0ng_p4Ssword",
            },
        )
        assert form.is_valid()

    @staticmethod
    def test_password_mismatch() -> None:
        form = RegistrationForm(
            data={
                "username": "not_exist",
                "email": "not_exist@example.com",
                "password": "V3ry_l0ng_p4Ssword",
                "password_confirm": "not_V3ry_l0ng_p4Ssword",
            },
        )
        assert not form.is_valid()
        assert isinstance(form.errors, ErrorDict)
        assert "password_confirm" in form.errors

    @staticmethod
    def test_password_without_digit() -> None:
        form = RegistrationForm(
            data={
                "username": "not_exist",
                "email": "not_exist@example.com",
                "password": "Very_long_paSsword",
                "password_confirm": "Very_long_paSsword",
            },
        )
        assert not form.is_valid()
        assert isinstance(form.errors, ErrorDict)
        assert "password" in form.errors

    @staticmethod
    def test_password_without_lower() -> None:
        form = RegistrationForm(
            data={
                "username": "not_exist",
                "email": "not_exist@example.com",
                "password": "AAAA1337AAAA1337",
                "password_confirm": "AAAA1337AAAA1337",
            },
        )
        assert not form.is_valid()
        assert isinstance(form.errors, ErrorDict)
        assert "password" in form.errors

    @staticmethod
    def test_password_without_upper() -> None:
        form = RegistrationForm(
            data={
                "username": "not_exist",
                "email": "not_exist@example.com",
                "password": "aaaa1337aaaa1337",
                "password_confirm": "aaaa1337aaaa1337",
            },
        )
        assert not form.is_valid()
        assert isinstance(form.errors, ErrorDict)
        assert "password" in form.errors

    @staticmethod
    def test_username_not_unique() -> None:
        form = RegistrationForm(
            data={
                "username": "exist",
                "email": "not_exist@example.com",
                "password": "V3ry_l0ng_p4Ssword",
                "password_confirm": "V3ry_l0ng_p4Ssword",
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
                "password": "V3ry_l0ng_p4Ssword",
                "password_confirm": "V3ry_l0ng_p4Ssword",
            },
        )
        assert not form.is_valid()
        assert isinstance(form.errors, ErrorDict)
        assert "email" in form.errors
