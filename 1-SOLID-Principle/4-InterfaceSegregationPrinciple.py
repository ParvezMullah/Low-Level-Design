"""
Definition :
    Clients should not be forced to depend upon the methods they dont use.
"""

from abc import ABC, abstractmethod

################################ Violation of ISP ################################


class CloudProvider(ABC):
    @abstractmethod
    def store_file(self):
        pass

    @abstractmethod
    def get_file(self):
        pass

    @abstractmethod
    def create_server(self):
        pass

    @abstractmethod
    def list_server(self):
        pass

    @abstractmethod
    def get_cdn_addresses(self):
        pass


class Amazon(CloudProvider):
    def store_file(self):
        print("file stored!")

    def get_file(self):
        print("file retrieved!")

    def create_server(self):
        print("server created!")

    def list_server(self):
        print("server list!")

    def get_cdn_addresses(self):
        print("CDN addresses")


class Dropbox(CloudProvider):
    def store_file(self):
        print("file stored!")

    def get_file(self):
        print("file retrieved!")

    def create_server(self):
        raise Exception("Service not available!")

    def list_server(self):
        raise Exception("Service not available!")

    def get_cdn_addresses(self):
        raise Exception("Service not available!")


# dropbox = Dropbox()
# dropbox.store_file()
# #Below line will give error because dropbox does not provides these features.
# dropbox.create_server()


################################ Correct Way by ISP ################################


class CloudStorageProvider(ABC):
    @abstractmethod
    def store_file(self):
        pass

    @abstractmethod
    def get_file(self):
        pass


class CloudHostProvider(ABC):
    @abstractmethod
    def create_server(self):
        pass

    @abstractmethod
    def get_server(self):
        pass


class CloudCDNProvider(ABC):
    @abstractmethod
    def get_cdn_addresses(self):
        pass


class Amazon(CloudStorageProvider, CloudHostProvider, CloudCDNProvider):
    def store_file(self):
        print("file stored!")

    def get_file(self):
        print("file retrieved!")

    def create_server(self):
        print("server created!")

    def get_server(self):
        print("server list!")

    def get_cdn_addresses(self):
        print("CDN addresses")


class Dropbox(CloudStorageProvider):
    def store_file(self):
        print("file stored!")

    def get_file(self):
        print("file retrieved!")


amazon = Amazon()
amazon.store_file()
amazon.get_file()
amazon.create_server()
amazon.get_server()
amazon.get_cdn_addresses()

dropbox = Dropbox()
dropbox.store_file()
dropbox.get_file()
