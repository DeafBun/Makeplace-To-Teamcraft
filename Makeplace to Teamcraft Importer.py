### CREATED BY PETRA ULSTRAD
### HTTPS://PETRA.CARRD.CO
### IF I SEE ANYONE CHARGING FOR THIS PLS DONT IDK HOW TO LICENSE ITS JUST SUPPOSED TO BE A NICE PIECE OF CODE THATLL HELP PEOPLE DEAL WITH A LITTLE LESS MONOTANY
import os
import json
import base64
from collections import Counter
import webbrowser
import time
import tkinter as tk
from tkinter import filedialog
browser = webbrowser.get()
counter = {}

##DISCLAIMERS:
print("Please be sure to use the most recent version of Makeplace for this converter to work at its best!")
print("")
##time.sleep(2)
print("A file dialogue will open shortly. Please select the file you wish to convert.")
print("")
##time.sleep(2)
#print("Be sure to remove the quotation marks from the file path as well!")
#print("")
#time.sleep(2)
print("Happy Housing!")
print("")
#time.sleep(2)

def choose_file():
    default_dir = os.path.join(os.path.expandvars("%APPDATA%"), "itch/apps/Makeplace/MakePlace/Save")
    file_path = filedialog.askopenfilename(initialdir=default_dir, filetypes=[("Makeplace JSON files", "*.json")])
    return file_path

## FILE AND URL
mpFile = choose_file()
print("")
file = open(mpFile)
data = json.load(file)
url = "https://ffxivteamcraft.com/import/"

## THINKMODE TOGGLE
thinkmode = 0
speed = 0

money = 0

if thinkmode != 1:
    thinkmode = 0
elif thinkmode == 1:
    speed = int(input("Please input wait time between steps in ms: "))/1000

#########################################################################################################################################

## THESE ARE FUNCTIONS I STOLE FROM THE INTERNET
def remove1st(string,substring):
    return "".join(string.split(substring,1))

def extract_element_from_json(obj, path):
    def extract(obj, path, ind, arr):
        key = path[ind]
        if ind + 1 < len(path):
            if isinstance(obj, dict):
                if key in obj.keys():
                    extract(obj.get(key), path, ind + 1, arr)
                else:
                    arr.append(None)
            elif isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        extract(item, path, ind, arr)
            else:
                arr.append(None)
        if ind + 1 == len(path):
            if isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        arr.append(item.get(key, None))
            elif isinstance(obj, dict):
                arr.append(obj.get(key, None))
            else:
                arr.append(None)
        return arr
    if isinstance(obj, dict):
        return extract(obj, path, 0, [])
    elif isinstance(obj, list):
        outer_arr = []
        for item in obj:
            outer_arr.append(extract(item, path, 0, []))
        return outer_arr

#########################################################################################################################################

## LOAD THE DATA

## FURNITURES
insideFurniture = data["interiorFurniture"]
outsideFurniture = data["exteriorFurniture"]

## CHANDELIER WALLS FLOORS ETC ETC
insideFixtures = data["interiorFixture"]
outsideFixtures = data["exteriorFixture"]

## HOUSE SIZE
houseSize = data["houseSize"]

#########################################################################################################################################

#### INITIALIZE ALL OF THE LISTS

## INSIDE FURNITURE LISTS
inside_furniturelistNames = []
inside_furniturelistData = []

## INSIDE FIXTURE LISTS
inside_fixturelistNames = []
inside_fixturelistData = []
inside_fixtureDyes = []

## OUTSIDE FURNITURE LISTS
outside_furniturelistNames = []
outside_furniturelistData = []
outside_furniture_amount = 0

## OUTSIDE FIXTURE LISTS
outside_fixturelistNames = []
outside_fixturelistData = []

## DYES
dyeNames = []
dyeID = []
dyelistrawIN = list(extract_element_from_json(data, ["interiorFurniture", "properties", "color"]))
dyelistrawOUT = list(extract_element_from_json(data, ["exteriorFurniture", "properties", "color"]))

