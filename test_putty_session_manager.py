import putty_session_manager as psm
from unittest import TestCase

DEFAULT_SESSION = 'Default%20Settings'
AUX_SESSION = 'test-case-session'
NO_SUCH_SESSION = 'no_such_session'

def delete_aux_session():
    """
    Delete auxiliary session if it exists
    """
    try:
        psm.delete(Container({'session': AUX_SESSION}))
    except psm.SessionNotFoundError as e:
        print('"%s" does not exist' % (AUX_SESSION))

class Container(object):
    """
    A helper class to instantiate objects with attributes
    from a given dictionary
    """
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

class GetTest(TestCase):

    def test_get_default_session(self):
        try:
            psm.get(Container({'session': DEFAULT_SESSION}))
        except Exception as err:
            self.fail(
                '%s raised unexpected error "%s": "%s"' \
                % ('get', err.__class__.__name__, err)
            )

    def test_get_no_such_session(self):
        self.assertRaises(
            psm.SessionNotFoundError, 
            psm.get,
            Container({'session': NO_SUCH_SESSION})
        )

class ListTest(TestCase):

    def test_should_not_fail(self):
        try:
            psm.list(Container({}))
        except Exception as err:
            self.fail(
                '%s raised unexpected error "%s": "%s"' \
                % ('list', err.__class__.__name__, err)
            )

class CopyAttrTest(TestCase):

    def test_fail_on_wrong_from_session(self):
        self.assertRaises(
            psm.SessionNotFoundError,
            psm.copy_attr,
            Container({'from_session': NO_SUCH_SESSION,
                       'to_session_pattern': NO_SUCH_SESSION,
                       'attr_pattern': '*'})
        )

    def test_fail_on_wrong_to_session(self):
        self.assertRaises(
            psm.SessionNotFoundError,
            psm.copy_attr,
            Container({'from_session': DEFAULT_SESSION,
                       'to_session_pattern': NO_SUCH_SESSION,
                       'attr_pattern': '.*'})
        )

    def test_fail_when_attributes_not_found(self):
        self.assertRaises(
            psm.SessionAttributeNotFoundError,
            psm.copy_attr,
            Container({'from_session': DEFAULT_SESSION,
                       'to_session_pattern': DEFAULT_SESSION,
                       'attr_pattern': 'no_such_attribute'})
        )

    def test_copy_attr_should_not_fail(self):
        try:
            psm.copy(Container({'source': DEFAULT_SESSION,
                                'dest': AUX_SESSION}))
            psm.copy_attr(Container({'from_session': DEFAULT_SESSION,
                                     'to_session_pattern': AUX_SESSION,
                                     'attr_pattern': '.*'}))
        except Exception as e:
            self.fail(
                '%s raised unexpected error "%s": "%s"' \
                % ('copy-attr', err.__class__.__name__, err)
            )


    def tearDown(self):
        delete_aux_session()

class CopyTest(TestCase):

    def test_fail_on_wrong_src_session(self):
        self.assertRaises(
            psm.SessionNotFoundError,
            psm.copy,
            Container({'source': NO_SUCH_SESSION,
                       'dest': NO_SUCH_SESSION})
        )

    def test_copy_should_not_fail(self):
        try:
            psm.copy(Container({'source': DEFAULT_SESSION,
                                'dest': AUX_SESSION}))
            psm.delete(Container({'session': AUX_SESSION}))
        except Exception as e:
            self.fail(
                '%s raised unexpected error "%s": "%s"' \
                % ('copy', err.__class__.__name__, err)
            )

    def tearDown(self):
        delete_aux_session()

class ComplexTest(TestCase):

    def test_get_after_copy_should_work(self):
        try:
            psm.copy(Container({'source': DEFAULT_SESSION,
                                'dest': AUX_SESSION}))
            psm.get(Container({'session': AUX_SESSION}))
        except Exception as e:
            self.fail(
                '%s raised unexpected error "%s": "%s"' \
                % ('copy', err.__class__.__name__, err)
            )

    def tearDown(self):
        delete_aux_session()

if __name__ == "__main__":
    import unittest
    unittest.main()
