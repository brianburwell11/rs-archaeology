"""Functions that get specific data from Third Party APIs"""

from requests import get


def get_ge_value(id):
    """Gets the current Grand Exchange value of an item

    Parameters
    ----------
    id : str
        The in-game ID of an item

    Returns
    -------
    int
        The median value of the item on the Grand Exchange
    """

    r = get("https://api.weirdgloop.org/exchange/history/rs/latest", params={"id": id})

    data = r.json()
    if data.get("error", False):
        return None

    return list(data.items())[0][1].get("price")


def get_image_url(id):
    """Gets the URL of the image for an object from Runescape's API

    This can be set as the `src` of an `img` element in HTML

    Parameters
    ----------
    id : int
        The in-game ID of an item

    Returns
    -------
    str
        The URL of the image
    """

    r = get(f"https://secure.runescape.com/m=itemdb_rs/obj_big.gif", {"id": id})
    if r.status_code == 404:
        return None
    else:
        return r.url


def get_NPC_image_url(name):
    """Gets the chathead image of an NPC

    Parameters
    ----------
    name : str
        The in-game name of the NPC

    Returns
    -------
    str
        The URL of the image

    Notes
    ------
    Buggy and not guaranteed
    """

    r = get(f'https://runescape.wiki/images/{name.replace(" ","_")}_chathead.png')
    if r.status_code == 404:
        return None
    else:
        return r.url
