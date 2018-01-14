# -*- coding: utf-8 -*-
from model.contact import Contact


def test__add_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Anton", mobile="656388735678"))
    app.session.logout()


def test__add_empty_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", mobile=""))
    app.session.logout()