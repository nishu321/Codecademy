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
    hurricanes = {}
    updated_damages_lst = update_damages(damages)

    for i in range(34):
        hurricanes[names[i]] = {
            "Name": names[i],
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": max_sustained_winds[i],
            "Areas Affected": areas_affected[i],
            "Damage": updated_damages_lst[i],
            "Deaths": deaths[i]
        }

    return hurricanes


# Test construct_dict()
# print(construct_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths))
hurricanes = construct_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)


# write your construct hurricane by year dictionary function here:
def construct_dict_by_year(hurricane_dict):
    """
    Creates a dictionary about hurricane information by year
    :param hurricane_dict: dict of hurricanes information
    :return: a dict of year and every hurricane that occurred during that year
    :rtype: dict
    """
    hurricane_info_by_year = {}

    for hurricane, hurricane_info in hurricane_dict.items():
        if hurricane_info["Year"] in hurricane_info_by_year:
            hurricane_info_by_year[hurricane_info["Year"]].append(hurricane_info)
        else:
            hurricane_info_by_year[hurricane_info["Year"]] = [hurricane_info]

    return hurricane_info_by_year


# Test construct_dict_by_year()
# print(construct_dict_by_year(hurricanes))


# write your count affected areas function here:
def affected_areas(hurricane_dict):
    """
    Counts the number of times each area has been affected
    :param hurricane_dict: dict of hurricanes information
    :return: dict of areas and count of how many times they were affected
    :rtype: dict
    """
    areas_affected_count = {}

    for hurricane, hurricane_info in hurricane_dict.items():
        for area in hurricane_info['Areas Affected']:
            if area in areas_affected_count.keys():
                areas_affected_count[area] += 1
            else:
                areas_affected_count[area] = 1

    return areas_affected_count


# Test affected_areas()
# print(affected_areas(hurricanes))


# write your find most affected area function here:
def most_affected_area(affected_area_dict):
    """
    Find the area most affected by hurricanes
    :param affected_area_dict: dict of areas and count of how often they were affected
    :return: string of area and its count that was most affected
    :rtype: STR
    """
    max_count = 0
    max_area = None

    for area, affected_count in affected_area_dict.items():
        if affected_count > max_count:
            max_count = affected_count
            max_area = area

    return "The area of {0} was affected {1} times by hurricanes.".format(max_area, max_count)


# Test most_affected_area()
# print(most_affected_area(affected_areas(hurricanes)))

# write your greatest number of deaths function here:
def greatest_deaths(hurricane_dict):
    """
    Find hurricane which caused most deaths
    :param hurricane_dict: dict of hurricanes information
    :return: string of hurricane and number of deaths caused by hurricane
    :rtype: STR
    """
    max_death = 0
    max_hurricane = None

    for hurricane, hurricane_info in hurricane_dict.items():
        if hurricane_info["Deaths"] > max_death:
            max_death = hurricane_info["Deaths"]
            max_hurricane = hurricane

    return "Hurricane {0} caused {1} deaths.".format(max_hurricane, max_death)


# Test greatest_deaths()
# print(greatest_deaths(hurricanes))

# write your categorize by mortality function here:
def mortality(hurricane_dict):
    """
    Creates a new dict with mortality scale as key and value as a list of dict of hurricanes
    :param hurricane_dict: dict of hurricanes information
    :return: Return dict of mortality and all hurricanes that belong to that mortality scale
    :rtype: dict
    """
    mortality_scale = {
        0: 0,
        1: 100,
        2: 500,
        3: 1000,
        4: 10000
    }

    mortality_dict = {}

    mortality_value = 0
    for hurricane, hurricane_info in hurricane_dict.items():
        for mortality, scale in mortality_scale.items():
            if hurricane_info["Deaths"] >= scale:
                mortality_value = mortality + 1
        if mortality_value in mortality_dict.keys():
            mortality_dict[mortality_value].append(hurricane_info)
        else:
            mortality_dict[mortality_value] = [hurricane_info]

    return mortality_dict


# Test greatest_deaths()
# print(mortality(hurricanes))


# write your greatest damage function here:
def greatest_damage(hurricane_dict):
    """
    Find hurricane that caused the most damages in dollars
    :param hurricane_dict: dict of hurricanes information
    :return: string of hurricane and amount of damages caused by hurricane
    :rtype: STR
    """
    max_damage = 0
    max_hurricane = None

    for hurricane, hurricane_info in hurricane_dict.items():
        if hurricane_info["Damage"] == "Damages not recorded":
            continue
        elif hurricane_info["Damage"] > max_damage:
            max_damage = hurricane_info["Damage"]
            max_hurricane = hurricane

    return "Hurricane {0} caused {1} dollars in damages.".format(max_hurricane, max_damage)


# Test greatest_damage()
# print(greatest_damage(hurricanes))

# write your categorize by damage function here:
def damage(hurricane_dict):
    """
    Create new dict with key as damage scale and value as list of dict hurricanes
    :param hurricane_dict: dict of hurricanes information
    :return: Return dict of damage scale and hurricanes that belong to that scale
    :rtype: dict
    """
    damage_scale = {
        0: 0,
        1: 100000000,
        2: 1000000000,
        3: 10000000000,
        4: 50000000000
    }

    damage_dict = {}

    damage_value = 0
    for hurricane, hurricane_info in hurricane_dict.items():
        if hurricane_info["Damage"] == "Damages not recorded":
            continue
        for scale, dollars in damage_scale.items():
            if hurricane_info["Damage"] >= dollars:
                damage_value = scale + 1
        if damage_value in damage_dict.keys():
            damage_dict[damage_value].append(hurricane_info)
        else:
            damage_dict[damage_value] = [hurricane_info]

    return damage_dict


# Test damage()
# print(damage(hurricanes))
