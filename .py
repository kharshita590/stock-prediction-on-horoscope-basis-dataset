# import pandas as pd
# import numpy as np 

# df=pd.read_csv("r.csv")
# df=df.drop(['state_code', 'state_name', 'dist_code', 'population_total', 'population_male', 'population_female', '0-6_population_total', '0-6_population_male', '0-6_population_female', 'literates_total', 'literates_male', 'literates_female', 'sex_ratio', 'child_sex_ratio', 'effective_literacy_rate_total', 'effective_literacy_rate_male', 'effective_literacy_rate_female', 'location', 'total_graduates', 'male_graduates', 'female_graduates'],axis=1)
# df.to_csv("f.csv",index=False)

# import random
# import pandas as pd
# df = pd.read_csv("main_data.csv")
# def generate_time():
#     hour = random.randint(0, 23)
#     minute = random.randint(0, 59)
#     return f"{hour}:{minute}"  
# def generate_sample_times(df):
#     num_samples = len(df)  
#     birth_times = [generate_time() for _ in range(num_samples)]
#     df['time_of_birth'] = birth_times
#     return df
# df = generate_sample_times(df)
# df.to_csv("updated_main_data.csv", index=False)

# import pandas as pd 
# import numpy as np 
# from geopy.geocoders import Nominatim

# geolocator = Nominatim(user_agent="MyApp")

# df=pd.read_csv("updated_main_data.csv")

# for i in df.iterrows():
#     location = geolocator.geocode(df['place_of_birth'])
#     df['latitude']=location.latitude
#     df['longitude']=location.longitude
# df.to_csv("update.csv",index=False)

# import pandas as pd
# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderTimedOut

# def geocode_location(place_of_birth):
#     try:
#         location=geolocator.geocode(place_of_birth,timeout=10)
#         if location:
#             return location.latitude,location.longitude
#         else:
#             return None,None
#     except GeocoderTimedOut:
#         print(f"Geocoding service timed out for: {place_of_birth}")
#         return None, None


# geolocator = Nominatim(user_agent="MyApp")
# df = pd.read_csv("updated_main_data.csv")

# longitude=[]
# latitude=[]

# for index,row in df.iterrows():
#     lat,lon=geocode_location(row['place_of_birth'])
#     latitude.append(lat)
#     longitude.append(lon)
# df['latitude']=latitude
# df['longitude']=longitude

# df.to_csv('main.csv',index=False)

import pandas as pd 
import swisseph as swe

def get_house(julian_day,latitude,longitude):
    ascmc = swe.houses(julian_day,latitude,longitude)
    houses = ascmc[0]  
    # ascendant = ascmc[1]  
    return  houses

def get_planet(julian_day):
    planets = {
        'Sun':swe.SUN,
        'Venus':swe.VENUS,
        'Jupiter':swe.JUPITER,
        'Mars':swe.MARS,
        'Uranus':swe.URANUS,
        'Mercury':swe.MERCURY,
        'Saturn':swe.SATURN,
        'Neptune':swe.NEPTUNE,
        'Earth':swe.EARTH
                }
    positions={}
    for planet_name,planet_code in planets.items():
        pos = swe.calc_ut(julian_day,planet_code)[0][0]
        positions[planet_name]=pos
    return positions


def main_idea(dob,birth_times,latitude,longitude):
    year,month,day=dob
    hour,min=birth_times
    julian_day=swe.julday(year,month,day,hour+min/60.0)

    houses=get_house(julian_day,latitude,longitude)
    planet_pos = get_planet(julian_day)

    planetary_houses = {}
    for planet, position in planet_pos.items():
        for i in range(12):
            if houses[i] <= position < houses[(i + 1) % 12]:
                planetary_houses[planet] = i + 1
                break
    
    return planetary_houses
df = pd.read_csv('main.csv')
df['house']=''
for index,row in df.iterrows():
    dob = [int(x) for x in row['DOB'].split('-')]
    birth_times = [int(x) for x in row['time_of_birth'].split(':')]
    latitude = row['latitude']
    longitude = row['longitude']

    houses = main_idea(dob,birth_times,latitude,longitude)
    for planet, house in houses.items():
     r=f"{planet} is in house {house}"
     df.at[index,'house']=r
df.to_csv('new.csv',index=False)



