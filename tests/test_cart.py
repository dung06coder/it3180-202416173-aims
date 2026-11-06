import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        
        # Thêm 20 đĩa DVD đầu tiên (đúng giới hạn cho phép)
        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i+1}")
            # Nếu class Cart dùng add_digital_video_disc thì đổi tên hàm bên dưới tương ứng
            if hasattr(cart, 'add_digital_video_disc'):
                cart.add_digital_video_disc(dvd)
            else:
                cart.add_dvd(dvd)
            
        # Thêm đĩa thứ 21 (vượt quá giới hạn MAX_NUMBERS_ORDERED = 20)
        dvd_21 = DigitalVideoDisc("DVD 21")
        if hasattr(cart, 'add_digital_video_disc'):
            result = cart.add_digital_video_disc(dvd_21)
        else:
            result = cart.add_dvd(dvd_21)
        
        self.assertFalse(result, "Giỏ hàng phải từ chối khi thêm đĩa thứ 21 vượt quá giới hạn cho phép")

    def test_sort_by_title(self):
        cart = Cart()
        dvd1 = DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95)
        dvd2 = DigitalVideoDisc("Aladdin", "Animation", "John Musker", 90, 18.99)
        
        add_fn = getattr(cart, 'add_digital_video_disc', getattr(cart, 'add_dvd', None))
        add_fn(dvd1)
        add_fn(dvd2)
        
        cart.sort_by_title()
        self.assertEqual(cart.items[0].title, "Aladdin")

    def test_sort_by_cost(self):
        cart = Cart()
        dvd1 = DigitalVideoDisc("Cheap Movie", "Comedy", "Director A", 90, 5.00)
        dvd2 = DigitalVideoDisc("Expensive Movie", "Action", "Director B", 120, 25.00)
        
        add_fn = getattr(cart, 'add_digital_video_disc', getattr(cart, 'add_dvd', None))
        add_fn(dvd1)
        add_fn(dvd2)
        
        cart.sort_by_cost()
        self.assertEqual(cart.items[0].cost, 25.00)

if __name__ == '__main__':
    unittest.main()