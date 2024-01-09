import os.path
import xml.etree.ElementTree as ET

process = "IntelliJ IDEA.app"

def adjustFont(size):
    jetBrainsPath = os.path.expanduser("~") + "/Library/Application Support/JetBrains/"

    if os.path.exists(jetBrainsPath) == False:
        raise FileNotFoundError("JetBrains dir not found")

    intellijDirName = list(sorted(filter(lambda name: name.startswith("IntelliJIdea"), os.listdir(jetBrainsPath))))[-1]
    optionsPath = jetBrainsPath + intellijDirName + "/options"

    if os.path.exists(optionsPath) == False:
        raise FileNotFoundError("IntelliJIdea options dir not found")

    editorFontPath = optionsPath + "/editor-font.xml"
    otherFontPath = optionsPath + "/other.xml"

    if os.path.exists(editorFontPath) == False:
        raise FileNotFoundError("IntelliJIdea editor-font.xml not found")

    if os.path.exists(otherFontPath) == False:
        raise FileNotFoundError("IntelliJIdea other.xml not found")

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
    print("IntelliJIdea: editor-font.xml updated")

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

    print("IntelliJIdea: other.xml updated")
