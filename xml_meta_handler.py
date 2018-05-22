import re


def handle_xml_meta(xml): #passed in a list of matches that are/should be xml strings
    meta_touples = {"": ""}
    dupes = []

    for i in xml:
        #parser_regex = r"(?:.*?:)(.*?=\".*?\")"
        #parser_regex = r"(?:.*?:)(.*?)(?:=\")(.*?)(?:\")" # dictionary
        #parser_regex = r"(?:.*?:.*?:|:.*?:|.*?:)(.*?)(?:=\")(.*?)(?:\")" # dictionary
        parser_regex = r"(?::)(\w+)(?:=\")(.*?)(?=\")" # dictionary

        for j in re.findall(parser_regex, i):
            if j not in dupes:
                meta_touples.update({j[0]:j[1]})
                #print(j)

                #meta_touples.update({j[1]:j[2]})
                dupes.append(j)

    return meta_touples
