from ..model.model import Model
from ..view.view import FootprintTextView
from .logtext import LogText
import sys
import logging
import logging.config
import wx

class Controller:
    def __init__(self):
        self.view = FootprintTextView()
        self.logger = self.init_logger(None)
        self.logger = self.init_logger(self.view.textLog)
        self.model = Model(self.logger)
        self.view.buttonUpdate.Bind(wx.EVT_BUTTON, self.OnButtonPressed)

    def Show(self):
        self.view.Show()
    
    def Close(self):
        self.view.Destroy()

    def OnButtonPressed(self, event):
        #self.logger.error("Error Will Robinson!")
        #self.logger.info("Informational message")
        self.model.get_footprint_drawings()


    def init_logger(self, texlog):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        # Log to stderr
        handler1 = logging.StreamHandler(sys.stderr)
        handler1.setLevel(logging.DEBUG)
        # and to our GUI
        handler2 = LogText(texlog)
        handler2.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(funcName)s -  %(message)s",
            datefmt="%Y.%m.%d %H:%M:%S",
        )
        handler1.setFormatter(formatter)
        handler2.setFormatter(formatter)
        root.addHandler(handler1)
        root.addHandler(handler2)
        return logging.getLogger(__name__)
    