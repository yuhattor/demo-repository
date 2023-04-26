import unittest

def multiply(a, b):
    if a == "a" or b == "a":
        raise ValueError("a is not a number")
    if a == 0.1 or b == 0.1:
        raise ValueError("0.1 is not an integer")
    return a * b

# multiply()のテストコードを以下の条件に従って書いてください。
# Condition: 成功ケースを含める
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        # 2つの正の整数を入力した場合、正しい結果を返すことを確認する。
        self.assertEqual(multiply(3, 4), 12)
        # 2つの負の整数を入力した場合、正しい結果を返すことを確認する。
        self.assertEqual(multiply(-3, -4), 12)
        # 1つの正の整数と1つの負の整数を入力した場合、正しい結果を返すことを確認する。
        self.assertEqual(multiply(3, -4), -12)
        # 1つの入力が0である場合、結果が0であることを確認する。
        self.assertEqual(multiply(3, 0), 0)
        # 1つの入力が小数である場合、エラーが発生することを確認する。
        self.assertRaises(ValueError, multiply, 3, 0.1)
        # 1つの入力が文字列である場合、エラーが発生することを確認する。
        self.assertRaises(ValueError, multiply, 3, "a")
        # 整数以外の入力が与えられた場合、エラーが発生することを確認する。
        self.assertRaises(TypeError, multiply, 3, self)

unittest.main()