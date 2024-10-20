# SS14 Map Converter - Image to YAML

### A tool for quickly converting map drawings to YAML map format of Space Station 14.
![image](https://github.com/user-attachments/assets/2b3bf4a3-9e1a-4f86-9afa-8f214f54e113)
![image](https://github.com/user-attachments/assets/81e55a4b-b6c6-4b69-bce0-82c254763d14)
![image](https://github.com/user-attachments/assets/6b0e3c3d-31ad-435d-ad0f-626a57629f70)


## Installing
To install, you must have a [python](https://www.python.org/downloads/) and [git](https://git-scm.com/downloads).
### 1. Clone this repo
```git clone https://github.com/poeMota/map-converter-ss14```

### 2. Install dependencies
- **Windows:** run `install.bat`.
- **Linux:** run `bash install.sh` from terminal.

Alternatively, you can manually install via terminal:
- `cd map-converter-ss14` - go to the cloned folder.
- `pip install -r requirements.txt` - install dependencies.

### 3. Now you can run the application
```python main.py```


# Usage
The application consists of two pages

## 1. Image
On this page you can:
- Select an image to convert by clicking - **Choose image**.
  - If you select an image with more colors than **256**, a **Warning** window will appear suggesting to convert the image with fewer bits (8-bit is recommended as there are few tiles in the game and this number of colours is the most effective).
  - If you select **PNG** image, the transparent background will be automatically interpreted as space.
- Select a folder to save the output file - **Choose output path**.
- Allow or disallow the use of tiles other than those saved in the **Tiles** folder of the programme by clicking on the **Use any tiles** checkbox.
- Select a name for the output file in the **text field**.
- Convert the image according to the selected settings by pressing - **Convert**

## 2. Settings
Once the image is loaded, this page will show options for customising each of the colors.

- **Type** - here you can choose how the colour will be interpreted on the image - Tile/Object
- **Tile name** - name of the tile that will be added to the map for this colour
 - In **Entity** mode, the tile will simply be added under it.
- **Entity proto** - field that appears in Object mode, in it you should enter the names of prototypes of objects that will be added, there can be several objects, they should be separated by a space, for example "**Window Grille**" - adding windows and grilles to the tile.
- **Autogenerate** - button for map art, it generates **tiles **according to color.
