import pcbnew

class FootprintDrawing:
    def __init__(self):
        self.reference = []
        self.value = []
        self.fabrication = []
        board = pcbnew.GetBoard()
        self.footprints = board.GetFootprints()
        self.get_footprint_drawings()
    
    def get_footprint_drawings(self):
        for footprint in self.footprints:
            self.reference.append(footprint.Reference())
            self.value.append(footprint.Value())
            for drawing in footprint.GraphicalItems():
                if drawing.GetClass() == 'MTEXT':
                    self.fabrication.append(drawing)
    