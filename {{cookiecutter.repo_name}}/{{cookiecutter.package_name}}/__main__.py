import click
from .config import settings
from . import some_action

@click.command()
def main():
    """{{cookiecutter.description}}"""
    print(some_action())


if __name__ == "__main__":
    main()
