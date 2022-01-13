from collections import defaultdict


class Address:
    street = None
    pincode = None
    city = None
    state = None
    country = None

    def set_street(self, street):
        self.street = street

    def get_street(self):
        return self.street

    def set_pincode(self, pincode):
        self.pincode = pincode

    def get_pincode(self):
        return self.pincode

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_country(self, country):
        self.country = country

    def get_country(self):
        return self.country


class User:
    first_name = None
    last_name = None
    email = None

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email


class Customer(User):
    pass


class Librarian(User):
    pass


class Rack:
    id = None
    description = None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description


class Book:
    id = None
    title = None
    type = None
    authors = []

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_authors(self, authors):
        self.authors = authors

    def get_authors(self):
        return self.authors


class BookItem:
    unique_identifier = None
    publication_date = None
    rack = None
    book_format = None
    book = None

    def set_unique_identifier(self, unique_identifier):
        self.unique_identifier = unique_identifier

    def get_unique_identifier(self):
        return self.unique_identifier

    def set_publication_date(self, publication_date):
        self.publication_date = publication_date

    def get_publication_date(self):
        return self.publication_date

    def set_rack(self, rack):
        self.rack = rack

    def get_rack(self):
        return self.rack

    def set_book_format(self, format):
        self.book_format = format

    def get_book_format(self):
        return self.book_format

    def set_book(self, book):
        self.book = book

    def get_book(self):
        return self.book


class BookIssue:
    book_item = None
    customer = None
    issued_at = None
    returned_at = None
    comment = None

    def set_book_item(self, book_item):
        self.book_item = book_item

    def get_book_item(self):
        return self.book_item

    def set_customer(self, customer):
        self.customer = customer

    def get_customer(self):
        return self.customer

    def set_issued_at(self, issued_at):
        self.issued_at = issued_at

    def get_issued_at(self):
        return self.issued_at

    def set_returned_at(self, returned_at):
        self.returned_at = returned_at

    def get_returned_at(self):
        return self.returned_at

    def set_comment(self, comment):
        self.comment = comment

    def get_comment(self):
        return self.comment


class Fine:
    book_issue = None
    amount = None
    status = None

    def set_book_issue(self, book_issue):
        self.book_issue = book_issue

    def get_book_issue(self):
        return self.book_issue

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    class Library:
        id = None
        addresses = None
        name = None

        def set_id(self, id):
            self.id = id

        def get_id(self):
            self.id

        def set_address(self, address):
            self.address = address

        def get_address(self):
            return self.address

        def set_name(self, name):
            self.name = name

        def get_name(self):
            return self.name


class Library:
    id = None
    address = None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address


class BookSubscribers:
    # book : [customers]
    subscribers = defaultdict(set)


class BookBorrowers:
    # cutomer : [books]
    borrowers = defaultdict(set)
