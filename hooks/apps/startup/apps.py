import logging
import threading
from importlib import import_module
from time import sleep

from django.apps import AppConfig
from django.conf import settings

logger = logging.getLogger(__name__)


class StartupConfig(AppConfig):
    name = "hooks.apps.startup"

    # pylint: disable=no-self-use
    def ready(self):
        def run(target: callable, zzz: int = 0):
            sleep(zzz)
            target()

        logger.info("init startup routine")

        prefs = settings.DJANGO_HOOKS["STARTUP"]
        delay = prefs.get("DELAY", 0)

        for hook in prefs.get("HOOKS", []):
            logger.info("running hook: %s", hook)

            module, name = hook.rsplit(".", 1)
            method = getattr(import_module(module), name)

            threading.Thread(target=run, args=[method, delay]).start()

        logger.info("finished startup routine")
