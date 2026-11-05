import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        
        # Thêm 20 đĩa DVD đầu tiên (đúng giới hạn cho phép)
        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i+1}")
            cart.add_dvd(dvd)
            
        # Thêm đĩa thứ 21 (vượt quá giới hạn MAX_NUMBERS_ORDERED = 20)
        dvd_21 = DigitalVideoDisc("DVD 21")
        result = cart.add_dvd(dvd_21)
        
        self.assertFalse(result, "Giỏ hàng phải từ chối khi thêm đĩa thứ 21 vượt quá giới hạn cho phép")

if __name__ == '__main__':
    unittest.main()