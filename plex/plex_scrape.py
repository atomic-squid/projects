# this script requres pandas, lxml, python-dotenv, and openpyxl
import pandas as pd
from os import getenv
from dotenv import dotenv_values

# load the environment variables from the .env file
config = dotenv_values('.env')
plex_url = config['PLEX_URL']
plex_token = config['PLEX_TOKEN']
movie_index = config['MOVIE_INDEX']
tv_index = config['TV_INDEX']

def split_path(path: str):
    folder, file = path.extract(r'(.*)\/([^\/]*)$', expand=True)
    return (folder, file)

# grab movies from Plex
movies_collection = pd.read_xml(
    path_or_buffer = f'{plex_url}/library/sections/{movie_index}/all?X-Plex-Token={plex_token}',
    parser = 'lxml',
    stylesheet='movie_transform.xsl',
    parse_dates=['release']
)

# split the full_path into folder and file
movies_collection[['folder', 'file']] = split_path(movies_collection['full_path'].str)
movies_collection = movies_collection.drop(columns=['full_path'])

# grab tv shows from Plex
tv_collection = pd.read_xml(
    path_or_buffer = f'{plex_url}/library/sections/{tv_index}/allLeaves?X-Plex-Token={plex_token}',
    parser = 'lxml',
    stylesheet='tv_transform.xsl',
    parse_dates=['release']
)

# split the full_path into folder and file
tv_collection[['folder', 'file']] = split_path(tv_collection['full_path'].str)
tv_collection = tv_collection.drop(columns=['full_path'])

# write to excel and csv
with pd.ExcelWriter("data.xlsx") as datafile:
    movies_collection.to_excel(datafile, sheet_name='Movies', index=None)
    tv_collection.to_excel(datafile, sheet_name='TV Shows', index=None)

movies_collection.to_csv('movie_data.csv', index=None)
tv_collection.to_csv('tv_data.csv', index=None)