from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from products.models import Product, Category, StockDrop


class TestProductViews(TestCase):

    def setUp(self):
        category = Category(name='clothing')
        category.save()

        valid_stockdrop = StockDrop(name='SD1',
                                    description='description',
                                    image=SimpleUploadedFile(
                                        name='default.png',
                                        content=open(
                                            'media/default.png', 'rb').read(),
                                        content_type='image/jpeg',))
        valid_stockdrop.save()

    def test_query_returns_results(self):
        response = self.client.get('/?query=retro')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_empty_query_returns_all_products(self):
        response = self.client.get('/?query=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')
        self.assertQuerysetEqual(response.context['products'],
                                 Product.objects.all().order_by(
                                     '-stock', '-popularity'),
                                 transform=lambda x: x)

    def test_render_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')
        self.assertTrue(response.context['stockdrops'])
        self.assertTrue(response.context['categories'])
        self.assertQuerysetEqual(response.context['products'],
                                 Product.objects.all().order_by(
                                     '-stock', '-popularity'),
                                 transform=lambda x: x)

    def test_render_product_detail(self):
        valid_product = Product.objects.latest('date_added')
        response = self.client.get(f'/product/{valid_product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertTrue(response.context['product'])
        self.assertTrue(response.context['categories_active'])

    def test_render_stockdrop_with_context(self):
        valid_stockdrop = StockDrop.objects.latest('date_added')
        response = self.client.get(f'/stockdrop/{valid_stockdrop.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/stockdrop_detail.html')
        self.assertTrue(response.context['stockdrops_active'])
        self.assertTrue(response.context['collection_active'])

    def test_render_category_with_context(self):
        valid_category = Category.objects.get(id=4)
        response = self.client.get(f'/category/{valid_category.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/category_detail.html')
        self.assertTrue(response.context['categories_active'])
        self.assertTrue(response.context['collection_active'])

    def test_render_404_not_found(self):
        response = self.client.get('/product/0/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed('404.html')
