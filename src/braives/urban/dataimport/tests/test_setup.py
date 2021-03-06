# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from braives.urban.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of braives.urban.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if braives.urban.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('braives.urban.dataimport'))

    def test_uninstall(self):
        """Test if braives.urban.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['braives.urban.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('braives.urban.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IBraivesUrbanDataimportLayer is registered."""
        from braives.urban.dataimport.interfaces import IBraivesUrbanDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(IBraivesUrbanDataimportLayer in utils.registered_layers())
