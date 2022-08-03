from ..model.model import Model, Status
from ..view.view import FootprintTextView
from .logtext import LogText
import sys
import logging
import logging.config
import wx
import pcbnew

class Controller:
    def __init__(self):
        self.view = FootprintTextView()
        self.logger = self.init_logger(None)
        self.logger = self.init_logger(self.view.textLog)
        self.model = Model(pcbnew.GetBoard(), self.logger)

        # Connect Events
        self.view.buttonUpdate.Bind(wx.EVT_BUTTON, self.OnButtonPressed)
        self.view.choiceAttributes.Bind( wx.EVT_CHOICE, self.OnChoiceAttributes)
        self.view.choiceJustification.Bind( wx.EVT_CHOICE, self.OnChoiceJustification)
        self.view.choiceLayer.Bind( wx.EVT_CHOICE, self.OnChoiceLayer)
        self.view.choiceOrientation.Bind( wx.EVT_CHOICE, self.OnChoiceOrientation)

    def Show(self):
        self.view.Show()
    
    def Close(self):
        self.view.Destroy()

    def OnButtonPressed(self, event):
        self.model.get_footprint_drawings()

    def OnChoiceAttributes(self, event):
        index = event.GetEventObject().GetSelection()
        value = event.GetEventObject().GetString(index)
        self.logger.info('Selected: %s' %value)

    def OnChoiceJustification(self, event):
        index = event.GetEventObject().GetSelection()
        value = event.GetEventObject().GetString(index)
        self.logger.info('Selected: %s' %value)
    
    def OnChoiceLayer(self, event):
        index = event.GetEventObject().GetSelection()
        value = event.GetEventObject().GetString(index)
        self.logger.info('Selected: %s' %value)
    
    def OnChoiceOrientation(self, event):
        index = event.GetEventObject().GetSelection()
        value = event.GetEventObject().GetString(index)
        self.logger.info('Selected: %s' %value)

    def get_current_status(self):
        attribute = self.view.GetAttributesValue()
        layer = self.view.GetLayerValue()
        orientation = self.view.GetOrientationValue()
        justification = self.view.GetJustificationValue()
        width = self.view.GetWidthValue()
        height = self.view.GetHeightValue()
        thickness = self.view.GetThicknessValue()
        checkLayer = self.view.GetLayerChecked()
        checkWidth = self.view.GetWidthChecked()
        checkHeight = self.view.GetHeightChecked()
        checkThickness = self.view.GetThicknessChecked()
        checkJustification = self.view.GetJustificationChecked()
        checkOrientation = self.view.GetOrientationChecked()
        visible = self.view.GetVisibleChecked()
        italic = self.view.GetItalicChecked()
        mirrored = self.view.GetMirroredChecked()
        status = Status(
            attribute, layer, checkLayer, width, checkWidth, 
            height, checkHeight, thickness, checkThickness, 
            justification, checkJustification, orientation, 
            checkOrientation, visible, italic, mirrored
        )
        return status

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
    