import configparser
from typing import Union


class Config:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.config = configparser.ConfigParser()
        self.config.read(self.filename)

    def get(self, section: str, option: str) -> str:
        """Get an option value for a given section."""
        return self.config.get(section.upper(), option)

    def getint(self, section: str, option: str) -> int:
        """Get an option value for a given section as an integer."""
        return self.config.getint(section.upper(), option)

    def set(self, section: str, option: str, value: Union[str, int]) -> None:
        """
        Set an option value for a given section.
        If the section or option doesn't exist, it will be created.

        Changes are written to the config file immediately.
        """
        section = section.upper()
        # Create the section if it doesn't exist
        if not self.config.has_section(section):
            self.config.add_section(section)

        # Set the option
        self.config.set(section, option, str(value))

        # Write the changes to the config file
        with open(self.filename, "w") as configfile:
            self.config.write(configfile)