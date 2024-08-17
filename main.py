import sys

from src.Tiles import TilesRefsManager
from src.UI import Window


if __name__ == '__main__':
    if sys.version_info.major < 3:
        print("You need python 3+ version to run this app")
        sys.exit(1)

    _tilesRefsMan = TilesRefsManager()
    _tilesRefsMan.getColorRefs()

    app = Window()
    app.mainloop()
    print("Good bye")

