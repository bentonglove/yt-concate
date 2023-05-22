import os
from dotenv import load_dotenv

load_dotenv()
Google_API_Key = os.getenv('API_KEY')
# Google API Key which should be stored in .env file


# YouTube Channel IDs
# Get Channel ID by username https://www.streamweasels.com/tools/youtube-channel-id-and-user-id-convertor/
SupercarBlondie_CID = 'UCKSVUHI9rbbkXhvAXK-2uxA'
TechWithTim_CID = 'UC4JX40jDee_tINbkjycV4Sg'

# The directories
DOWNLOADS_DIR = 'downloads\\'
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions\\')
VTT_DIR = os.path.join(CAPTIONS_DIR, 'vtt\\')
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos\\')
OUTPUTS_DIR = 'outputs\\'
