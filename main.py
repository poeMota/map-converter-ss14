from src.Tiles import TilesRefsManager
from src.UI import Window


if __name__ == '__main__':
    _tilesRefsMan = TilesRefsManager()
    _tilesRefsMan.getColorRefs()

    app = Window()
    app.mainloop()

