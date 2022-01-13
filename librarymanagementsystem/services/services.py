from collections import defaultdict
from librarymanagementsystem.models import (
    Address, Customer, Librarian, Book, BookItem,
    Rack, BookIssue, Fine, Library, BookBorrowers,
    BookSubscribers
)


class AddressService:
    def __init__(self):
        pass

    def add_address(self, street, pincode, city, state, country):
        address = Address()
        address.set_street(street)
        address.set_pincode(pincode)
        address.set_city(city)
        address.set_state(state)
        address.set_country(country)
        return address


class CustomerService:
    def __init__(self):
        self.books_checked_out = defaultdict(set)

    def add_customer(self, first_name, last_name, email):
        customer = Customer()
        customer.set_first_name(first_name)
        customer.set_last_name(last_name)
        customer.set_email(email)
        return customer


class LibrarianService:
    def __init__(self):
        pass

    def add_customer(self, first_name, last_name, email):
        librarian = Librarian()
        librarian.set_first_name(first_name)
        librarian.set_last_name(last_name)
        librarian.set_email(email)
        return librarian

    def issue_book(self, book_item, customer):
        pass

    def returned_issued_book(self, book_issue):
        pass


class RackService:
    def __init__(self):
        pass

    def add_rack(self, id, description):
        rack = Rack()
        rack.set_id(id)
        rack.set_description(description)
        return rack


class BookService:
    def __init__(self):
        books = dict(set)  # book_id: [book_items]
        subscribers = defaultdict(set)

    def add_book(self, id, title, type, authors):
        book = Book()
        book.set_id(id)
        book.set_title(title)
        book.set_type(type)
        book.set_authors(authors)
        self.books[id] = book
        return self.books[id]

    def subscribe_books(self, book_id, customer_id):
        pass

    def is_book_present(self, book_id):
        return book_id in self.books

    def remove_book(self, book_id):
        pass

    def get_books(self):
        return self.books


class BookItemService:
    def __init__(self):
        pass

    def add_book_item(self, book, unique_identifier, publication_date, rack, book_format):
        book_item = BookItem()
        book_item.set_book(book)
        book_item.set_unique_identifier(unique_identifier)
        book_item.set_publication_date(publication_date)
        book_item.set_book_format(book_format)
        book_item.set_rack(rack)
        return book_item


class BookIssueService:
    def __init__(self):
        pass

    def add_book_issue(self, book_item, customer, issued_at, comment=None):
        book_issue = BookIssue()
        book_issue.set_book_item(book_item)
        book_issue.set_customer(customer)
        book_issue.set_issued_at(issued_at)
        book_issue.set_comment(comment)
        return book_issue


class FineService:
    def __init__(self):
        pass

    def add_fine(self, book_issue, amount, status):
        fine = Fine()
        fine.set_book_issue(book_issue)
        fine.set_amount(amount)
        fine.set_status(status)
        return fine

    def collect_fine(self, book_issue):
        pass



class SearchService:
    def search_by_title(self, title, book_items):
        pass

    def search_by_author(self, author, book_items):
        pass

    def search_by_book_type(self, book_type, book_items):
        pass

    def serach_by_publisher(self, publisher, book_items):
        pass


class LibraryService:
    def __init__(self):
        pass

    def add_library(self, id, name, address):
        library = Library()
        library.set_id(id)
        library.set_name(name)
        library.set_address(address)
        return library
