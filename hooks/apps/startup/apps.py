import logging
import threading
from importlib import import_module
from time import sleep

from django.apps import AppConfig
from django.conf import settings

logger = logging.getLogger(__name__)


def runner(hook: str, config: dict):
    args = config.get("args", [])
    kwargs = config.get("kwargs", {})
    delay = config.get("delay", 0)

    module, name = hook.rsplit(".", 1)
    method = getattr(import_module(module), name)

    sleep(delay)
    method(*args, **kwargs)


class StartupConfig(AppConfig):
    name = "hooks.apps.startup"

    # pylint: disable=no-self-use
    def ready(self):
        logger.info("init startup routine")

        hooks = settings.DJANGO_HOOKS["STARTUP"]

        for hook, config in hooks.items():
            logger.info("running hook: %s", hook)
            threading.Thread(target=runner, args=[hook, config]).start()

        logger.info("finished startup routine")
