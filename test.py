import unittest
import c1
import c2
import c3


class TestC1(unittest.TestCase):
    def test_1(self):
        """
        Provided test case 1
        """
        input_ = "1 2 3 4 7 8 9 11 13"
        expected = "1-4 7-9"
        output = c1.sequence_finder(input_)
        self.assertEqual(output, expected)
    def test_2(self):
        """
        Provided test case 2
        """
        input_ = "1 2 3 5 6 7 9 10 11 12"
        expected = "1-3 5-7 9-12"
        output = c1.sequence_finder(input_)
        self.assertEqual(output, expected)
    def test_3(self):
        """
        Provided test case 3
        """
        input_ = "1 3 5 6 7 9 11 12 13"
        expected = "5-7 11-13"
        output = c1.sequence_finder(input_)
        self.assertEqual(output, expected)
    def test_4(self):
        """
        Additional test case
        """
        input_ = "1 2"
        expected = "1-2"
        output = c1.sequence_finder(input_)
        self.assertEqual(output, expected)
    def test_5(self):
        """
        Additional test case
        """
        input_ = "1 3 4 5 6 7 9"
        expected = "3-7"
        output = c1.sequence_finder(input_)
        self.assertEqual(output, expected)
    def test_6(self):
        """
        Additional test case
        """
        input_ = "1 2 3 4 9 12 13 14 99 102 103 104 107"
        expected = "1-4 12-14 102-104"
        output = c1.sequence_finder(input_)
        self.assertEqual(output, expected)


class TestC2(unittest.TestCase):
    def test_1(self):
        """
        Provided test case 1
        """
        input_ = "9f"
        expected = 159
        output = c2.hex_to_dec(input_)
        self.assertEqual(output, expected)
    def test_2(self):
        """
        Provided test case 2
        """
        input_ = "11"
        expected = 17
        output = c2.hex_to_dec(input_)
        self.assertEqual(output, expected)
    def test_3(self):
        """
        Test some random numbers
        """
        input_ = "0"
        expected = int("0", 16)
        output = c2.hex_to_dec(input_)
        self.assertEqual(output, expected)
    def test_4(self):
        """
        Test a bunch of numbers
        """
        nums = [x for x in range(0, 1024, 1)]
        for num in nums:
            input_ = hex(num).lstrip("0x")
            output = c2.hex_to_dec(input_)
            self.assertEqual(output, num)
    def test_5(self):
        """
        Test a big number for fun
        """
        input_ = "ffffffd51"
        expected = int("ffffffd51", 16)
        output = c2.hex_to_dec(input_)
        print(output)
        self.assertEqual(output, expected)


class TestC3(unittest.TestCase):
    def test_1(self):
        """
        Provided test case 1
        """
        text = "No More Secrets."
        ascii_cipher = c3.AsciiCipher()
        cipher_text = ascii_cipher.encrypt(text)
        print(cipher_text)
        output = ascii_cipher.decrypt(cipher_text)
        self.assertEqual(output, text)


if __name__ == '__main__':
    unittest.main()
