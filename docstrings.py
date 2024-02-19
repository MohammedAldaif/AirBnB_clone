#!/usr/bin/python3

class DocStrings:
    """Helper class for command help functions."""
    @staticmethod
    def help_all(self):
        """Print help for all commands."""
        print("Available commands: create, destroy, show, update, all")
    @staticmethod
    def help_create(self): 
        """Print help for the create command."""
        print("This command creates something.")
    @staticmethod
    def help_destroy(self):
        """Print help for the destroy command."""
        print("This command destroys something.")
    @staticmethod
    def help_show(self):
        """Print help for the show command."""
        print("This command shows something.")
    @staticmethod
    def help_update(self):
        """Print help fr the update command."""
        print("This command updates something.")
