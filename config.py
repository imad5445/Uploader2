import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("7021614897:AAHBoSWb_y6mv-x4Bls2KYHQTKSGpgtOpPQ", "")
    # The Telegram API things
    API_ID = int(os.environ.get("24218997", 12345))
    API_HASH = os.environ.get("b0419e875ab8647b12e885e74c492297")
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = int(os.environ.get("6904945981", ""))
    SESSION_NAME = "UPLOADER-X-BOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("mongodb+srv://imadndv786:OYQUgQ4zErsMGjIL@cluster0.wblwjan.mongodb.net/?retryWrites=true&w=majority", "")
    MAX_RESULTS = "50"
