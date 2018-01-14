from model.contact import Contact


def test__modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Tom"))
    app.session.logout()


def test__modify_contact_mobile(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(mobile="1110001100"))
    app.session.logout()