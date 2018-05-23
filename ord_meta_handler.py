import re

def handle_meta(imgdata):
    metadata_regex_ord = r"(?<=\\x[0-9A-Za-z]{2})([A-Za-z0-9 ]{1}[A-Za-z0-9 .:#-/]{3,150})(?=\\x)"
    dupes = []
    metadata_ord = []

    # FINDING ORDINARY METADATA IN IMAGE
    if re.findall(metadata_regex_ord, imgdata):
        for i in re.findall(metadata_regex_ord, imgdata):
            match = re.search(r"([A-Za-z0-9 .:/-]{5,150})", i)
            if match and match.group(0) not in dupes and "bool" not in match.group(0) and "long" not in match.group(
                    0) and not re.search(
                    r"([A-Z]{1,5}[a-z]{1,5}[A-Z]{1,5})|(.*\.|-$)|([A-Za-z]{1,5}[0-9]{1,5}[A-Za-z]{1,5})|([0-9]{1,5}[A-Za-z]{1,5})",
                    match.group(0)):
                metadata_ord.append(match.group(0))
                dupes.append(match.group(0))
    metadata_ord.sort(key=len, reverse=True)

    return metadata_ord
