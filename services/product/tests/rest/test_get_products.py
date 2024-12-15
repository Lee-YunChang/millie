from decimal import Decimal
from uuid import uuid4
from unittest.mock import MagicMock

from django.urls import reverse
from rest_framework.test import APITestCase

from utils.testcases.assertion import AssertionMixin


class TestProductList(AssertionMixin, APITestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('product-list')

    def test_get_products_no_category(self, mock_get_products, mock_build_response):
        mock_get_products.return_value = []
        mock_build_response.return_value = []

        res = self.client.get(self.url)
        self.assertOK(res)
        self.assertEqual(res.data['data'], [])

    def test_get_products_with_category(self, mock_get_products, mock_build_response):
        product_dto = MagicMock()
        product_dto.id = 1
        product_dto.name = "테스트 상품"
        product_dto.description = "테스트 설명"
        product_dto.price = Decimal('10000.00')
        product_dto.discount_rate = Decimal('5.00')
        product_dto.coupon_applicable = True
        category_mock = MagicMock(id=1, name="의류", description="의류 카테고리")
        product_dto.category = category_mock

        mock_get_products.return_value = [product_dto]
        mock_build_response.return_value = [{
            "id": 1,
            "name": "테스트 상품",
            "description": "테스트 설명",
            "price": "10,000.00",
            "category": {
                "id": 1,
                "name": "의류",
                "description": "의류 카테고리"
            },
            "coupon_applicable": True,
            "discount_rate": "5.00"
        }]

        res = self.client.get(self.url, {"category_id": 1})
        self.assertOK(res)
        data = res.data['data']
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "테스트 상품")
        self.assertEqual(data[0]['category']['name'], "의류")


class TestProductDetail(AssertionMixin, APITestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.product_id = 1
        cls.coupon_code = uuid4()
        cls.url = reverse('product-detail', args=[cls.product_id, cls.coupon_code])

    def test_get_product_detail_with_coupon(self, mock_get_product_detail, mock_build_detail_response):
        product_detail_dto = MagicMock()
        product_detail_dto.id = 1
        product_detail_dto.name = "상세 상품"
        product_detail_dto.description = "상세 설명"
        product_detail_dto.original_price = "10,000.00"
        product_detail_dto.discounted_price = "9,000.00"
        product_detail_dto.final_price = "8,500.00"
        category_mock = MagicMock(id=1, name="의류", description="의류 카테고리")
        product_detail_dto.category = category_mock
        product_detail_dto.coupon_applicable = True
        product_detail_dto.discount_rate = "10.00"

        mock_get_product_detail.return_value = product_detail_dto
        mock_build_detail_response.return_value = {
            "id": 1,
            "name": "상세 상품",
            "description": "상세 설명",
            "original_price": "10,000.00",
            "discounted_price": "9,000.00",
            "final_price": "8,500.00",
            "category": {
                "id": 1,
                "name": "의류",
                "description": "의류 카테고리"
            },
            "coupon_applicable": True,
            "discount_rate": "10.00"
        }

        res = self.client.get(self.url)
        self.assertOK(res)
        data = res.data['data']
        self.assertEqual(data['name'], "상세 상품")
        self.assertEqual(data['final_price'], "8,500.00")
        self.assertTrue(data['coupon_applicable'])

    def test_get_product_detail_no_coupon(self, mock_get_product_detail, mock_build_detail_response):
        # coupon_code를 빈 값으로 테스트 하기 위해 url 변경 또는 product_detail_view를 mocking하는 방법
        # 여기서는 coupon_code를 optional하게 받도록 view를 수정했거나, 별도의 url 패턴 사용을 가정
        url = reverse('product-detail', args=[self.product_id, uuid4()])
        product_detail_dto = MagicMock()
        product_detail_dto.id = 1
        product_detail_dto.name = "상세 상품"
        product_detail_dto.description = "상세 설명"
        product_detail_dto.original_price = "10,000.00"
        product_detail_dto.discounted_price = "10,000.00"  # 할인 없음
        product_detail_dto.final_price = "10,000.00"       # 쿠폰 없음
        category_mock = MagicMock(id=1, name="의류", description="의류 카테고리")
        product_detail_dto.category = category_mock
        product_detail_dto.coupon_applicable = False
        product_detail_dto.discount_rate = None

        mock_get_product_detail.return_value = product_detail_dto
        mock_build_detail_response.return_value = {
            "id": 1,
            "name": "상세 상품",
            "description": "상세 설명",
            "original_price": "10,000.00",
            "discounted_price": "10,000.00",
            "final_price": "10,000.00",
            "category": {
                "id": 1,
                "name": "의류",
                "description": "의류 카테고리"
            },
            "coupon_applicable": False,
            "discount_rate": None
        }

        res = self.client.get(url)
        self.assertOK(res)
        data = res.data['data']
        self.assertEqual(data['final_price'], "10,000.00")
        self.assertFalse(data['coupon_applicable'])
        self.assertIsNone(data.get('discount_rate'))
