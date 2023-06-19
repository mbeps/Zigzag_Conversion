import pytest

def test_zigzag_conversion_1():
    solution = Solution()
    result = solution.convert("PAYPALISHIRING", 3)
    assert result == "PAHNAPLSIIGYIR"

def test_zigzag_conversion_2():
    solution = Solution()
    result = solution.convert("PAYPALISHIRING", 4)
    assert result == "PINALSIGYAHRPI"

def test_zigzag_conversion_3():
    solution = Solution()
    result = solution.convert("A", 1)
    assert result == "A"

def test_zigzag_conversion_4():
    solution = Solution()
    result = solution.convert("AB", 1)
    assert result == "AB"

def test_zigzag_conversion_5():
    solution = Solution()
    result = solution.convert("ABCD", 2)
    assert result == "ACBD"
