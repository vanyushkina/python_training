from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Anton", mobile="656388735678"))
    app.contact.delete_first_contact()
