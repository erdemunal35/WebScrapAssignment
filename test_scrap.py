import unittest
import scrap

class TestScrap(unittest.TestCase):
    def test_hotel_name(self):
        self.assertEqual(scrap.output_dataset["hotel_name"], "Kempinski Hotel Bristol Berlin, Germany ")

    def test_address(self):
        self.assertEqual(scrap.output_dataset["address"], "Kurf\u00fcrstendamm 27, Charlottenburg-Wilmersdorf, 10719 Berlin, Germany")

    def test_stars(self):
        self.assertEqual(scrap.output_dataset["stars"], "ratings_stars_5")
    
    def test_review_points(self):
        self.assertEqual(scrap.output_dataset["review_points"], "8.3")
    
    def test_number_of_reviews(self):
        self.assertEqual(scrap.output_dataset["number_of_reviews"], "1401")
    
    def test_description(self):
        self.assertEqual(scrap.output_dataset["description"], "This 5-star hotel on Berlin\u2019s Kurf\u00fcrstendamm shopping street offers elegant rooms, an indoor pool and great public transport links. It is 600 metres from the Ged\u00e4chtniskirche Church and Berlin Zoo.Kempinski Hotel Bristol Berlin offers air-conditioned rooms with large windows, modern bathrooms and international TV channels. Bathrobes are provided. Free WiFi is available in all areas and high-speed WiFi access can be booked at an additional cost.Gourmet cuisine is served in the popular Kempinski Grill. Reinhard's brasserie offer light cuisine and a terrace overlooking Kurf\u00fcrstendamm. Guests can enjoy drinks in the Gobelin Halle lounge or in the Bristol Bar.Kempinski Bristol Berlin\u2019s spa includes a sauna, steam room and gym. Massages and beauty treatments can also be booked here. The hotel's business centre can be used free of charge.Uhlandstra\u00dfe Underground Station is just outside the Kempinski\u2019s front door. The KaDeWe shopping mall is 2 stops away. \n\nWe speak your language!\nThis property has been on Booking.com since 17 May 2010.\nHotel Rooms: 301, \nHotel Chain:\nKempinski\n")

    def test_room_categories(self):
        self.assertEqual(scrap.output_dataset["room_categories"], ["Suite with Balcony", "Classic Double or Twin Room", "Superior Double or Twin Room", "Deluxe Double Room", "Deluxe Business Suite", "Junior Suite", "Family Room"])

    def test_alternative_hotels(self):
        self.assertEqual(scrap.output_dataset["alternative_hotels"], ["Hotel Adlon Kempinski Berlin", "Grand Hyatt Berlin", "Sofitel Berlin Kurf\u00fcrstendamm", "Hilton Berlin"])

if __name__ == '__main__':
    unittest.main()