# Import python libraries here
import re

# Import third-party libraries
import numpy as np
from hdx.location.country import Country
from stdnum import isin, lei
from stdnum.gb import sedol


def validate_id(value, type_id='isin'):
    """
        Validates an official id. By default, the id type is isin.

        Parameters:
            value (string): the id to be validated
            type_id (string): defines the type of the identifier to be validated ('lei', 'isin' or 'sedol')
        Returns:
            np.nan : if the value is not a string, is null or have zero length
            True or False: the validity of the identifier
        Raises:
            NotImplementedError: if the type_id is not recognizable
    """

    if not isinstance(value, str):
        return np.nan

    if len(str(value).strip()) == 0:
        return np.nan

    # Remove spaces in the beginning and in the end and convert it to lower case
    value = value.strip().lower()

    # Remove excessive spaces in between words
    value = re.sub(r'\s+', ' ', value)

    if type_id == 'lei':
        return lei.is_valid(value)
    elif type_id == 'isin':
        return isin.is_valid(value)
    elif type_id == 'sedol':
        return sedol.is_valid(value)
    else:
        raise NotImplementedError


def get_name_from_alpha2(country):
    """
        Gets the name of a country given its alpha2 code.

        Parameters:
            country (string): the alpha2 code
        Returns:
            NaN (np.nan): if the alpha code was not found
            country_name (string): the name of the country
        Raises:
            No exception is raised.
    """

    country_name = Country.get_country_name_from_iso2(country, use_live=False)
    if not country_name:
        return None
    return country_name