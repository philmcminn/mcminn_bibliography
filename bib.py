from enum import Enum

Venue = Enum(
    "Venue",
    ["BOOK_CHAPTER", "CONFERENCE", "JOURNAL", "PHD_THESIS", "TECH_REPORT", "WORKSHOP"],
)


def add_pub(bib, key, pub):
    if key in bib:
        print('"' + key + '" already in bib')
        quit()
    bib[key] = pub


def get_years(bib):
    years = {inner_dict["year"] for inner_dict in bib.values() if "year" in inner_dict}
    return sorted(years, reverse=True)


def get_pubs_in_year(bib, year):
    filtered_pubs = {
        key: pub for key, pub in bib.items() if year == pub['year']
    }

    sorted_pubs = dict(
        sorted(
            filtered_pubs.items(),
            key=lambda x: (
                x[1]['author'][0][0],
                x[1]['author'][0][1]
            )
        )
    )

    return sorted_pubs


def count_venue_type(bib, venue_type):
    filtered_entries = filter(
        lambda pub: isinstance(pub, dict)
        and "venue" in pub
        and "type" in pub["venue"]
        and pub["venue"]["type"] == venue_type,
        bib.values(),
    )
    count = len(list(filtered_entries))
    return count


def get_pub_by_gsid(bib, gsid):
    for key, pub in bib.items():
        if "gsid" in pub and pub["gsid"] == gsid:
            return pub
    return None


def get_pubs_with_tag(bib, tag):
    filtered_pubs = {
        key: pub for key, pub in bib.items() if tag in pub['tags']
    }

    sorted_pubs = dict(
        sorted(
            filtered_pubs.items(),
            key=lambda x: (
                -x[1]['year'],
                x[1]['author'][0][0],
                x[1]['author'][0][1]
            )
        )
    )

    return sorted_pubs
