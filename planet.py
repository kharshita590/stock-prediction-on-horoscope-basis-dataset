# import pandas as pd 
# import numpy as np 

# # df = pd.read_csv("planet.csv")
# # df = df.sample(n=768,random_state=42)
# # df.to_csv('planet_influence.csv',index=False)

# # df = pd.read_csv("hi.csv")
# # df1=pd.read_csv("planet_influence.csv")
# # df = pd.concat([df1,df],axis=1)
# # df.to_csv("hi.csv",index=False)
# def planet(df):
#     if df['Planetary_pos']=="Sun in 1st House" or planets=="Sun in 7th House" or planets=="Sun in 10th House" or planets=="Moon in 10th House" or planets=="Mars in 1st House" or planets=="Jupiter in 10th House" or planets=="Saturn in 10th House" or planets=="Rahu in 1st House" or planets=="Jupiter retrograding":
#         df['planets'] = f"{df['Planetary_pos']} so you should invest in startups and in government projects, some stocks in this field are
# Stockal, Smallcase, Trade Brains, CapitalVia,Gill Broking, etc. "
#     elif df['Planetary_pos']=="Sun in 2nd House" or planets=="Moon in 2nd House" or planets=="Venus in 1st House" or planets=="Venus in 2nd House" or planets=="Venus in 7th House" :
#         df['planets'] = f"{df['Planetary_pos']} so you should invest in gold and luxury goods and moon is in 2nd House so you can also invest in media stocks. "
    
#     elif df['Planetary_pos']=="Sun in 3rd House" or planets=="Moon in 3rd House" or planets=="Mercury in 1st House" or planets=="Rahu in 3rd House" or planets=="Ketu in 3rd House":
#         df['planets'] = f"{df['Planetary_pos']} so you should invest in media and communication stocks, some stocks in this field are Reliance Industries, Hathway, Route Mobile etc. "

#     elif df['Planetary_pos']=="Mercury retrograding":
#         df["planets"] = f"{df['Planetary_pos']} so you should not invest in media and communication stocks"

#     elif df['Planetary_pos'] == "Sun in 4th House" or planets=="Mercury in 4th House" or planets=="Venus in 4th House" or planets=="Mars in 4th House" or planets=="Jupiter in 4th House" or planets=="Saturn in 4th House" or planets=="Rahu in 4th House" or planets=="Ketu in 4th House":
#         df["planets"] = f"{df['Planetary_pos']} so you should invest in real estate stocks, some stocks in this field are Oberoi Realty, Phoenix Mills, DLF,Godrej Properties,Sunteck Realty, etc "
    
#     elif df['Planetary_pos']=="Venus retrograding":
#         df["planets"] = f"{df['Planetary_pos']} so you should not invest in real estate stocks"

#     elif df['planets']=="Sun in 5th House" or planets=="Moon in 5th House" or planets=="Venus in 5th House":
#         df["planets"] = f"{planets} so you should invest in entertainment stocks, some stocks in this field are PVR INOX,Shemaroo Entertainment,
# Tips Industries,Network18 etc "
        
#     elif df['planets']=="Sun in 6th House" or planets=="Moon in 6th House" or planets=="Moon in 12th House" or planets=="Mercury in 6th House" or planets=="Venus in 6th House" or planets=="Mars in 6th House" or planets=="Venus in 12th House" or planets=="Jupiter in 6th House" or planets=="Saturn in 6th House" or planets=="Rahu in 6th House" or planets=="Ketu in 6th House":
#          df["planets"] = f"{planets} so you should invest in healthcare or pharma stocks, some stocks in this field are Dr Lal Path Labs,Apollo Hospitals,Fortis Healthcare,Divi's Laboratories,
# Cipla,Mankind Pharma,etc "
         
#     elif df['planets']=="Mars retrograding":
#         df["planets"] = f"{planets} so you should not invest in healthcare or pharma stocks."

