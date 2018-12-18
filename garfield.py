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
#  Made by Anurag (https://github.com/wafflemelon)               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# to get a date
def daterange(start, end):
    for x in range(int((end - start).days)+1):
        yield start + timedelta(x)

# This is to create a subdirectory, because the working directory will be a mess if it isn't organized
dir = "./comics/"
if not os.path.exists(dir):
    os.makedirs(dir)

todays_date = date.today()

# This has to be set because Garfield started on 1978/6/19
starting_date = todays_date.replace(year=1978, month=6, day=19)

for some_date in daterange (starting_date, todays_date):
    dir = f"./comics/{some_date.year}"
    if not os.path.exists(dir):
        os.makedirs(dir)
    reqd_date = f"{some_date.year}-{some_date.month:02}-{some_date.day:02}"
    image_url = f"https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/{some_date.year}/{reqd_date}.gif"
    file = f"./comics/{some_date.year}/{str(reqd_date)}.gif"
    if not os.path.exists(file):
        with urllib.request.urlopen(image_url) as im:
            print(f"Downloading: {image_url}")
            save_file = open(f"./comics/{some_date.year}/{str(reqd_date)}.gif", "w" + "b")
            save_file.write(im.read())
            save_file.close()

print("All Garfield comics have been downloaded.")
print("Thanks for using.")
