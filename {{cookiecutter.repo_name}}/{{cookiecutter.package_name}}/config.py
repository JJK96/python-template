import os
from dynaconf import Dynaconf
from pathlib import Path

dir = Path(__file__).parent

settings = Dynaconf(
    envvar_prefix="{{cookiecutter.package_name|upper}}",
    settings_files=[
        dir / '../settings.toml',
        Path(os.environ['HOME']) / '.config' / '{{cookiecutter.package_name}}' / 'settings.toml'
    ],
)
