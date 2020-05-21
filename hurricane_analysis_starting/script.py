# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# write your update damages function here:
def update_damages(damages):
    """
    Convert list of values to float values
    :param damages: list of values to convert
    :return: List of values as floats
    :rtype: list
    """
    convert_prefix = {
        "M": 1000000,
        "B": 1000000000
    }

    new_damages = []

    for damage in damages:
        if damage == "Damages not recorded":
            new_damages.append(damage)
        else:
            new_damages.append(convert_prefix[damage[-1]] * float(damage[:-1]))

    return new_damages


# Test update_damages()
# print(update_damages(damages))


# write your construct hurricane dictionary function here:
def construct_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    """
    Creates a dictionary about hurricane information
    :param names: names of the hurricanes
    :param months: months in which the hurricanes occurred
    :param years: years in which the hurricanes occurred
    :param max_sustained_winds: maximum sustained winds (miles per hour) of the hurricanes
    :param areas_affected:  list of different areas affected by each of the hurricanes
    :param damages: list of damages in USD of each hurricane
    :param deaths: list of deaths from each hurricane
    :return: dictionary of hurricane information
    :rtype: dict
    """
    hurricane_info = {}
    updated_damages_lst = update_damages(damages)

    for i in range(34):
        hurricane_info[names[i]] = {
            "Name": names[i],
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": max_sustained_winds[i],
            "Areas Affected": areas_affected[i],
            "Damage": updated_damages_lst[i],
            "Deaths": deaths[i]
        }

    return hurricane_info


# Test construct_dict()
# print(construct_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths))

# write your construct hurricane by year dictionary function here:
def construct_dict_by_year(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    """
    Creates a dictionary about hurricane information by year
    :param names: names of the hurricanes
    :param months: months in which the hurricanes occurred
    :param years: years in which the hurricanes occurred
    :param max_sustained_winds: maximum sustained winds (miles per hour) of the hurricanes
    :param areas_affected:  list of different areas affected by each of the hurricanes
    :param damages: list of damages in USD of each hurricane
    :param deaths: list of deaths from each hurricane
    :return: dictionary of hurricane information by year
    :rtype: dict
    """
    hurricane_info_by_year = {}
    updated_damages_lst = update_damages(damages)

    for i in range(34):
        if years[i] in hurricane_info_by_year.keys():
            current_value = hurricane_info_by_year[years[i]]
            current_value.append(
                {
                    "Name": names[i],
                    "Month": months[i],
                    "Year": years[i],
                    "Max Sustained Wind": max_sustained_winds[i],
                    "Areas Affected": areas_affected[i],
                    "Damage": updated_damages_lst[i],
                    "Deaths": deaths[i]
                })
            hurricane_info_by_year[years[i]] = current_value
        else:
            hurricane_info_by_year[years[i]] = [{
                "Name": names[i],
                "Month": months[i],
                "Year": years[i],
                "Max Sustained Wind": max_sustained_winds[i],
                "Areas Affected": areas_affected[i],
                "Damage": updated_damages_lst[i],
                "Deaths": deaths[i]
            }]

    return hurricane_info_by_year


# Test construct_dict_by_year()
# print(construct_dict_by_year(names, months, years, max_sustained_winds, areas_affected, damages, deaths))

# write your count affected areas function here:
def affected_areas(areas_affected):
    """
    Creates dict of count of areas affected by area
    :param areas_affected: list of areas affected
    :return: dict of area affected with number of times affected
    :rtype: dict
    """
    areas_affected_count = {}

    for areas in areas_affected:
        for area in areas:
            if area in areas_affected_count.keys():
                areas_affected_count[area] += 1
            else:
                areas_affected_count[area] = 1

    return areas_affected_count


# Test affected_areas()
# print(affected_areas(areas_affected))

# write your find most affected area function here:


# write your greatest number of deaths function here:


# write your categorize by mortality function here:


# write your greatest damage function here:


# write your categorize by damage function here:
