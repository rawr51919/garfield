import os
import urllib.request
from urllib.error import HTTPError
from datetime import date, timedelta

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   _____  _____           _____  _____ ______   __  __ ______  #
#  |  __ \|  __ \    /\   |_   _|/ ____|  ____| |  \/  |  ____| #
#  | |__) | |__) |  /  \    | | | (___ | |__    | \  / | |__    #
#  |  ___/|  _  /  / /\ \   | |  \___ \|  __|   | |\/| |  __|   #
#  | |    | | \ \ / ____ \ _| |_ ____) | |____  | |  | | |____  #
#  |_|    |_|  \_/_/    \_|_____|_____/|______| |_|  |_|______| #
#                                                               #
#  Made by Anurag (https://github.com/wafflemelon)              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Get the date range
def daterange(start, end):
    for x in range(int((end - start).days)+1):
        yield start + timedelta(x)

# Set Garfield's start date (6/19/1978) and today's date
todays_date = date.today()
starting_date = date(1978, 6, 19)

# check if the folders for each publication year up to this point
# exist, and if not, create them. start downloading them afterwards
# reqd_date is how it is due to the date structure on the image links
# using a slightly different date structure than what Python generally uses
# 2025 edit: ensure we use a new URL as the original has gone defunct
# and do error checking if the requested date doesn't exist
for some_date in daterange(starting_date, todays_date):
    dir = f"./comics/Garfield/{some_date.year}"
    if not os.path.exists(dir):
        os.makedirs(dir)

    reqd_date = f"{some_date.year % 100}{some_date.month:02}{some_date.day:02}"
    image_url = f"https://picayune.uclick.com/comics/ga/{some_date.year}/ga{reqd_date}.gif"
    file_path = f"{dir}/ga{reqd_date}.gif"

    if not os.path.exists(file_path):
        try:
            with urllib.request.urlopen(image_url) as im:
                print(f"Downloading: {image_url}")
                with open(file_path, "wb") as save_file:
                    save_file.write(im.read())
        except HTTPError as e:
            if e.code == 404:
                print(f"Comic not found for date {some_date} (404). Skipping.")
            else:
                print(f"HTTP error {e.code} for date {some_date}. Skipping.")
        except Exception as e:
            print(f"Error downloading {some_date}: {e}")

print("All Garfield comics have been processed.\nThanks for using.")
