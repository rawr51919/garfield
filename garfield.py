import io
import os
import urllib.request
from datetime import date, timedelta

# to get a date


def daterange(start, end):
    for x in range(int((end - start).days)):
        yield start + timedelta(x)


# to create a directory because it will be a mess if not organized
dir = "./comics/"
if not os.path.exists(dir):
    os.makedirs(dir)


todays_date = date.today()

# this has to be set because garfield started on 1978/6/19
starting_date = todays_date.replace(year=1978, month=6, day=19)


for some_date in daterange(starting_date, todays_date):
    reqd_date = f"{some_date.year}-{some_date.month:02}-{some_date.day:02}"
    # image_url = f"https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/{some_date.year}/{some_date}.gif"
    # but will print "1" instead of "01"
    image_url = f"https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/{some_date.year}/{reqd_date}.gif"

    file = f"{dir}{str(reqd_date)}.gif"
    if not os.path.exists(file):
        with urllib.request.urlopen(image_url) as im:
            print(f"Downloading:: {image_url}")
            save_file = open(f"{dir}{str(reqd_date)}.gif", "w" + "b")
            save_file.write(im.read())
            save_file.close()

print("All comics have been downloaded")
print("thanks for using")
