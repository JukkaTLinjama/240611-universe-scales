#converters.py  v0.2    12.6.2024

import math

#### funtion definitions:
#  user_units  and _engineering_units

def convert_to_user_units(distance):
    """  ver 20240610 
    Convert the given distance into user-defined units using a logarithmic scale,
    and return a formatted string with the number and its units. If no suitable unit is found,
    the distance is returned in meters in scientific notation.

    :param distance: Distance in meters (float or string in scientific notation)
    :return: Formatted string with the distance and its unit
    """
    # User units list with conversion functions
    units_list = [
        ('Atom nuclei', lambda meters: meters / 2e-15),
        ('Atom diameters', lambda meters: meters / 5e-10),
        ('picometers', lambda meters: meters * 1e12),
        ('micrometers', lambda meters: meters * 1e6),
        ('millimeters', lambda meters: meters * 1000),
        ('meters', lambda meters: meters),
        ('kilometers', lambda meters: meters / 1000),
        ('Earth diameters', lambda meters: meters / 12700e3),
        ('M km', lambda meters: meters / 1e9),
        ('Sun diameters', lambda meters: meters / 1.391e6),
        ('AU', lambda meters: meters / 149.5e9),
        ('light years', lambda meters: meters / 9.461e15),
        ('Galaxy diameters', lambda meters: meters / 2e21),
        ('M light years', lambda meters: meters / 9.461e21),
        ('B light years', lambda meters: meters / 9.461e24)
    ]

    # Convert input to float
    distance = float(distance)

    # Determine the most reasonable unit using logarithmic differences
    best_unit = None
    best_value = None
    minimum_log_diff = float('inf')
    for unit, conversion_function in units_list:
        converted_value = conversion_function(distance)
        log_diff_from_one = abs(math.log10(converted_value) - math.log10(1)) # log difference from given units
        #  limits for acceptable presentation in decimals:
        if 0.01 <= converted_value < 10000 and log_diff_from_one < minimum_log_diff:
            best_unit = unit
            best_value = converted_value
            minimum_log_diff = log_diff_from_one

    return f"{best_value:.3g} {best_unit}" if best_unit else f"{distance:.3e} m"
    
# ---------------------------------------------

def convert_to_engineering_units(distance):
    """ ver 20240610
    Convert the given distance into engineering units with reference decades using a logarithmic scale,
    and return a formatted string with the number and its units. If no suitable unit is found,
    the distance is returned in meters in scientific notation.

    :param distance: Distance in meters (float or string in scientific notation)
    :return: Formatted string with the distance and its unit
    """
    # Units list with conversion functions, targeted for engineering scales with reference decades
    units_list = [
        ('zeptometers (-21)', lambda meters: meters * 1e21),
        ('attometers (-18)', lambda meters: meters * 1e18),
        ('femtometers (-15)', lambda meters: meters * 1e15),
        ('picometers (-12)', lambda meters: meters * 1e12),
        ('nanometers (-9)', lambda meters: meters * 1e9),
        ('micrometers (-6)', lambda meters: meters * 1e6),
        ('millimeters (-3)', lambda meters: meters * 1000),
        ('meters (0)', lambda meters: meters),
        ('kilometers (+3)', lambda meters: meters / 1000),
        ('Megameters (+6)', lambda meters: meters / 1e6),
        ('Gigameters (+9)', lambda meters: meters / 1e9),
        ('Terameters (+12)', lambda meters: meters / 1e12),
        ('Petameters (+15)', lambda meters: meters / 1e15),
        ('Exameters (+18)', lambda meters: meters / 1e18),
        ('Zettameters (+21)', lambda meters: meters / 1e21)
    ]

    # Convert input to float
    distance = float(distance)

    # Determine the most reasonable unit using logarithmic differences
    best_unit = None
    best_value = None
    minimum_log_diff = float('inf')
    for unit, conversion_function in units_list:
        converted_value = conversion_function(distance)
        log_diff_from_one = abs(math.log10(converted_value) - math.log10(1))
        # limits for decimal presentation
        if 0.01 <= converted_value < 1000 and log_diff_from_one < minimum_log_diff:
            best_unit = unit
            best_value = converted_value
            minimum_log_diff = log_diff_from_one

    return f"{best_value:.3g} {best_unit}" if best_unit else f"{distance:.3e} m"
    
""" Example usage
distance_m = 1e-9  # 1 nanometer
print(convert_to_engineering_units(distance_m))  # Convert to engineering unit with reference decade
"""