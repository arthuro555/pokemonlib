import logging
from ..misc import Exeptions


playerlog = logging.getLogger("Main.PlayerClass")


class Player(object):
    def __init__(self, new=False, save=None):
        if new:
            self.pokemon = []
            playerlog.info("New player created")
