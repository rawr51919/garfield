import os
import urllib.request
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
starting_date = todays_date.replace(year=1978, month=6, day=19)

# check if the folders for each publication year up to this point
# exist, and if not, create them. start downloading them afterwards
# reqd_date is how it is due to the date structure on the image links
# using a slightly different date structure than what Python generally uses
for some_date in daterange(starting_date, todays_date):
    dir = f"./comics/Garfield/{some_date.year}"
    if not os.path.exists(dir):
        os.makedirs(dir)
    reqd_date = f"{some_date.year}-{some_date.month:02}-{some_date.day:02}"
    image_url = f"https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/{some_date.year}/{reqd_date}.gif"
    file = f"{dir}/{str(reqd_date)}.gif"
    if not os.path.exists(file):
        with urllib.request.urlopen(image_url) as im:
            print(f"Downloading: {image_url}")
            save_file = open(f"{dir}/{str(reqd_date)}.gif", "w" + "b")
            save_file.write(im.read())
            save_file.close()

print("All Garfield comics have been downloaded.\nThanks for using.")