#     elif df['planets']=="Sun in 7th House" or planets=="Mercury in 7th House" or planets=="Mars in 7th House" or planets=="Saturn in 7th House" or planets=="Rahu in 7th House" or planets=="Ketu in 7th House":
#          df["planets"] = f"{planets} so you should invest in legal firms , some stocks in this field are Thomson Reuters Corporation, 
# Gateley (Holdings) PLC, RBG Holdings, Keystone Law Gr, etc "
         
#     elif df['planets']=="Sun in 8th House" or planets=="Moon in 8th House" or planets=="Mars in 8th House" or planets=="Jupiter in 8th House" or planets=="Saturn in 8th House":
#         df["planets"] = f"{planets} so you should invest in insurance stocks , some stocks in this field are ICICI Prudential Life Insurance, HDFC Life Insurance, New India Assurance, Star Health and Allied Insurance etc "
    
#     elif df['planets']=="Sun in 9th House" or planets=="Moon in 9th House" or planets=="Mercury in 9th House" or planets=="Jupiter in 5th House" or planets=="Rahu in 9th House" or planets=="Ketu in 9th House":
#           df["planets"] = f"{planets} so you should invest in educational stocks, some stocks in this field are Veranda Learning, CL Educate, Zee Learn, Global Education, 
# MT Educare, etc "
          
#     elif df['planets']=="Jupiter retrograding":
#         df["planets"] = f"{planets} so you should not invest in educational stocks ."

#     elif df['planets']=="Sun in 10th House " or planets=="Jupiter in 10th House":
#          df["planets"] = f"{planets} so you should invest in government projects stocks, some stocks in this field are 
# Ircon International, Engineers India, NBCC (India) Limited etc "
         
#     elif df['planets']=="Saturn retrograding":
#         df["planets"] = f"{planets} so you should not invest in government projects stocks ."

#     elif df['planets']=="Sun in 11th House" or planets=="Moon in 11th House" or planets=="Mercury in 11th House" or planets=="Mars in 3rd House" or planets=="Mars in 11th House" or planets=="Jupiter in 11th House" or planets=="Saturn in 11th House" or planets=="Rahu in 1st House" or planets=="Rahu in 3rd House" or planets=="Rahu in 11th House" or planets=="Ketu in 11th House":
#         df["planets"] = f"{planets} so you should invest in IT, technology stocks, some stocks in this field are 
# MapmyIndia, Coforge, 
# Infosys, Affle (India) Limited, Newgen Software, HCLTech etc "
        
#     elif df['planets']=="Rahu retrograding":
#         df["planets"] = f"{planets} so you should not invest in IT, technology stocks ."

#     elif df['planets']=="Sun in 12th House":
#         df["planets"] = f"{planets} so you should invest in foreign stocks, some stocks in this field are 
# NVIDIA, Microsoft, Apple etc "
        
#     elif df['planets']=="Moon in 1st House":
#         df["planets"] = f"{planets} so you should invest in food stocks, some stocks in this field are 
# Britannia Industries, Hatsun Agro Products, 
# Mrs. Bectors Food, etc "
        
#     return df


# df = pd.read_csv("hi.csv")       
# for index,row in df.iterrows():
#     f = planet(row['Planetary_pos'])

import pandas as pd
import numpy as np

