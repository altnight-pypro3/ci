import unittest
from django.test import TestCase as DjangoTest

from menu.models import Tea
from menu.forms import TeaSearchForm


class TeaManagerTest(DjangoTest):
    def setUp(self):
        Tea.objects.bulk_create([
            Tea(price=100, name="ダージリン", kind="english"),
            Tea(price=100, name="スリランカ", kind="english"),
            Tea(price=100, name="ウーロン茶", kind="chinese"),
            Tea(price=100, name="鉄観音茶", kind="chinese"),
            Tea(price=100, name="プーアル茶", kind="chinese"),
            Tea(price=100, name="静岡茶", kind="japanese"),
        ])

    def test_count_each_kind(self):
        result = Tea.objects.count_each_kind()
        self.assertEqual(result, dict(english=2, chinese=3, japanese=1))


class TeaSearchFormTest(unittest.TestCase):
    def test_valid(self):
        """正常な入力をしたときにエラーにならないことを検証する。 """
        params = dict(name="foo", kind=["english"])
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), True, form.errors.as_text())

    def test_either1(self):
        """名称と種類のどちらも入力しないとエラーになることを検証する。 """
        params = dict()
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), False, form.errors.as_text())

    def test_either2(self):
        """名称を入力すればエラーにならないことを検証する。 """
        params = dict(name="foo")
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), True, form.errors.as_text())

    def test_either3(self):
        """種類を入力すればエラーにならないことを検証する。 """
        params = dict(kind=["english", "chinese"])
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), True, form.errors.as_text())
