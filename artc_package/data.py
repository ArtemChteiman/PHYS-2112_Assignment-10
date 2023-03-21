import os
import pandas as pd

from urllib.request import urlretrieve

WINNIPEG_TRANSIT_PASSUP_URL = "https://data.winnipeg.ca/resource/mer2-irmb.csv"
WINNIPEG_AIR_QUALITY_URL = "https://data.winnipeg.ca/resource/f58p-2ju3.csv"
WINNIEG_PARKS_AND_OPEN_SPACE_DATA = "https://data.winnipeg.ca/resource/tx3d-pfxq.csv"


def get_winnipeg_transit_passups_data(
    filename="mer2-irmb.csv", url=WINNIPEG_TRANSIT_PASSUP_URL, force_download=False
):
    """
    filename : string (optinal)
        name/location of the file to be saved.
    url : string (optional)
        web location of the data to be downloaded from.
    force_download : bool (optional)
        if True, force redownload the data.
    Returns
        data : pandas.DataFrame
            reading an CSV file and returns it as data.
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv("mer2-irmb.csv", parse_dates=True)
    return data


def get_winnipeg_air_quality_data(
    filename="f58p-2ju3.csv", url=WINNIPEG_AIR_QUALITY_URL, force_download=False
):
    """
    filename : string (optinal)
        name/location of the file to be saved.
    url : string (optional)
        web location of the data to be downloaded from.
    force_download : bool (optional)
        if True, force redownload the data.
    Returns
        data : pandas.DataFrame
            reading an CSV file and returns it as data.
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv("f58p-2ju3.csv", parse_dates=True)
    return data


def get_winnieg_parks_and_open_space_data(
    filename="tx3d-pfxq.csv",
    url=WINNIEG_PARKS_AND_OPEN_SPACE_DATA,
    force_download=False,
):
    """
    filename : string (optinal)
        name/location of the file to be saved.
    url : string (optional)
        web location of the data to be downloaded from.
    force_download : bool (optional)
        if True, force redownload the data.
    Returns
        data : pandas.DataFrame
            reading an CSV file and returns it as data.
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv("tx3d-pfxq.csv", parse_dates=True)
    return data