## Blank Inner Wall
bw_idlist = []
bwDataRaw = list(extract_element_from_json(data, ["interiorFurniture", "properties", "material"]))

## EVERYTHING LIST
furniturelistfull = []


#########################################################################################################################################

## READS JSON FILES

for i in insideFurniture:
    if i != None:
        inside_furniturelistNames.append(i["name"])
        inside_furniturelistData.append(i["itemId"])
        if thinkmode == 1:
            print("Inside Furnishing Added!")
            print("")
            #time.sleep(speed)

for i in outsideFurniture:
    if i != None:
        outside_furniturelistNames.append(i["name"])
        outside_furniturelistData.append(i["itemId"])
        if thinkmode == 1:
            print(f"Outside Furnishing Added!")
            print("")
            #time.sleep(speed)

for i in insideFixtures:
    if i != None:
        inside_fixturelistNames.append(i["name"])
        inside_fixturelistData.append(i["itemId"])
        if thinkmode == 1:
            print(f"Inside Fixture Added!")
            print("")
            #time.sleep(speed)

for i in outsideFixtures:
    if i != None:
        outside_fixturelistNames.append(i["name"])
        outside_fixturelistData.append(i["itemId"])
        if thinkmode == 1:
            print(f"Outside Fixture Added!")
            #time.sleep(speed)

#########################################################################################################################################

## SORTING THE THINGS
if thinkmode == 1:
    print("Sorting Inside Furniture List Names...")
    #time.sleep(speed)

inside_furniturelistNames = sorted(inside_furniturelistNames)

if thinkmode == 1:
    print("Sorting Inside Fixture List Names...")
    #time.sleep(speed)

inside_fixturelistNames = sorted(inside_fixturelistNames)

if thinkmode == 1:
    print("Sorting Inside Furniture List Data...")
    #time.sleep(speed)

inside_fixturelistData = sorted(inside_fixturelistData)

if thinkmode == 1:
    print("Sorting Inside Fixture List Data...")
    #time.sleep(speed)

inside_furniturelistData = sorted(inside_furniturelistData)

if thinkmode == 1:
    print("Sorting Outside Fixture List Names...")
    #time.sleep(speed)

outside_fixturelistNames = sorted(outside_fixturelistNames)

if thinkmode == 1:
    print("Sorting Outside Fixture List Data...")
    #time.sleep(speed)

outside_fixturelistData = sorted(outside_fixturelistData)

if thinkmode == 1:
    print("Sorting Outside Furniture List Names")
    #time.sleep(speed)

outside_furniturelistNames = sorted(outside_furniturelistNames)

if thinkmode == 1:
    print("Sorting Outside Fixture List Names")
    #time.sleep(speed)

outside_furniturelistData = sorted(outside_furniturelistData)

#########################################################################################################################################
## HANDLING OF RANDOM THINGS THAT EQUAL 0
#for i in inside_fixturelistNames:
#    if i == "Leveilleur Estate Interior Wall":
#        inside_fixturelistData.append("38674")
#    if i == "Leveilleur Estate Flooring":
#        inside_fixturelistData.append("38672")
#    if i == "Leveilleur Estate Chandelier":
#        inside_furniturelistData.append("38673")


#########################################################################################################################################

## DYEPUTER
dyelistclean = []

for i in dyelistrawIN:
    if i != None :
        dyelistclean.append(i)

for i in dyelistrawOUT:
    if i != None:
        dyelistclean.append(i)

if thinkmode == 1:
    print("The Dyeputer is running through the 102 case switch statement from hell...")
    #time.sleep(speed * 5)

