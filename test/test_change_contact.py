from model.contact import Contact


def test_change_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact(firstname="Nick", mobile="1313131313"))
    app.session.logout()