import sys

from src.Tiles import TilesRefsManager
from src.UI import Window
from src.Config import GlobalSettings


if __name__ == '__main__':
    if sys.version_info.major < 3:
        print("You need python 3+ version to run this app")
        sys.exit(1)

    settings = GlobalSettings()
    _tilesRefsMan = TilesRefsManager()
    _tilesRefsMan.getColorRefs()

    app = Window()
    app.mainloop()

    settings.writeConfig()
    print("Good bye")