## THE SWITCH STATEMENT TO END ALL SWITCH STATEMENTS RAHHHHHHHHHHHHHHHHHHHHH
for i in dyelistclean:
    match i:
        case '312D57FF':
            dyeNames.append("Abyssal Blue Dye")
            dyeID.append("5804")
        case '8E581BFF':
            dyeNames.append("Acorn Brown Dye")
            dyeID.append("5755")
        case '5F7558FF':
            dyeNames.append("Adamantoise Green Dye")
            dyeID.append("5782")
        case 'A2875CFF':
            dyeNames.append("Aldgoat Brown Dye")
            dyeID.append("5753")
        case '9BB363FF':
            dyeNames.append("Apple Green Dye")
            dyeID.append("5778")
        case 'ACA8A2FF':
            dyeNames.append("Ash Grey Dye")
            dyeID.append("5730")
        case '6A4B37FF':
            dyeNames.append("Bark Brown Dye")
            dyeID.append("5746")
        case '913B27FF':
            dyeNames.append("Blood Red Dye")
            dyeID.append("5742")
        case 'EBD3A0FF':
            dyeNames.append("Bone White Dye")
            dyeID.append("5762")
        case '658241FF':
            dyeNames.append("Cactaur Green Dye")
            dyeID.append("5779")
        case 'FEF864FF':
            dyeNames.append("Canary Yellow Dye")
            dyeID.append("30118")
        case '96BDB9FF':
            dyeNames.append("Celeste Green Dye")
            dyeID.append("5785")
        case '4F5766FF':
            dyeNames.append("Ceruleum Blue Dye")
            dyeID.append("5794")
        case '484742FF':
            dyeNames.append("Charcoal Grey Dye")
            dyeID.append("5733")
        case 'F5379BFF':
            dyeNames.append("Cherry Pink Dye")
            dyeID.append("30117")
        case '3D290DFF':
            dyeNames.append("Chestnut Brown Dye")
            dyeID.append("5757")
        case '6E3D24FF':
            dyeNames.append("Chocolate Brown Dye")
            dyeID.append("5747")
        case 'BC8804FF':
            dyeNames.append("Coeurl Yellow Dye")
            dyeID.append("5767")
        case 'DC9BCAFF':
            dyeNames.append("Colibri Pink Dye")
            dyeID.append("5811")
        case 'CC6C5EFF':
            dyeNames.append("Coral Pink Dye")
            dyeID.append("5741")
        case 'C99156FF':
            dyeNames.append("Cork Brown Dye")
            dyeID.append("5750")
        case '8E9BACFF':
            dyeNames.append("Corpse Blue Dye")
            dyeID.append("5793")
        case 'F2D770FF':
            dyeNames.append("Cream Yellow Dye")
            dyeID.append("5768")
        case '322C3BFF':
            dyeNames.append("Currant Purple Dye")
            dyeID.append("5807")
        case '781A1AFF':
            dyeNames.append("Dalamud Red Dye")
            dyeID.append("5738")
        case '121F2DFF':
            dyeNames.append("Dark Blue Dye")
            dyeID.append("8740")
        case '28211CFF':
            dyeNames.append("Dark Brown Dye")
            dyeID.append("8736")
        case '152C2CFF':
            dyeNames.append("Dark Green Dye")
            dyeID.append("8738")
        case '232026FF':
            dyeNames.append("Dark Purple Dye")
            dyeID.append("8742")
        case '321919FF':
            dyeNames.append("Dark Red Dye")
            dyeID.append("8735")
        case '1E2A21FF':
            dyeNames.append("Deepwood Green Dye")
            dyeID.append("5784")
        case 'DBB457FF':
            dyeNames.append("Desert Yellow Dye")
            dyeID.append("5764")
        case '000EA2FF':
            dyeNames.append("Dragoon Blue Dye")
            dyeID.append("30120")
        case '514560FF':
            dyeNames.append("Gloom Purple Dye")
            dyeID.append("5806")
        case 'B9A489FF':
            dyeNames.append("Gobbiebag Brown Dye")
            dyeID.append("5758")
        case '898784FF':
            dyeNames.append("Goobbue Grey Dye")
            dyeID.append("5731")
        case '3B2A3DFF':
            dyeNames.append("Grape Purple Dye")
            dyeID.append("5809")
        case 'A58430FF':
            dyeNames.append("Halatali Yellow Dye")
            dyeID.append("5769")
        case 'FAC62BFF':
            dyeNames.append("Honey Yellow Dye")
            dyeID.append("5765")
        case '284B2CFF':
            dyeNames.append("Hunter Green Dye")
            dyeID.append("5780")
        case 'B2C4CEFF':
            dyeNames.append("Ice Blue Dye")
            dyeID.append("5788")
        case '1A1F27FF':
            dyeNames.append("Ink Blue Dye")
            dyeID.append("5796")
        case 'B79EBCFF':
            dyeNames.append("Iris Purple Dye")
            dyeID.append("5808")
        case '1E1E1EFF':
            dyeNames.append("Jet Black Dye")
            dyeID.append("8733")
        case '30211BFF':
            dyeNames.append("Kobold Brown Dye")
            dyeID.append("5749")
        case '877FAEFF':
            dyeNames.append("Lavender Purple Dye")
            dyeID.append("5805")
        case '836969FF':
            dyeNames.append("Lilac Purple Dye")
            dyeID.append("5736")
        case 'ABB054FF':
            dyeNames.append("Lime Green Dye")
            dyeID.append("5773")
        case '3F3329FF':
            dyeNames.append("Loam Brown Dye")
            dyeID.append("5761")
        case 'FECEF5FF':
            dyeNames.append("Lotus Pink Dye")
            dyeID.append("5810")
        case '323621FF':
            dyeNames.append("Marsh Green Dye")
            dyeID.append("5777")
        case '8B9C63FF':
            dyeNames.append("Meadow Green Dye")
            dyeID.append("5775")
        case '7D3906FF':
            dyeNames.append("Mesa Red Dye")
            dyeID.append("5745")
        case '181937FF':
            dyeNames.append("Midnight Blue Dye")
            dyeID.append("5802")
        case 'E49E34FF':
            dyeNames.append("Millioncorn Yellow Dye")
            dyeID.append("5766")
        case '615245FF':
            dyeNames.append("Mole Brown Dye")
            dyeID.append("5760")
        case '1F4646FF':
            dyeNames.append("Morbol Green Dye")
            dyeID.append("5787")
        case '707326FF':
            dyeNames.append("Moss Green Dye")
            dyeID.append("5774")
        case '585230FF':
            dyeNames.append("Mud Green Dye")
            dyeID.append("5771")
        case '3B4D3CFF':
            dyeNames.append("Nophica Green Dye")
            dyeID.append("5783")
        case '406339FF':
            dyeNames.append("Ochu Green Dye")
            dyeID.append("5781")
        case '4B5232FF':
            dyeNames.append("Olive Green Dye")
            dyeID.append("5776")
        case '7B5C2DFF':
            dyeNames.append("Opo-opo Brown Dye")
            dyeID.append("5752")
        case '644216FF':
            dyeNames.append("Orchard Brown Dye")
            dyeID.append("5752")
        case '2F5889FF':
            dyeNames.append("Othard Blue Dye")
            dyeID.append("5756")
        case '96A4D9FF':
            dyeNames.append("Pastel Blue Dye")
            dyeID.append("8739")
        case 'BACFAAFF':
            dyeNames.append("Pastel Green Dye")
            dyeID.append("8737")
        case 'FDC8C6FF':
            dyeNames.append("Pastel Pink Dye")
            dyeID.append("8734")
        case 'BBB5DAFF':
            dyeNames.append("Pastel Purple Dye")
            dyeID.append("8741")
        case '3B6886FF':
            dyeNames.append("Peacock Blue Dye")
            dyeID.append("5791")
        case '79526CFF':
            dyeNames.append("Plum Purple Dye")
            dyeID.append("5812")
        case 'C57424FF':
            dyeNames.append("Pumpkin Orange Dye")
            dyeID.append("5754")
        case 'F9F8F4FF':
            dyeNames.append("Pure White Dye")
            dyeID.append("8732")
        case '996E3FFF':
            dyeNames.append("Qiqirn Brown Dye")
            dyeID.append("5751")
        case '403311FF':
            dyeNames.append("Raisin Brown Dye")
            dyeID.append("5770")
        case '5B7FC0FF':
            dyeNames.append("Raptor Blue Dye")
            dyeID.append("5797")
        case '66304EFF':
            dyeNames.append("Regal Purple Dye")
            dyeID.append("5813")
        case '1C3D54FF':
            dyeNames.append("Rhotano Blue Dye")
            dyeID.append("5792")
        case '5B1729FF':
            dyeNames.append("Rolanberry Red Dye")
            dyeID.append("5737")
        case 'E69F96FF':
            dyeNames.append("Rose Pink Dye")
            dyeID.append("5735")
        case '273067FF':
            dyeNames.append("Royal Blue Dye")
            dyeID.append("5801")
        case 'E40011FF':
            dyeNames.append("Ruby Red Dye")
            dyeID.append("30116")
        case '4F2D1FFF':
            dyeNames.append("Russet Brown Dye")
            dyeID.append("5748")
        case '622207FF':
            dyeNames.append("Rust Red Dye")
            dyeID.append("5739")
        case 'E4AA8AFF':
            dyeNames.append("Salmon Pink Dye")
            dyeID.append("5743")
        case '6481A0FF':
            dyeNames.append("Seafog Blue Dye")
            dyeID.append("5790")
        case '373747FF':
            dyeNames.append("Shadow Blue Dye")
            dyeID.append("5803")
        case '92816CFF':
            dyeNames.append("Shale Brown Dye")
            dyeID.append("5759")
        case '83B0D2FF':
            dyeNames.append("Sky Blue Dye")
            dyeID.append("5789")
        case '656565FF':
            dyeNames.append("Slate Grey Dye")
            dyeID.append("5732")
        case 'E4DFD0FF':
            dyeNames.append("Snow White Dye")
            dyeID.append("5729")
        case '2B2923FF':
            dyeNames.append("Soot Black Dye")
            dyeID.append("5734")
        case '234172FF':
            dyeNames.append("Storm Blue Dye")
            dyeID.append("5799")
        case 'B75C2DFF':
            dyeNames.append("Sunset Orange Dye")
            dyeID.append("5744")
        case 'BBBB8AFF':
            dyeNames.append("Sylph Green Dye")
            dyeID.append("5772")
        case '04AFCDFF':
            dyeNames.append("Turquoise Blue Dye")
            dyeID.append("30121")
        case '437272FF':
            dyeNames.append("Turquoise Green Dye")
            dyeID.append("5786")
        case 'B7A370FF':
            dyeNames.append("Ul Brown Dye")
            dyeID.append("5763")
        case 'FBF1B4FF':
            dyeNames.append("Vanilla Yellow Dye")
            dyeID.append("30119")
        case '112944FF':
            dyeNames.append("Void Blue Dye")
            dyeID.append("5800")
        case '451511FF':
            dyeNames.append("Wine Red Dye")
            dyeID.append("5740")
        case '2F3851FF':
            dyeNames.append("Woad Blue Dye")
            dyeID.append("5795")

