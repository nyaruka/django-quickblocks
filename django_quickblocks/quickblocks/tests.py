from django import template
from django.test import TestCase
from mock import Mock

class TestLoadQuickBlocksNode(TestCase):
    
    def test_load_quickblocks():
        parser = Mock()
        token = Mock(methods=['split_contents'])
        token.split_contents.return_value = ('load_qbs', 'test_blocks')

        import pdb; pdb.set_trace()
