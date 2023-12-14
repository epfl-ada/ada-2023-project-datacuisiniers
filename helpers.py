import numpy as np
import pandas as pd
import os
import json
import gzip
import pandas as pd
from tqdm import tqdm
import xml.etree.ElementTree as ET

def extract_character_names(movie_plots):
    ''' This function extracts the character names form the corNLP dataset, which is a structured form of 
        the corpus movie plot summaries 
        input: movie_plots database
        output: The extracted character names'''
    
    character_names = []
    for (i, j) in tqdm(enumerate(movie_plots['id'])):
        # Specify the path to your compressed XML file
        compressed_file_path = 'corenlp_plot_summaries/' + str(j) + '.xml.gz'
        
        # Open the compressed file and decompress it
        with gzip.open(compressed_file_path, 'rb') as compressed_file:
            # Parse the XML content from the decompressed file
            tree = ET.parse(compressed_file)
            root = tree.getroot()

            # Extract character names (entities of type "PERSON")
            for sentence in root.iter('sentence'):
                for entity in sentence.iter('token'):
                    entity_type = entity.find('NER').text
                    if entity_type == 'PERSON':
                        mention = ' '.join(token.find('word').text for token in entity.iter('token'))
                        character_names.append((mention, j))

    return character_names

########################################### LONGEVITY ###########################################
def format_of_country_change(x):
    n = len(x)
    if n == 0:
        return np.nan
    else:
        return list(x.values())

country_to_region = {
    'United States of America': 'North America',
    'Canada': 'North America',
    'Mexico': 'North America',
    'China': 'Asia',
    'India': 'Asia',
    'Russia': 'Europe',
    'Indonesia': 'Asia',
    'Pakistan': 'Asia',
    'Brazil': 'South America',
    'Nigeria': 'Africa',
    'Bangladesh': 'Asia',
    'Mexico': 'North America',
    'Japan': 'Asia',
    'Ethiopia': 'Africa',
    'Philippines': 'Asia',
    'Egypt': 'Africa',
    'Vietnam': 'Asia',
    'DR Congo': 'Africa',
    'Turkey': 'Europe',
    'Iran': 'Asia',
    'Germany': 'Europe',
    'Thailand': 'Asia',
    'United Kingdom': 'Europe',
    'France': 'Europe',
    'Italy': 'Europe',
    'Tanzania': 'Africa',
    'South Africa': 'Africa',
    'Myanmar': 'Asia',
    'South Korea': 'Asia',
    'Colombia': 'South America',
    'Kenya': 'Africa',
    'Spain': 'Europe',
    'Argentina': 'South America',
    'Ukraine': 'Europe',
    'Uganda': 'Africa',
    'Algeria': 'Africa',
    'Sudan': 'Africa',
    'Iraq': 'Asia',
    'Poland': 'Europe',
    'Canada': 'North America',
    'Morocco': 'Africa',
    'Saudi Arabia': 'Asia',
    'Uzbekistan': 'Asia',
    'Malaysia': 'Asia',
    'Peru': 'South America',
    'Angola': 'Africa',
    'Ghana': 'Africa',
    'Yemen': 'Asia',
    'Nepal': 'Asia',
    'Australia':'Oceania',
    'New Zealand' : 'Oceania',
    'Belgium' : 'Europe'
}

def get_region(country_list):
    if isinstance(country_list, list):
        first_country = country_list[0] if country_list else np.nan
        return country_to_region.get(first_country, 'Other')
    return 'Other'

########################################### REVENUES ###########################################

def count_unique(series):
    """Aggregation function to get the length of list of unique values in dictionaries"""
    if all(not my_dict for my_dict in series):
        return None
    else:
        return len(set(val for sublist in series for val in sublist))

def most_frequent_occ(series): 
    """Aggregation function to get the most frequent value of a column"""
    if not series.empty and not series.isna().all():
        return series.mode().iloc[0]  
    else:
        return None
    
def most_frequent_in_dictionary(series):
    if all(not my_dict for my_dict in series):
        return None
       
    else:
        # Flatten the list of dictionaries
        flattened_values = [item for sublist in series for item in sublist.values()]

        # Create a pandas Series from the flattened values
        flattened_series = pd.Series(flattened_values)

        # Calculate the mode of the flattened Series
        mode_value = flattened_series.mode().iloc[0]
        return mode_value
    
    
########################################### OSCARS ###########################################

def transform_features_all(input_features):
    """Reverses encoding for Oscar prediction"""
    string_indices = [0, 5, 6, 7, 8] 
    
    for index in string_indices:
        if input_features[index] in gender_mapping:
            input_features[index] = gender_mapping[input_features[index]]
        elif input_features[index] in language_dict:
            input_features[index] = language_dict[input_features[index]]
        elif input_features[index] in genre_dict:
            input_features[index] = genre_dict[input_features[index]]
        elif input_features[index] in country_dict:
            input_features[index] = country_dict[input_features[index]]
        elif input_features[index] in ethnicity_dict:
            input_features[index] = ethnicity_dict[input_features[index]]

    return input_features

def transform_features_select(input_features):
    """Reverses encoding for Oscar prediction"""
    string_indices = [0, 3, 4, 5] # to change if order of variables changes
    
    for index in string_indices:
        if input_features[index] in gender_mapping:
            input_features[index] = gender_mapping[input_features[index]]
        elif input_features[index] in language_dict:
            input_features[index] = language_dict[input_features[index]]
        elif input_features[index] in genre_dict:
            input_features[index] = genre_dict[input_features[index]]
        elif input_features[index] in country_dict:
            input_features[index] = country_dict[input_features[index]]

    return input_features

def concatenate_values_all(row):
    """Concatenate values and transform the features into something readable by our model"""
    InputArray = [row['Actor gender'], row['Actor age at movie release'], row['Actor height'],row['Movie runtime'], row['Persona'], row['languages'], row['genres'],row['countries'], row['Actor ethnicity']]
    return transform_features_all(InputArray)



def concatenate_values_select(row):
    InputArray = [row['Actor gender'], row['Actor age at movie release'],row['Movie runtime'], row['languages'], row['genres'],row['countries']]
    return transform_features_select(InputArray)
