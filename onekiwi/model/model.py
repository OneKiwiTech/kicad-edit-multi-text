import pcbnew

class Model:
    def __init__(self, logger):
        self.logger = logger
        self.board = pcbnew.GetBoard()

    def get_footprint_drawings(self):
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
