# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application_C


@pytest.fixture
def app(request):
    fixture = Application_C()
    request.addfinalizer(fixture.destroy)
    return fixture


def test__add_contacts(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Anton", mobile_number="656388735678"))
    app.logout()


def test__add_empty_contacts(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", mobile_number=""))
    app.logout()