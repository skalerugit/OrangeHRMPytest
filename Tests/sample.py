

import pytest
import re
from Utils import utility


class Test_sample:

    @pytest.mark.parametrize("str_object", ["hello", "test"])
    def test_sorted(self, str_object):
        print("".join(sorted(str_object)))

    @pytest.mark.parametrize("num, output", [(1, 11), (2, 22), (3, 33), (4, 44)])
    def test_multiplication_11(self, num, output):
        assert 11 * num == output

    @pytest.mark.parametrize("list1", [["name", "age"]])
    @pytest.mark.parametrize("list2", [["Ram", 29]])
    def test_merge_two_lists(self, list1, list2):
        print(dict(zip(list1, list2)))

    @pytest.mark.parametrize("list1", [["cat", "cat", "dog"], ["BMW", "Hyundai", "Mercedes", "BMW"]])
    @pytest.mark.parametrize("str_object", ["cat", "BMW"])
    def test_occurences_of_word(self, list1, str_object):
        list2 = [index for index, value in enumerate(list1) if value == str_object]
        print(list2)

    @pytest.mark.parametrize("str_object", ["hello"])
    def test_reverse_string(self, str_object):
        print(str_object[::-1])

    @pytest.mark.parametrize("ip_address", ["122.134.3.123"])
    def test_validate_ip_address(self, ip_address):
        regexIP = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?).(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?).(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?).(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

        if re.search(regexIP, ip_address):
            print("Valid IP address")

        else:
            print("Invalid IP address")

    @pytest.mark.parametrize("str_object", ["75.7, 77.7, 88.9, 34.6, 73.5"])
    def test_calculate_avg_sum(self, str_object):
        temp = []
        str_object = str_object.split(",")
        for i in range(len(str_object)):
            value = float(str_object[i])
            temp.append(value)
        print(temp)
        sum_of_str = sum(temp)
        avg_of_str = sum(temp) / len(str_object)
        print("The Sum is {} and average is {}".format(round(sum_of_str, 2), round(avg_of_str, 2)))

    @pytest.mark.parametrize("str_object", ["hello welcome to world of python programming"])
    def test_reverse_of_words_in_string(self, str_object):
        str_object = str_object.split(" ")
        reverse = str_object[-1::-1]
        print(" ".join(reverse))

    @pytest.mark.parametrize("num1, num2", [(10, 20)])
    def test_swap_numbers(self, num1, num2):
        print("Before swapping the numbers are {}, {}".format(num1, num2))
        num1, num2 = num2, num1
        print("After swapping the numbers are {}, {}".format(num1, num2))

    @pytest.mark.parametrize("list1", [[10, 20, 40, 60, 80, 34, 8]])
    def test_max_min_in_list(self, list1):
        print("The maximum number in the given {} is {}".format(list1, max(list1)))
        print("The minimum number in the given {} is {}".format(list1, min(list1)))

    @pytest.mark.parametrize("list1", [[10, 20, 40, 60, 80, 55]])
    def test_reverse_of_list(self, list1):
        print(list1[-1::-1])

    @pytest.mark.parametrize("s", ["hello"])
    def test_reverseString1(self, s: list[str]) -> None:
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l + 1, r - 1)

        reverse(0, len[s] - 1)

    @pytest.mark.parametrize("maybe_palindrome, expected_result", [
        ("", True),
        ("a", True),
        ("Bob", True),
        ("madam", True),
        ("Do geese see God?", True),
        ("abc", False),
        ("abab", False),
    ])
    def test_is_palindrome(self, utils, maybe_palindrome, expected_result):
        assert utils.is_palindrome(maybe_palindrome) == expected_result

    @pytest.mark.parametrize("str_object, expected_result", [
        ("hello", "olleP"),
        ("madam", "madam"),
        ("1234", "4321"),
        ('', ''),
        ('a', 'a'),
        ('aaaa', 'aaaa'),
        ('abc', 'cba'),
        ('testing416', '614gnitset'),
        ('#CLF C01', '10C FLC#'),
        ('b', 'c')
    ])
    def test_reverse_string(self, utils, str_object, expected_result):
        assert utils.reverseString(str_object) == expected_result



