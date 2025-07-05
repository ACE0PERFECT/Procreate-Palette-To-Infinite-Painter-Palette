import zipfile
import json
import colorsys
from io import TextIOWrapper


# this is path of the .Swatches file
zip_file_path = "水_力_昼.swatches"








def read_json_from_zip(zip_path, json_filename=None):
    """
    Read json file from .Swatches file. (.Swatches file is exported from Procreate color palette)
    
    Params:
        zip_path: File path of .Swatches file.
        json_filename: Exact wanted json file name. Actually this is of no use because you can only export one palette from Procreate so far.
        
    Return:
        dict: the json data.
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            # if not assigned json file name, will use the first json file
            if json_filename is None:
                json_files = [f for f in zf.namelist() if f.lower().endswith('.json')]
                if not json_files:
                    raise FileNotFoundError("No json file found in the zip file.")
                json_filename = json_files[0]
            
            # read and parse
            with zf.open(json_filename) as json_file:
                # make sure the coding is correct
                with TextIOWrapper(json_file, encoding='utf-8') as text_file:
                    return json.load(text_file)
    
    except zipfile.BadZipFile:
        raise ValueError("Zip file corrupted.")
    except KeyError:
        raise FileNotFoundError(f"Zip file contains no such file: {json_filename}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing zip file: {e}")
    
def hsv_to_IPColor(h, s, v):
    """
    Converts HSV to ARGB in decimal. According to IP staff, the A for palette is always FF.
    
    Params:
        h (float): Hue (0-360)
        s (float): Saturation (0-100 or 0-1)
        v (float): Brightness (0-100 or 0-1)
    
    Return:
        int: Decimal ARGB code
    """
    # uniform
    if s > 1 or v > 1:  
        s /= 100.0
        v /= 100.0
    
    h = h % 360 / 360.0
    
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    
    # make sure its within 0-255
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))
    return int(f"0xFF{r:02x}{g:02x}{b:02x}".upper(),16)

# example
if __name__ == "__main__":
    try:
        pro = read_json_from_zip(zip_file_path)

        palette_name = str(pro["name"])
        pro_colors = pro["swatches"]
        shift = int("0x100000000", 16)
        converted = []
        for i, color in enumerate(pro_colors):

            # palette in Procreate is 3x10 while it in IP is 5xN
            if i > 29: 
                break

            # if its None then the color is undefined in Pro, but IP doesn't support undefined color in palette
            #  so it's discarded.
            if color == None:
                continue
            converted.append(hsv_to_IPColor(360*color["hue"],color["saturation"],color["brightness"])-shift)

        data = {
            "colors":converted,
            "name": palette_name
        }
        with open(palette_name+".clrs", "w") as f:
            json.dump(data, f, indent=4)
        
    
    except Exception as e:
        print(f"Encountered error: {e}")

