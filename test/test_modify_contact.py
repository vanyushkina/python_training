from model.contact import Contact


def test__modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Mari", mobile="777777777"))
    app.contact.modify_first_contact(Contact(firstname="Tom"))


def test__modify_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Anna", mobile="777777777"))
    app.contact.modify_first_contact(Contact(mobile="55555555555"))
