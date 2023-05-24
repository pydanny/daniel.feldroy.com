import csv

content = """---
title: Travels of Daniel Roy Greenfeld"
description: "My location in the present, future, and past"
author: "Daniel Roy Greenfeld"
image: /images/future-office.png
og_url: https://daniel.feldroy.com/travels
---
"""

current = []
future = []
past = []

with open('travels.csv') as f:
    for travel in csv.DictReader(f):
        match travel['status']:
           case "current":
                current.append(travel)
           case "past":
                past.append(travel)
           case "future":
                future.append(travel)

    past = sorted(past, key=lambda x: x["city"].lower())

    # print("current", current)
    # print("future", future)
    # print("past", past)


def write_status(status, travels):
    result = f"\n\n# {status.title()}\n\n"
    for travel in travels:
        if travel['event'].strip():
            event = f", {travel['event']}"
        else:
            event = ""
            
        if travel['link'].strip():
            result += f"- {travel['city']}, {travel['country']} [{event}]({travel['link']})"
        else:
            result += f"- {travel['city']}, {travel['country']} {event}"
        result += "\n"
    return result

content += write_status("current", current)
content += write_status("future", future)
content += write_status("past", past)
with open("pages/travels.mdoc", "w") as f:
    f.write(content)

