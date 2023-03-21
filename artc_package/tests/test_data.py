#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import artc_package.data as apackage


def test_get_winnipeg_transit_passups_data():
    transit_passups_data = apackage.get_winnipeg_transit_passups_data()
    assert transit_passups_data.shape[0] > 0, "ERROR: No data returned."
    assert all(
        transit_passups_data.columns
        == [
            "pass_up_id",
            "pass_up_type",
            "time",
            "route_number",
            "route_name",
            "route_destination",
            "location",
        ]
    ), "ERROR: Missmatching columns in the data."


def test_get_winnipeg_air_quality_data():
    air_quality_data = apackage.get_winnipeg_air_quality_data()
    assert air_quality_data.shape[0] > 0, "ERROR: No data returned."
    assert all(
        air_quality_data.columns
        == [
            "observationid",
            "observationtime",
            "thingid",
            "locationname",
            "measurementtype",
            "measurementvalue",
            "measurementunit",
            "location",
            "point",
        ]
    ), "ERROR: Missmatching columns in the data."


def test_get_winnieg_parks_and_open_space_data():
    parks_and_open_space_data = apackage.get_winnieg_parks_and_open_space_data()
    assert parks_and_open_space_data.shape[0] > 0, "ERROR: No data returned."
    assert all(
        parks_and_open_space_data.columns
        == [
            "park_id",
            "park_name",
            "address",
            "location_description",
            "park_category",
            "linear_park_system",
            "district",
            "neighbourhood",
            "electoral_ward",
            "cca",
            "area_in_hectares",
            "water_area_in_hectares",
            "land_area_in_hectares",
            "location",
            "polygon",
        ]
    ), "ERROR: Missmatching columns in the data."
