from model.group import Group


def test_change_group(app):
    app.session.login(username="admin", password="secret")
    app.group.change(Group(name="test", header="group", footer="change"))
    app.session.logout()