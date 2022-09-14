from django.test import TestCase

# Create your tests here.
from katalog.models import CatalogItem

# Create your tests here.
class Coba(TestCase):
    def setUp(self):
        CatalogItem.objects.create(
            item_name = "Kacamata",
            item_price = 199000,
            item_stock = 3,
            description = "Kegantengan++",
            rating = 10,
            item_url = "https://github.com/rafialyfarrel/Tugas2")
        
        CatalogItem.objects.create(
            item_name = "Topi",
            item_price = 289000,
            item_stock = 1,
            description = "Penutup Kepala Botak",
            rating = 9,
            item_url = "https://github.com/rafialyfarrel/Tugas2")

        CatalogItem.objects.create(
            item_name = "Jam Tangan",
            item_price = 10000000,
            item_stock = 2,
            description = "Anak Sultan",
            rating = 1,
            item_url = "https://github.com/rafialyfarrel/Tugas2"
        )
    
    def test_if_item_exists(self):
        coba1 = CatalogItem.objects.get(item_name = "Kacamata")
        coba2 = CatalogItem.objects.get(item_name = "Topi")
        coba3 = CatalogItem.objects.get(item_name = "Jam Tangan")
        self.assertIn("Kacamata", coba1.item_name)
        self.assertIn("Topi", coba2.item_name)
        self.assertIn("Jam Tangan", coba3.item_name)