#########################################################################################################################################

## BLANKWALLPUTER

for i in bwDataRaw:
    match i:
        case "/Game/HouseAssets/Wallpaper/AlpineInnerWall/AlpineInnerWall.AlpineInnerWall":
            bw_idlist.append("14070")
        case "/Game/HouseAssets/Wallpaper/AmaurotineInteriorWall/AmaurotineInteriorWall.AmaurotineInteriorWall":
            bw_idlist.append("37408")
        case "/Game/HouseAssets/Wallpaper/ArborInteriorWall/ArborInteriorWall.ArborInteriorWall":
            bw_idlist.append("7138")
        case "/Game/HouseAssets/Wallpaper/Black-and-whiteInteriorWall/Black-and-whiteInteriorWall.Black-and-whiteInteriorWall":
            bw_idlist.append("24539")
        case "/Game/HouseAssets/Wallpaper/BlueskyInteriorWall/BlueskyInteriorWall.BlueskyInteriorWall":
            bw_idlist.append("15165")
        case "/Game/HouseAssets/Wallpaper/ChocoboInteriorWall/ChocoboInteriorWall.ChocoboInteriorWall":
            bw_idlist.append("7139")
        case "/Game/HouseAssets/Wallpaper/ClassicInteriorWall/ClassicInteriorWall.ClassicInteriorWall":
            bw_idlist.append("8010")
        case "/Game/HouseAssets/Wallpaper/CobInnerWall/CobInnerWall.CobInnerWall":
            bw_idlist.append("13095")
        case "/Game/HouseAssets/Wallpaper/CountryInteriorWall/CountryInteriorWall.CountryInteriorWall":
            bw_idlist.append("7131")
        case "/Game/HouseAssets/Wallpaper/EerieWallpaper/EerieWallpaper.EerieWallpaper":
            bw_idlist.append("8829")
        case "/Game/HouseAssets/Wallpaper/EggstravagantInteriorWall/EggstravagantInteriorWall.EggstravagantInteriorWall":
            bw_idlist.append("17033")
        case "/Game/HouseAssets/Wallpaper/EulmoranInnerWall/EulmoranInnerWall.EulmoranInnerWall":
            bw_idlist.append("28126")
        case "/Game/HouseAssets/Wallpaper/FactoryInteriorWall/FactoryInteriorWall.FactoryInteriorWall":
            bw_idlist.append("30378")
        case "/Game/HouseAssets/Wallpaper/FlameInteriorWall/FlameInteriorWall.FlameInteriorWall":
            bw_idlist.append("7135")
        case "/Game/HouseAssets/Wallpaper/FortempsManorInteriorWall/FortempsManorInteriorWall.FortempsManorInteriorWall":
            bw_idlist.append("17032")
        case "/Game/HouseAssets/Wallpaper/GarleanConcreteInnerWall/GarleanConcreteInnerWall.GarleanConcreteInnerWall":
            bw_idlist.append("35809")
        case "/Game/HouseAssets/Wallpaper/GladeFloraInteriorWall/GladeFloraInteriorWall.GladeFloraInteriorWall":
            bw_idlist.append("8008")
        case "/Game/HouseAssets/Wallpaper/GladeInteriorWall/GladeInteriorWall.GladeInteriorWall":
            bw_idlist.append("6456")
        case "/Game/HouseAssets/Wallpaper/GoldenKasamatsuInteriorWall/GoldenKasamatsuInteriorWall.GoldenKasamatsuInteriorWall":
            bw_idlist.append("24185")
        case "/Game/HouseAssets/Wallpaper/GoldenUpholsteredInteriorWall/GoldenUpholsteredInteriorWall.GoldenUpholsteredInteriorWall":
            bw_idlist.append("24184")
        case "/Game/HouseAssets/Wallpaper/GoldLeafInteriorWall/GoldLeafInteriorWall.GoldLeafInteriorWall":
            bw_idlist.append("20717")
        case "/Game/HouseAssets/Wallpaper/HannishInteriorWall/HannishInteriorWall.HannishInteriorWall":
            bw_idlist.append("39429")
        case "/Game/HouseAssets/Wallpaper/HighlandInteriorWall/HighlandInteriorWall.HighlandInteriorWall":
            bw_idlist.append("36887")
        case "/Game/HouseAssets/Wallpaper/HinganInteriorWall/HinganInteriorWall.HinganInteriorWall":
            bw_idlist.append("20716")
        case "/Game/HouseAssets/Wallpaper/HouseBorelInteriorWall/HouseBorelInteriorWall.HouseBorelInteriorWall":
            bw_idlist.append("21867")
        case "/Game/HouseAssets/Wallpaper/LeveilleurEstateInteriorWall/LeveilleurEstateInteriorWall.LeveilleurEstateInteriorWall":
            bw_idlist.append("38674")
        case "/Game/HouseAssets/Wallpaper/LilyHillsInteriorWall/LilyHillsInteriorWall.LilyHillsInteriorWall":
            bw_idlist.append("17989")
        case "/Game/HouseAssets/Wallpaper/MasonworkInteriorWall/MasonworkInteriorWall.MasonworkInteriorWall":
            bw_idlist.append("8831")
        case "/Game/HouseAssets/Wallpaper/MetalInteriorWall/MetalInteriorWall.MetalInteriorWall":
            bw_idlist.append("7137")
        case "/Game/HouseAssets/Wallpaper/MGSInteriorWall/MGSInteriorWall.MGSInteriorWall":
            bw_idlist.append("10345")
        case "/Game/HouseAssets/Wallpaper/MoogleInteriorWall/MoogleInteriorWall.MoogleInteriorWall":
            bw_idlist.append("7140")
        case "/Game/HouseAssets/Wallpaper/MosaicInteriorWall/MosaicInteriorWall.MosaicInteriorWall":
            bw_idlist.append("8012")
        case "/Game/HouseAssets/Wallpaper/OasisFloraInteriorWall/OasisFloraInteriorWall.OasisFloraInteriorWall":
            bw_idlist.append("8009")
        case "/Game/HouseAssets/Wallpaper/OasisInteriorWall/OasisInteriorWall.OasisInteriorWall":
            bw_idlist.append("6457")
        case "/Game/HouseAssets/Wallpaper/PalaceOfTheDeadInteriorWall/PalaceOfTheDeadInteriorWall.PalaceOfTheDeadInteriorWall":
            bw_idlist.append("16015")
        case "/Game/HouseAssets/Wallpaper/RivieraFloraInteriorWall/RivieraFloraInteriorWall.RivieraFloraInteriorWall":
            bw_idlist.append("8007")
        case "/Game/HouseAssets/Wallpaper/RivieraInteriorWall/RivieraInteriorWall.RivieraInteriorWall":
            bw_idlist.append("6455")
        case "/Game/HouseAssets/Wallpaper/RoughStoneInteriorWall/RoughStoneInteriorWall.RoughStoneInteriorWall":
            bw_idlist.append("28960")
        case "/Game/HouseAssets/Wallpaper/SerpentInteriorWall/SerpentInteriorWall.SerpentInteriorWall":
            bw_idlist.append("7134")
        case "/Game/HouseAssets/Wallpaper/Solid-brickInteriorWall/Solid-brickInteriorWall.Solid-brickInteriorWall":
            bw_idlist.append("22530")
        case "/Game/HouseAssets/Wallpaper/SpottedInteriorWall/SpottedInteriorWall.SpottedInteriorWall":
            bw_idlist.append("9766")
        case "/Game/HouseAssets/Wallpaper/StainedCrystalInteriorWall/StainedCrystalInteriorWall.StainedCrystalInteriorWall":
            bw_idlist.append("10346")
        case "/Game/HouseAssets/Wallpaper/StarlightInteriorWall/StarlightInteriorWall.StarlightInteriorWall":
            bw_idlist.append("8830")
        case "/Game/HouseAssets/Wallpaper/StoneInteriorWall/StoneInteriorWall.StoneInteriorWall":
            bw_idlist.append("7132")
        case "/Game/HouseAssets/Wallpaper/StormBlueInteriorWall/StormBlueInteriorWall.StormBlueInteriorWall":
            bw_idlist.append("33248")
        case "/Game/HouseAssets/Wallpaper/StormInteriorWall/StormInteriorWall.StormInteriorWall":
            bw_idlist.append("7133")
        case "/Game/HouseAssets/Wallpaper/StripedInteriorWall/StripedInteriorWall.StripedInteriorWall":
            bw_idlist.append("8011")
        case "/Game/HouseAssets/Wallpaper/Sultana_sBreathInteriorWall/Sultana_sBreathInteriorWall.Sultana_sBreathInteriorWall":
            bw_idlist.append("17990")
        case "/Game/HouseAssets/Wallpaper/TiledInteriorWall/TiledInteriorWall.TiledInteriorWall":
            bw_idlist.append("7136")
        case "/Game/HouseAssets/Wallpaper/TopmastInteriorWall/TopmastInteriorWall.TopmastInteriorWall":
            bw_idlist.append("17988")
        case "/Game/HouseAssets/Wallpaper/UnfinishedInteriorWall/UnfinishedInteriorWall.UnfinishedInteriorWall":
            bw_idlist.append("23902")
        case "/Game/HouseAssets/Wallpaper/VariedWoodInteriorWall/VariedWoodInteriorWall.VariedWoodInteriorWall":
            bw_idlist.append("32254")
        case "/Game/HouseAssets/Wallpaper/WalnutInteriorWall/WalnutInteriorWall.WalnutInteriorWall":
            bw_idlist.append("27268")
        case "/Game/HouseAssets/Wallpaper/WavyInteriorWall/WavyInteriorWall.WavyInteriorWall":
            bw_idlist.append("9767")
        case "/Game/HouseAssets/Wallpaper/WhiteInteriorWall/WhiteInteriorWall.WhiteInteriorWall":
            bw_idlist.append("17034")




