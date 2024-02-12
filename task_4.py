import doctest


class Messengers:
    """
    Base class for messengers.
    """

    def __init__(self, name: str, platform: str):
        """
        Initialize a messenger instance.

        Args:
            name (str): The name of the messenger.
            platform (str): The platform on which the messenger operates.
        """
        self.name = name
        self.platform = platform

    def __str__(self) -> str:
        """
        Return a string representation of the messenger.

        Returns:
            str: The string representation of the messenger.
        """
        return f"{self.name} - {self.platform}"

    def __repr__(self) -> str:
        """
        Return a string representation of the messenger.

        Returns:
            str: The string representation of the messenger.
        """
        return f"{self.__class__.__name__}(name='{self.name}', platform='{self.platform}')"


class Telegram(Messengers):
    """
    Child class representing the Telegram messenger.
    """

    def __init__(self, name: str, platform: str, username: str):
        """
        Initialize a Telegram instance.

        Args:
            name (str): The name of the messenger.
            platform (str): The platform on which Telegram operates.
            username (str): The username associated with the Telegram account.
        """
        super().__init__(name, platform)
        self.username = username

    def send_message(self, message: str):
        """
        Send a message using Telegram.

        Args:
            message (str): The message to be sent.

        Example:
            telegram = Telegram('Telegram', 'iOS', '@example_user')
            telegram.send_message('Hello, world!')
        """
        print(f"Sending message '{message}' on Telegram as {self.username}")

    def __str__(self) -> str:
        """
        Return a string representation of the Telegram messenger.

        Returns:
            str: The string representation of the Telegram messenger.
        """
        return f"{self.name} - {self.platform} (Username: {self.username})"


class Signal(Messengers):
    """
    Child class representing the Signal messenger.
    """

    def __init__(self, name: str, platform: str, phone: str):
        """
        Initialize a Signal instance.

        Args:
            name (str): The name of the messenger.
            platform (str): The platform on which Signal operates.
            phone (str): The phone number associated with the Signal account.
        """
        super().__init__(name, platform)
        self.phone = phone

    def send_message(self, message: str):
        """
        Send a message using Signal.

        Args:
            message (str): The message to be sent.

        Example:
            signal = Signal('Signal', 'Android', '+1234567890')
            signal.send_message('Hello, world!')
        """
        print(f"Sending message '{message}' on Signal using phone number {self.phone}")

    def __str__(self) -> str:
        """
        Return a string representation of the Signal messenger.

        Returns:
            str: The string representation of the Signal messenger.
        """
        return f"{self.name} - {self.platform} (Phone: {self.phone})"


if __name__ == "__main__":
    doctest.testmod()
    pass
