import os.path
import xml.etree.ElementTree as ET

process = "Android Studio.app"

def adjustFont(size):
    googlePath = os.path.expanduser("~") + "/Library/Application Support/Google/"

    if os.path.exists(googlePath) == False:
        raise FileNotFoundError("Android Studio dir not found")

    androidStudioDirName = list(sorted(filter(lambda name: name.startswith("AndroidStudio"), os.listdir(googlePath))))[-1]
    optionsPath = googlePath + androidStudioDirName + "/options"

    if os.path.exists(optionsPath) == False:
        raise FileNotFoundError("Android Studio options dir not found")

    editorFontPath = optionsPath + "/editor-font.xml"
    otherFontPath = optionsPath + "/other.xml"

    if os.path.exists(editorFontPath) == False:
        raise FileNotFoundError("Android Studio editor-font.xml not found")

    if os.path.exists(otherFontPath) == False:
        raise FileNotFoundError("Android Studio other.xml not found")

    editorFontFile = open(editorFontPath, "r")
    editorFontXmlR = ET.fromstringlist(editorFontFile.readlines())
    editorFontFile.close()

    font_size_option = editorFontXmlR.find('.//component/option[@name="FONT_SIZE"]')
    font_size_option2d = editorFontXmlR.find('.//component/option[@name="FONT_SIZE_2D"]')

    if font_size_option is None:
        font_size_option = ET.SubElement(editorFontXmlR.find('.//component'), 'option')
        font_size_option.set('name', 'FONT_SIZE')

    if font_size_option2d is None:
        font_size_option2d = ET.SubElement(editorFontXmlR.find('.//component'), 'option')
        font_size_option2d.set('name', 'FONT_SIZE_2D')

    font_size_option.set('value', str(size))
    font_size_option2d.set('value', str(size))

    xml = ET.tostring(editorFontXmlR, encoding='utf-8').decode('utf-8')

    editorFontFile = open(editorFontPath, 'w')
    editorFontFile.write(xml)
    editorFontFile.close()
    print("Android Studio: editor-font.xml updated")

    otherFontFile = open(otherFontPath, 'r')
    otherXmlRoot = ET.fromstringlist(otherFontFile.readlines())
    otherFontFile.close()

    notRoamableUiSettingsXml = otherXmlRoot.find('.//component[@name="NotRoamableUiSettings"]')
    otherFontSizeXml = notRoamableUiSettingsXml.find('option[@name="fontSize"]')

    if otherFontSizeXml is None:
        otherFontSizeXml = ET.SubElement(notRoamableUiSettingsXml, 'option')
        otherFontSizeXml.set('name', 'fontSize')

    otherFontSizeXml.set('value', str(size))

    with open(otherFontPath, 'w') as file:
        file.write(ET.tostring(otherXmlRoot, encoding='utf-8').decode('utf-8'))

    print("Android Studio: other.xml updated")
