from django.test import TestCase
from .models import Editor, tags, Article

# Create your tests here.
class EditorTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.caren = Editor(first_name = 'Caren', last_name = 'Chepkorir', email = 'karenkoech3@gmail.com')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.caren,Editor))

       