# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test group", header="test", footer="create a test group"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

