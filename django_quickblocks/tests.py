from mock import Mock
from django.test import TestCase
from django.contrib.auth.models import User
from django_quickblocks.models import QuickBlockType, QuickBlock
from django_quickblocks.templatetags.quickblocks import do_load_quickblocks

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

        
    def test_quickblock_render(self):
        # create quickblocktype and quickblocks
        user = User.objects.create_user('eugene','eugene@nyaruka.com','glue')
        blocktype = QuickBlockType.objects.create(slug='test',description='testing...',owner=user)
        QuickBlock.objects.create(title='Hahahaha....',content='Oh my God! Hahahahaaa...',type=blocktype,owner=user)
        QuickBlock.objects.create(title='Wow....',content='Oh my God! Wowwwww...',type=blocktype,owner=user)

        
        # create context just a dictionary
        context = {}
        # test if the quickblocktype doesntexists

        self.assertFalse(blocktype, QuickBlockType.objects.get(slug='test'))
        self.assertRaises(QuickBlockType.DoesNotExist, QuickBlockType.objects.get(slug='raise_exception'))

        # test if the quickblocktype exists
        self.assertEquals(blocktype, QuickBlockType.objects.get(slug='test'))

        blocks = QuickBlock.objects.filter(type=blocktype.pk)

        context['test'] = blocks

        # test if the context contains blocks
        self.assertEquals(blocks, context['test'])
