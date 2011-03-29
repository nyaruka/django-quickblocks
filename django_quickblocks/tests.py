from mock import Mock
from django.test import TestCase
from django.contrib.auth.models import User
from django_quickblocks.models import QuickBlockType, QuickBlock
from django_quickblocks.templatetags.quickblocks import do_load_quickblocks, LoadQuickBlocksNode

class TestQuickblocks(TestCase):
    
    def test_load_quickblocks(self):
        parser = Mock()
        token = Mock(['split_contents',])

        token.split_contents.return_value = ('load_qbs', 'test_blocks')
        node = do_load_quickblocks(parser, token)

        self.assertEquals("test_blocks", node.slug)

        token.split_contents.return_value = ('load_qbs', '"test_blocks"')
        node = do_load_quickblocks(parser, token)

        self.assertEquals("test_blocks", node.slug)

        token.split_contents.return_value = ('load_qbs', "'test_blocks'")
        node = do_load_quickblocks(parser, token)

        self.assertEquals("test_blocks", node.slug)

        
    def test_node(self):
        node = LoadQuickBlocksNode('test', False)

        # create context dictionary
        context = {}
        
        value = node.render(context)

        self.assertEquals('<b><font color="red">QuickBlockType with slug: "test" not found.</font></b>', value)

        self.assertFalse('test' in context)

        # create quickblocktype and quickblocks
        user = User.objects.create_user('eugene','eugene@nyaruka.com','glue')
        blocktype = QuickBlockType.objects.create(slug='another_test',description='testing...',owner=user)
        QuickBlock.objects.create(title='Hahahaha....',content='Oh my God! Hahahahaaa...',type=blocktype,owner=user)
        QuickBlock.objects.create(title='Wow....',content='Oh my God! Wowwwww...',type=blocktype,owner=user)

        node = LoadQuickBlocksNode('another_test', False)
        
        context['another_test'] = QuickBlock.objects.filter(type=blocktype)
        
        value = node.render(context)

        self.assertTrue('another_test' in context)
        self.assertEqual('', value)


        

        
