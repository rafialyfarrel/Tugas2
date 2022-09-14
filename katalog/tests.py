from django.test import TestCase

# Create your tests here.
from katalog.models import CatalogItem

# Create your tests here.
class Coba_Run(TestCase):
    def setUp(self):
        CatalogItem.objects.create(
            item_name = "Kacamata",
            item_price = 199000,
            item_stock = 3,
            description = "Kegantengan++",
            rating = 10,
            item_url = "https://www.tokopedia.com/optikdiana/frame-kacamata-pria-wanita-sooper-eyewear-689-model-vintage")
        
        CatalogItem.objects.create(
            item_name = "Topi",
            item_price = 289000,
            item_stock = 1,
            description = "Penutup Kepala Botak",
            rating = 9,
            item_url = "https://www.tokopedia.com/premierclothing/newsboy-cap-wool-pria-premier-hat-style-m?extParam=ivf%3Dfalse&src=topads")

        CatalogItem.objects.create(
            item_name = "Jam Tangan",
            item_price = 10000000,
            item_stock = 2,
            description = "Anak Sultan",
            rating = 1,
            item_url = "https://www.tokopedia.com/liga-arloji/casio-mw-240-1evdf-jam-tangan-pria-hitam-balok-hitam?extParam=ivf%3Dfalse"
        )
    
    def test(self):
        coba1 = CatalogItem.objects.get(item_name = "Kacamata")
        coba2 = CatalogItem.objects.get(item_name = "Topi")
        coba3 = CatalogItem.objects.get(item_name = "Jam Tangan")
        self.assertIn("Kacamata", coba1.item_name)
        self.assertIn("Topi", coba2.item_name)
        self.assertIn("Jam Tangan", coba3.item_name)