#########################################################################################################################################

### DUPLICATE ITEM HANDLER


for i in inside_furniturelistData:
    if i not in counter:
        counter[i] = 0
    counter[i] += 1

if thinkmode == 1:
    print("")
    #time.sleep(speed)
    print("Inside furniture tally complete!")

if thinkmode == 1:
    print("")
    #time.sleep(speed)
    print("Removing null fixtures and furnishings...")

inside_fixturelistData.remove(0)

if thinkmode == 1:
    print("")
    #time.sleep(speed)
    print("No more null fixtures or furnishings!!")

for i in inside_fixturelistData:
    if i != 0:
        if i not in counter:
            counter[i] = 0
        counter[i] += 1

if thinkmode == 1:
    print("")
    #time.sleep(speed)
    print("Inside fixture tally complete!")

if houseSize != "Apartment":
    for i in outside_furniturelistData:
        if i not in counter:
            counter[i] = 0
        counter[i] += 1

if thinkmode == 1:
    print("")
    #time.sleep(speed)
    print("Outside furniture tally complete!")

if houseSize != "Apartment":
    for i in outside_fixturelistData:
        if i != 0:
            if i not in counter:
                counter[i] = 0
            counter[i] += 1

if thinkmode == 1:
    print("")
    #time.sleep(speed)
    print("Outside fixture tally complete!")

