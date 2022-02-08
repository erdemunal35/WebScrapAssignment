from bs4 import BeautifulSoup
import codecs
import json

html_file = codecs.open("webpage.html", "r", "utf-8")

soup = BeautifulSoup(html_file, "lxml")

output_dataset = {}

#Fill the json format with required entries
try:
    output_dataset["hotel_name"] = soup.title.string.split("-")[0].split("\n")[1]
    output_dataset["address"] = soup.find("span", id="hp_address_subtitle").text.split("\n")[1]
    output_dataset["stars"] = soup.find("span", attrs={'class':"hp__hotel_ratings__stars hp__hotel_ratings__stars__clarification_track"}).i["class"][2]
    output_dataset["review_points"] = soup.find("span", attrs={'class':'average js--hp-scorecard-scoreval'}).text
    output_dataset["number_of_reviews"] = soup.find("div", id= "location_score_tooltip").small.strong.text
    output_dataset["description"] = "".join([p.text for p in soup.find("div", attrs={'class': "hotel_description_wrapper_exp"}).find_all("p")])
    output_dataset["room_categories"] = [row.find("td", attrs={'class':'ftd'}).text.split("\n")[1] for row in soup.find("table", id="maxotel_rooms").find("tbody").find_all("tr")]
    output_dataset["alternative_hotels"] = [col.find("a").text.split("\n")[1] for col in soup.find("table", id="althotelsTable").find("tbody").find_all("td")]
except:
    print("An exception occurred while scrapping the html file")
    
# For debug
#print(output_dataset["description"])

json_dump = json.dumps(output_dataset)
print(json_dump)