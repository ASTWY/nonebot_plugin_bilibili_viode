
from nonebot import get_driver
from nonebot.plugin.manager import PluginLoader

from .config import Config

if isinstance(globals()["__loader__"], PluginLoader):
    global_config = get_driver().config
    config = Config(**global_config.dict())
    from . import main


__version__ = "0.1.3"
