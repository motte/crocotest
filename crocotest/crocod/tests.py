import time


from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse
from django.utils import unittest
from django.template import Context, Template
from django.test.client import Client

from .models import Example, NullableExample

TEST_DOC_DATA = (
    '%PDF-1.7\n\n1 0 obj  % entry point\n<<\n  /Type /Catalog\n  /Pages 2 0 '
    'R\n>>\nendobj\n\n2 0 obj\n<<\n  /Type /Pages\n  /MediaBox [ 0 0 200 200 '
    ']\n  /Count 1\n  /Kids [ 3 0 R ]\n>>\nendobj\n\n3 0 obj\n<<\n  /Type '
    '/Page\n  /Parent 2 0 R\n  /Resources <<\n    /Font <<\n      /F1 4 0 R \n'
    '    >>\n  >>\n  /Contents 5 0 R\n>>\nendobj\n\n4 0 obj\n<<\n  /Type '
    '/Font\n  /Subtype /Type1\n  /BaseFont /Times-Roman\n>>\nendobj\n\n5 0 obj'
    '  % page content\n<<\n  /Length 44\n>>\nstream\nBT\n70 50 TD\n/F1 12 '
    'Tf\n(Hello, world!) Tj\nET\nendstream\nendobj\n\nxref\n0 6\n0000000000 '
    '65535 f \n0000000010 00000 n \n0000000079 00000 n \n0000000173 00000 n '
    '\n0000000301 00000 n \n0000000380 00000 n \ntrailer\n<<\n  /Size 6\n  '
    '/Root 1 0 R\n>>\nstartxref\n492\n%%EOF\n'
)
TEST_DOC_NAME = 'test_doc_file.pdf'

client = Client()

def initial_setup():
    example = Example.objects.create(
        name = 'Test item',
        document = SimpleUploadedFile(TEST_DOC_NAME, TEST_DOC_DATA))

    instance = Example.objects.get(id=example.id)
    return instance

Class CrocoTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.instance = initial_setup()
    
    def setUp(self):
        time.sleep(1)
