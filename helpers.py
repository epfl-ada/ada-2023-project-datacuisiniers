import numpy as np
import pandas as pd
import os
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