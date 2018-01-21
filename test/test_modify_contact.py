from model.contact import Contact


def test__modify_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="Tom"))


def test__modify_contact_mobile(app):
    app.contact.modify_first_contact(Contact(mobile="55555555555"))
