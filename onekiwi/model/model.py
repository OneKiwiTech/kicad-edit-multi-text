import pcbnew
import math
from ..kicad.board import get_current_unit

class Status:
    def __init__(
    self, attribute, layer, checkLayer, width, checkWidth, 
    height, checkHeight, thickness, checkThickness, 
    justification, checkJustification, orientation, checkOrientation,
    visible, italic, mirrored
    ):
        self.attribute = attribute
        self.layer = layer
        self.checkLayer = checkLayer
        self.width = width
        self.checkWidth = checkWidth
        self.height = height
        self.checkHeight = checkHeight
        self.thickness = thickness
        self.checkThickness = checkThickness
        self.justification = justification
        self.checkJustification = checkJustification
        self.orientation = orientation
        self.checkOrientation = checkOrientation
        self.visible = visible
        self.italic = italic
        self.mirrored = mirrored

class Model:
    def __init__(self, board, status, logger):
        self.logger = logger
        self.top_refs = []
        self.top_vals = []
        self.top_fabs = []
        self.bot_refs = []
        self.bot_vals = []
        self.bot_fabs = []
        self.status:Status = status
        self.unit = get_current_unit()
        self.footprints = board.GetFootprints()
        self.get_footprint_drawings()

    def get_footprint_drawings(self):
        for footprint in self.footprints:
            if footprint.IsFlipped() == True:
                self.bot_refs.append(footprint.Reference())
                self.bot_vals.append(footprint.Value())
                for drawing in footprint.GraphicalItems():
                    if drawing.GetClass() == 'MTEXT':
                        self.bot_fabs.append(drawing)
            else:
                self.top_refs.append(footprint.Reference())
                self.top_vals.append(footprint.Value())
                for drawing in footprint.GraphicalItems():
                    if drawing.GetClass() == 'MTEXT':
                        self.top_fabs.append(drawing)

    def update_status(self, status):
        self.status = status

    def check_attribute(self):
        if self.status.attribute == 'F.Silk_Reference':
            self.set_reference_top()
        if self.status.attribute == 'B.Silk_Reference':
            self.set_reference_bot()
        if self.status.attribute == 'F.Footprint_Value':
            self.set_value_top()
        if self.status.attribute == 'B.Footprint_Value':
            self.set_value_bot()
        if self.status.attribute == 'F.Fab_Reference':
            self.set_fabrication_top()
        if self.status.attribute == 'B.Fab_Reference':
            self.set_fabrication_bot()

    def set_reference_top(self):
        self.logger.info('len: %d' %len(self.top_refs))
        for text in self.top_refs:
            self.update_text_value(text)
        pcbnew.Refresh()

    def set_reference_bot(self):
        self.logger.info('len: %d' %len(self.bot_refs))
        for text in self.bot_refs:
            self.update_text_value(text)
        pcbnew.Refresh()

    def set_value_top(self):
        self.logger.info('len: %d' %len(self.top_vals))
        for text in self.top_vals:
            self.update_text_value(text)
        pcbnew.Refresh()

    def set_value_bot(self):
        self.logger.info('len: %d' %len(self.bot_vals))
        for text in self.bot_vals:
            self.update_text_value(text)
        pcbnew.Refresh()

    def set_fabrication_top(self):
        self.logger.info('len: %d' %len(self.bot_fabs))
        for text in self.top_fabs:
            self.update_text_value(text)
        pcbnew.Refresh()

    def set_fabrication_bot(self):
        self.logger.info('len: %d' %len(self.bot_fabs))
        for text in self.bot_fabs:
            self.update_text_value(text)
        pcbnew.Refresh()

    def update_text_value(self, text):
        self.logger.info('xxx: %s' %self.status.thickness)
        
        if self.status.italic == True:
            text.SetItalic(True)
        else:
            text.SetItalic(False)

        if self.status.mirrored == True:
            text.SetMirrored(True)
        else:
            text.SetMirrored(False)
        
        if self.status.visible == True:
            text.SetVisible(True)
        else:
            text.SetVisible(False)

        if self.status.checkJustification == True:
            text.SetHorizJustify(self.status.justification)
        
        if self.status.checkOrientation == True:
            text.SetTextAngle(math.pi/2)
        
        if self.status.checkWidth == True:
            widthf = float(self.status.width)
            if self.unit == 'mm':
                width = int(1000000*widthf)
            if self.unit == 'mil':
                width = int(25400*widthf)
            if self.unit == 'in':
                width = int(25400000*widthf)
            text.SetTextWidth(width)

        if self.status.checkHeight == True:
            heightf = float(self.status.height)
            if self.unit == 'mm':
                height = int(1000000*heightf)
            if self.unit == 'mil':
                height = int(25400*heightf)
            if self.unit == 'in':
                height = int(25400000*heightf)
            text.SetTextThickness(height)

        if self.status.checkThickness == True:
            thicknessf = float(self.status.thickness)
            if self.unit == 'mm':
                thickness = int(1000000*thicknessf)
            if self.unit == 'mil':
                thickness = int(25400*thicknessf)
            if self.unit == 'in':
                thickness = int(25400000*thicknessf)
            text.SetTextThickness(thickness)

    def get_footprint_drawingss(self):
        drawings = []
        footprints = self.board.GetFootprints()
        """
        for d in self.board.GetDrawings():
            if d.GetClass() == 'PTEXT' and d.GetLayer() == pcbnew.F_SilkS:
                self.logger.info('class: %s' %d.GetClass())
                self.logger.info('text: %s' %d.GetText())
        """
    
        check = 3
        for f in footprints:
            if check == 1:
                for d in f.GraphicalItems():
                    if d.GetClass() == 'MTEXT' and d.GetLayer() == pcbnew.F_Fab:
                        self.logger.info('===================')
                        self.logger.info('class: %s' %d.GetClass())
                        self.logger.info('Text: %s' %d.GetText())
                        self.logger.info('ShownText: %s' %d.GetShownText())
                        self.logger.info('TextWidth: %s' %d.GetTextWidth())
                        self.logger.info('TextHeight: %s' %d.GetTextHeight())
                        self.logger.info('TextThickness: %s' %d.GetTextThickness())
                        d.SetItalic(True)
                        d.SetLayer(pcbnew.F_Fab)
            elif check == 2:
                if f.Reference().GetLayer() == pcbnew.F_SilkS:
                    self.logger.info('class: %s' %f.Reference().GetClass())
                    self.logger.info('Text: %s' %f.Reference().GetText())
                    self.logger.info('ShownText: %s' %f.Reference().GetShownText())
                    self.logger.info('TextWidth: %s' %f.Reference().GetTextWidth())
                    self.logger.info('TextHeight: %s' %f.Reference().GetTextHeight())
                    self.logger.info('TextThickness: %s' %f.Reference().GetTextThickness())
                    f.Reference().SetVisible(True)
            else:
                if f.Value().GetLayer() == pcbnew.User_1:
                    self.logger.info('class: %s' %f.Value().GetClass())
                    self.logger.info('Text: %s' %f.Value().GetText())
                    self.logger.info('ShownText: %s' %f.Value().GetShownText())
                    self.logger.info('TextWidth: %s' %f.Value().GetTextWidth())
                    self.logger.info('TextHeight: %s' %f.Value().GetTextHeight())
                    self.logger.info('TextThickness: %s' %f.Value().GetTextThickness())
                    f.Value().SetVisible(True)
        pcbnew.Refresh()
        return drawings
