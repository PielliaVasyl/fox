def get_direction_city_parameter(direction_title=None, city_title=None):
    direction_city_parameter = ''
    if direction_title:
        direction_city_parameter += 'direction-'
        direction_city_parameter += direction_title
        direction_city_parameter += '/'

    if city_title:
        direction_city_parameter += 'city-'
        direction_city_parameter += city_title
        direction_city_parameter += '/'
    return direction_city_parameter
