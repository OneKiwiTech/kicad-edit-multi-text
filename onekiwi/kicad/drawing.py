import pcbnew

class FootprintDrawing:
    def __init__(self):
        self.drawings = []
        board = pcbnew.GetBoard()
        self.footprints = board.GetFootprints()
    
    def get_footprint_drawings():
        drawings = []
        board = pcbnew.GetBoard()
        footprints = board.GetFootprints()

        for f in footprints:
            #drawings.append(("ref", f.Reference()))
            #drawings.append(("val", f.Value()))
            for d in f.GraphicalItems():
                print('class: %s' %d.GetClass())
                #drawings.append((d.GetClass(), d))
        return drawings