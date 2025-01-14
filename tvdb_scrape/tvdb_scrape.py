from sys import argv, exit

def help():
    print("""
Usage: python tvdb_scrape.py <flags> show-name

Flags:
    -h: This help message
    -o: Official order (default)
    -d: DVD Order
    -a: Alternate order

Example:
    python tvdb_scrape.py -a animaniacs
    """)

# URL of the webpage to scrape
if len(argv) < 2 or argv[1] == '-h':
    help()
    exit()
elif len(argv) >= 3:
    match argv[1]:
        case '-o':
            order = 'official'
        case '-d':
            order = 'dvd'
        case '-a':
            order = 'alternate'
else:
    order = 'official'

show_name = argv[-1].strip().lower().replace(" ", "-")

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime

url = f'https://www.thetvdb.com/series/{show_name}/allseasons/{order}'

def clean_str(string):
    return re.sub(r'[<>:"/\\|?*]', '', string)

def gen_record(episode):
        try:

            episode_code = episode.find(['span','small'], class_='text-muted episode-label').text.strip()

            if 'SPECIAL' in episode_code.upper():
                special_match = re.search(r'SPECIAL 0x(\d+)', episode_code, re.IGNORECASE)
                season_num = 0
                episode_num = int(special_match[1]) if special_match else None
            else:
                season_match = re.search(r'S(\d+)E(\d+)', episode_code, re.IGNORECASE)
                if season_match:
                    season_num = int(season_match[1])
                    episode_num = int(season_match[2])
                else:
                    season_num, episode_num = None, None

            episode_code = f'S{season_num:02}E{episode_num:02}'

        except ValueError:
            episode_code, season_num, episode_num = None, None, None

        try:
            air_date = datetime.strptime(
                episode.find('ul', class_='list-inline text-muted').find('li').text.strip(),
                '%B %d, %Y'
            )
        except:
            air_date = None

        title = episode.find('a').text.strip()

        clean_title = clean_str(str(title).replace('/', '-'))

        description = episode.find('div', class_='col-xs-9').find('p').text.strip()
        description = re.sub(r'[\n\r\s]+', ' ', description)

        try:
            image_url = episode.find('div', class_='col-xs-3').find('img')['data-src']
        except Exception:
            image_url = None

        filename = f'{clean_show_name} - {episode_code} - {clean_title}'

        data = {
            'Episode Code': episode_code,
            'Air Date': air_date,
            'Filename': filename,
            'Season Number': season_num,
            'Episode Number': episode_num,
            'Title': title,
            'Description': description,
            'Image URL': image_url
        }
        
        return data


# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    page_content = BeautifulSoup(response.text, 'html.parser')

    # set the show name from the HTML head
    clean_show_name = clean_str(page_content.find("head").find("title").text.split("-")[0].strip())

    # Create output dataset
    output_data = []

    episodes = page_content.find_all('li', class_='list-group-item')

    for episode in episodes:

        output_data.append(gen_record(episode))

        # print(f'Episode: {episode_code}, Title: {title}, Image: {image}')

else:
    print(f'Failed to retrieve the page for show \"{argv[1]}\". Status code: {response.status_code}')
    exit()

output_dataframe = pd.DataFrame(output_data)

try:
    output_dataframe = output_dataframe.sort_values(['Season Number', 'Episode Number'])
except KeyError:
    pass

if not output_dataframe.empty:
    output_file_name = f'{show_name}-{order}.csv'

    output_dataframe.to_csv(output_file_name, index=None)

    print(f'{len(output_dataframe)} records output to {output_file_name}.')
else:
    print('No data to export. exiting.')