def planet(planets):
    if planets == "Sun in 1st House" or planets == "Sun in 7th House" or planets == "Sun in 10th House" or planets == "Moon in 10th House" or planets == "Mars in 1st House" or planets == "Jupiter in 10th House" or planets == "Saturn in 10th House" or planets == "Rahu in 1st House" or planets == "Jupiter retrograding":
        return f"{planets} so you should invest in startups and in government projects. Some stocks in this field are Stockal, Smallcase, Trade Brains, CapitalVia, Gill Broking, etc."
    
    elif planets == "Sun in 2nd House" or planets == "Moon in 2nd House" or planets == "Venus in 1st House" or planets == "Venus in 2nd House" or planets == "Venus in 7th House":
        return f"{planets} so you should invest in gold and luxury goods, and since Moon is in 2nd House, you can also invest in media stocks."
    
    elif planets == "Sun in 3rd House" or planets == "Moon in 3rd House" or planets == "Mercury in 1st House" or planets=="Mercury in 3rd House" or planets == "Rahu in 3rd House" or planets == "Ketu in 3rd House" or planets=="Jupiter in 3rd House":
        return f"{planets} so you should invest in media and communication stocks. Some stocks in this field are Reliance Industries, Hathway, Route Mobile, etc."
    
    elif planets == "Mercury retrograding":
        return f"{planets} so you should not invest in media and communication stocks."
    
    elif planets == "Sun in 4th House" or planets == "Mercury in 4th House" or planets == "Venus in 4th House" or planets == "Mars in 4th House" or planets == "Jupiter in 4th House" or planets == "Saturn in 4th House" or planets == "Saturn in 10th House" or planets == "Rahu in 4th House" or planets == "Ketu in 4th House" or planets=="Moon in 4th House":
        return f"{planets} so you should invest in real estate stocks. Some stocks in this field are Oberoi Realty, Phoenix Mills, DLF, Godrej Properties, Sunteck Realty, etc."
    
    elif planets == "Venus retrograding":
        return f"{planets} so you should not invest in real estate stocks."
    
    elif planets == "Sun in 5th House" or planets == "Moon in 5th House" or planets == "Venus in 5th House":
        return f"{planets} so you should invest in entertainment stocks. Some stocks in this field are PVR INOX, Shemaroo Entertainment, Tips Industries, Network18, etc."
    
    elif planets == "Sun in 6th House" or planets == "Moon in 6th House" or planets=="Moon in 12th House"  or planets == "Mercury in 6th House" or planets == "Mercury in 12th House" or planets == "Venus in 6th House" or planets == "Mars in 6th House" or planets == "Venus in 12th House" or planets == "Jupiter in 6th House" or planets == "Saturn in 6th House" or planets == "Rahu in 6th House" or planets == "Ketu in 6th House":
        return f"{planets} so you should invest in healthcare or pharma stocks. Some stocks in this field are Dr. Lal Path Labs, Apollo Hospitals, Fortis Healthcare, Divi's Laboratories, Cipla, Mankind Pharma, etc."
    
    elif planets == "Mars retrograding":
        return f"{planets} so you should not invest in healthcare or pharma stocks."
    
    elif planets == "Sun in 7th House" or planets == "Mercury in 7th House" or planets == "Mars in 7th House" or planets == "Saturn in 7th House" or planets == "Rahu in 7th House" or planets == "Ketu in 7th House" or planets=="Jupiter in 1st House" or planets=="Jupiter in 7th House":
        return f"{planets} so you should invest in legal firms. Some stocks in this field are Thomson Reuters Corporation, Gateley (Holdings) PLC, RBG Holdings, Keystone Law Group, etc."
    
    elif planets == "Sun in 8th House" or planets == "Moon in 8th House" or planets == "Mars in 8th House" or planets == "Jupiter in 8th House" or planets == "Saturn in 8th House" or planets=="Rahu in 8th House":
        return f"{planets} so you should invest in insurance stocks. Some stocks in this field are ICICI Prudential Life Insurance, HDFC Life Insurance, New India Assurance, Star Health and Allied Insurance, etc."
    
    elif planets == "Sun in 9th House" or planets == "Moon in 9th House" or planets == "Mercury in 9th House" or planets=="Mercury in 5th House" or planets == "Jupiter in 5th House" or planets == "Jupiter in 9th House" or planets == "Rahu in 9th House" or planets == "Ketu in 9th House" or planets=="Saturn in 5th House" or planets == "Saturn in 9th House":
        return f"{planets} so you should invest in educational stocks. Some stocks in this field are Veranda Learning, CL Educate, Zee Learn, Global Education, MT Educare, etc."
    
    elif planets == "Jupiter retrograding":
        return f"{planets} so you should not invest in educational stocks."
    
    elif planets == "Sun in 10th House" or planets == "Jupiter in 10th House" or planets=="Mercury in 10th House":
        return f"{planets} so you should invest in government projects stocks. Some stocks in this field are Ircon International, Engineers India, NBCC (India) Limited, etc."
    
    elif planets == "Saturn retrograding":
        return f"{planets} so you should not invest in government projects stocks."
    
    elif planets == "Sun in 11th House" or planets == "Moon in 11th House" or planets == "Mercury in 11th House" or planets == "Mars in 3rd House" or planets == "Mars in 11th House" or planets == "Mars in 10th House" or planets == "Jupiter in 11th House" or planets == "Saturn in 3rd House " or planets == "Saturn in 11th House" or planets == "Rahu in 1st House" or planets == "Rahu in 3rd House" or planets == "Rahu in 11th House" or planets == "Ketu in 11th House" or planets=="Venus in 11th House":
        return f"{planets} so you should invest in IT and technology stocks. Some stocks in this field are MapmyIndia, Coforge, Infosys, Affle (India) Limited, Newgen Software, HCLTech, etc."
    
    elif planets == "Rahu retrograding":
        return f"{planets} so you should not invest in IT and technology stocks."
    
    elif planets == "Sun in 12th House" or planets=="Mercury in 9th House" or planets=="Mars in 12th House" or planets=="Jupiter in 12th House" or planets=="Saturn in 12th House" or planets=="Rahu in 2nd House" or planets=="Rahu in 5th House" or planets=="Rahu in 9th House":
        return f"{planets} so you should invest in foreign stocks. Some stocks in this field are NVIDIA, Microsoft, Apple, etc."
    
    elif planets == "Moon in 1st House" or planets=="Rahu in 12th House":
        return f"{planets} so you should invest in food stocks. Some stocks in this field are Britannia Industries, Hatsun Agro Products, Mrs. Bectors Food, etc."
    
    elif planets=="Moon in 7th House":
         return f"{planets} so you should invest in Women centric companies stocks. Some stocks in this field are Ventas, Inc, Best Buy Co. Inc, Duke Energy Corporation, etc."
    
    elif planets=="Mercury in 2nd House" or planets=="Mercury in 8th House":
         return f"{planets} so you should invest in Retail stocks. Some stocks in this field are V2 Retail, V-Mart Retail, Sai Silks (Kalamandir) Ltd, Spencer's Retail etc."
    
    elif planets=="Venus in 10th House" or planets=="Venus in 3rd House" or planets=="Venus in 7th House" or planets=="Venus in 8th House" or planets=="Venus in 9th House" or planets=="Venus in 10th House" :
          return f"{planets} so you should invest in beauty stocks. Some stocks in this field are Tira, V-Mart Nykaa,  etc."
    
    elif planets=="Mars in 2nd House":
         return f"{planets} so you should invest in steel,energy stocks. Some stocks in this field are Jindal Steel and Power,Sarda Energy & Minerals, Electrotherm  etc."
    
    elif planets=="Mars in 5th House" or planets=="Mars in 9th House" or planets=="Rahu in 10th House":
          return f"{planets} so you should invest in sports stocks. Some stocks in this field are the Madison Square Garden Company, Churchill Downs Incorporated, Formula One Group, PENN Entertainment etc."
    
    elif planets=="Jupiter in 2nd House" or planets=="Saturn in 2nd House":
         return f"{planets} so you should invest in Banking, Finance stocks. Some stocks in this field are ICICI Bank, Kotak Mahindra Bank, HDFC Bank, Axis Bank, etc ."
    
    elif planets=="Ketu in 1st House" or planets=="Ketu in 2nd House" or planets=="Ketu in 5th House" or planets=="Ketu in 7th House" or planets=="Ketu in 8th House" or planets=="Ketu in 10th House" or planets=="Ketu in 12th House":
         return f"{planets} so you should invest in spritual stocks. Some stocks in this field are Divine Dance, Blissful Balance, Sacred Space, Awakened Journeys, etc ."
    
    elif planets=="Ketu retrograding":
         return f"{planets} so you should not invest in spritual stocks."
    
    return ""

df = pd.read_csv("hi.csv")

df['Investment_Advice'] = df['Planetary_pos'].apply(planet)
df=df.drop(['Planetary_position','Planetary_influence'],axis=1)
df.to_csv("hi1.csv", index=False)
