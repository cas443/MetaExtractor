import re


def handle_xml_meta(xml): #passed in a list of matches that are/should be xml strings
    meta_touples = {"": ""}
    dupes = []

    for i in xml:
        #parser_regex = r"(?:.*?:)(.*?=\".*?\")"
        #parser_regex = r"(?:.*?:)(.*?)(?:=\")(.*?)(?:\")" # dictionary
        #parser_regex = r"(?:.*?:.*?:|:.*?:|.*?:)(.*?)(?:=\")(.*?)(?:\")" # dictionary
        parser_regex = r"(?::)(\w+)(?:=\")(.*?)(?=\")" # dictionary

        between_tags = r"(?:>)(\w+.*?)(?:<)"
        lat_long_regex = r"(?:exif:)([A-Za-z0-9]+)(?:>.*?)([0-9. ]+[A-Z]+)(?:</)"
        gps_timestamp_regex = r"(?:exif:)([A-Za-z0-9]+)(?:>)([0-9. :]+)(?:</)"

        for j in re.findall(parser_regex, i):
            if j not in dupes and "" not in j:
                meta_touples.update({j[0]:j[1]})
                dupes.append(j)

        for j in re.findall(lat_long_regex, i):
            if j not in dupes:
                meta_touples.update({j[0]: j[1]})
                dupes.append(j)

        for j in re.findall(gps_timestamp_regex, i):
            if j not in dupes:
                meta_touples.update({j[0]: j[1]})
                dupes.append(j)

        # for j in re.findall(between_tags, i):
        #     if j not in dupes:
        #         meta_touples.update({j[0]: j[1]})
        #         dupes.append(j)

        if len(meta_touples) == 0: #fix this, it doesnt work
            print("[i] NO METADATA FROM XML AVAILABLE.")

    return meta_touples