for i in dyeID:
    if i not in counter:
        counter[i] = 0
    counter[i] += 1

if thinkmode == 1:
    print("")
    #time.sleep(speed)
    print("Dye tally complete!")

for i in bw_idlist:
    if i not in counter:
        counter[i] = 0
    counter[i] += 1

if thinkmode == 1:
    print("")
    #time.sleep(speed)
    print("Extra wall tally complete!")

dictionary = dict(counter)
iterator = 0

dictIDs = list(dictionary.keys())
dictVals = list(dictionary.values())

#########################################################################################################################################


for i in dictIDs:
    furniturelistfull.append(str(dictIDs[iterator]))
    furniturelistfull.append(",null,")
    furniturelistfull.append(str(dictVals[iterator]))
    furniturelistfull.append(";")
    iterator += 1
    if thinkmode == 1:
        print("")
        #time.sleep(speed)
        print(i)


iterator = 0

if thinkmode == 1:
    print("")
    #time.sleep(speed)
    print("Cleaning up!")
    #time.sleep(speed)

furniturelistfull.pop(-1)
pre_encoded_string = ''.join(furniturelistfull)

if thinkmode == 1:
    print("")
    #time.sleep(speed)
    print(f"Preincoded string: {pre_encoded_string}")
    print("")


encoded = base64.b64encode(pre_encoded_string.encode('utf-8'))

encoded_string = str(encoded)

if thinkmode == 1:
    #time.sleep(speed)
    print(f"Your encoded string is: {encoded_string}")
    print("")

final = str(url + encoded_string)
final = remove1st(final, "b'")
final = final[:-1]


print("")
#time.sleep(speed)
print(final)
print("")
#time.sleep(speed)
browser.open(final)
print("Made with love by Petra!")
print("https://deafbun.carrd.co")