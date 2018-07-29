import re

def handle_meta(imgdata):

    if imgdata is "":
        return "[-] No metadata is available. Please try another image."

    print("[i] Length of image data BEFORE reduction: {}".format(len(imgdata)))

    #imgdata = re.sub(r"(?<=\\)(x[0-9A-Za-z]{2,5}\\)","", imgdata)
    imgdata = re.sub(r"(?<=\\)(x[0-9A-Za-z().*|\\^\"@+=\-/\[\]:;<>$&!?`#{}~ ]{2,6}\\)","", imgdata)

    print("[i] Length of image data AFTER reduction: {}".format(len(imgdata)))
    print(imgdata[:20000])


    extraction_regexes_XML = [
               r"(?::)(\w+)(?:=\")(.*?)(?=\")",
               r"(?::)(.*?)(?:>)(\w+.*?)(?:<)",
               r"(?:exif:)([A-Za-z0-9]+)(?:>)(.*?)(?:<)",
               r"(?:exif:)([A-Za-z0-9]+)(?:>)([0-9. :]+)(?:</)"]
    extraction_regexes_ORD = [r"(?<=\\x[0-9A-Za-z]{2})([A-Za-z0-9 ]{1}[A-Za-z0-9 .:#-/]{3,150})(?=\\x)"]

    meta_matches_XML_DICT = {}
    meta_matches_ORD_LIST = []

    duplicates = []

    for i in extraction_regexes_XML:

        curr = re.findall(i, imgdata)

        for j in curr:
            if j not in duplicates and type(j) is tuple and j[1] is not "" and "\n" not in j and len(j[0]) < 100 and len(j[1]) < 150 and "\\x" not in j[0] and "\\x" not in j[1]:
                meta_matches_XML_DICT.update({j[0] : j[1]})
                duplicates.append(j[0])
                duplicates.append(j[1])


    for i in extraction_regexes_ORD:

        curr = re.findall(i, imgdata)

        for j in curr:

            match = re.search(r"([A-Za-z0-9 .:/-]{5,150})", i)

            if j not in duplicates and j is not "" and "   " not in j and "bool" not in match.group(0):
                meta_matches_ORD_LIST.append(j)
                duplicates.append(j)

    #meta_matches_ORD_LIST.sort(key=len, reverse=True)


    print("Length of meta_matches_XML: {}".format(len(meta_matches_XML_DICT)))
    print("Length of meta_matches_ORD: {}".format(len(meta_matches_ORD_LIST)))

    print(meta_matches_XML_DICT)

    return meta_matches_XML_DICT, meta_matches_ORD_LIST
