import pcbnew
from ..kicad.board import get_current_unit

class Model:
    def __init__(self, board, logger):
        self.logger = logger
        self.top_refs = []
        self.top_vals = []
        self.top_fabs = []
        self.bot_refs = []
        self.bot_vals = []
        self.bot_fabs = []
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

    def set_reference(self, attribute):
        if attribute == 'F.Silk_Reference':
            self.set_reference_top()
        elif attribute == 'B.Silk_Reference':
            self.set_reference_bot()

    def set_value(self, attribute):
        if attribute == 'F.Footprint_Value':
            self.set_value_top()
        elif attribute == 'B.Footprint_Value':
            self.set_value_bot()

    def set_fabrication(self, attribute):
        if attribute == 'F.Fab_Reference':
            self.set_fabrication_top()
        elif attribute == 'B.Fab_Reference':
            self.set_fabrication_bot()
            
    def set_reference_top(self):
        pass
    def set_reference_bot(self):
        pass
    def set_value_top(self):
        pass
    def set_value_bot(self):
        pass
    def set_fabrication_top(self):
        pass
    def set_fabrication_bot(self):
        pass
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
