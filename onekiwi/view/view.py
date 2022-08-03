import wx
from .dialog import *
from ..kicad.board import get_current_unit

class FootprintTextView(FootprintTextDialog):
    def __init__(self):
        FootprintTextDialog.__init__(self, None)
        self.AddItemAttributes()
        self.AddItemJustification()
        self.AddItemLayer()
        self.AddItemOrientation()
        self.window = wx.GetTopLevelParent(self)
        self.SetUnit()
        #self.textLog.SetMinSize(self.HighResWxSize(self.window, wx.Size(-1, 150)))
        

    def AddItemAttributes(self):
        items = [
            'F.Silk_Reference', 'B.Silk_Reference', 
            'F.Fab_Reference', 'B.Fab_Reference', 
            'F.Footprint_Value', 'B.Footprint_Value']
        self.choiceAttributes.Append(items)
        self.choiceAttributes.SetSelection(0)

    def AddItemJustification(self):
        items = ['Left', 'Center', 'Right']
        self.choiceJustification.Append(items)
        self.choiceJustification.SetSelection(0)
    
    def AddItemLayer(self):
        items = [
            'F.Silkscreen', 'B.Silkscreen',
            'F.Fab', 'B.Fab', 'F.Cu', 'B.Cu',
            'User.Comments', 'User.1', 'User.2',
            'User.3', 'User.4', 'User.5', 'User.6',
            'User.7', 'User.8', 'User.9']
        self.choiceLayer.Append(items)
        self.choiceLayer.SetSelection(0)
    
    def AddItemOrientation(self):
        items = [
            '0.0', '45.0', '90.0', '135.0', '180.0']
        self.choiceOrientation.Append(items)
        self.choiceOrientation.SetSelection(4)


    def SetUnit(self):
        unit = get_current_unit()
        self.textUnitWith.LabelText = unit
        self.textUnitHeight.LabelText = unit
        self.textUnitThickness.LabelText = unit

    def HighResWxSize(self, window, size):
        """Workaround if wxWidgets Version does not support FromDIP"""
        if hasattr(window, "FromDIP"):
            return window.FromDIP(size)
        else:
            return size