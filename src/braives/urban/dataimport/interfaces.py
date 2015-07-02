# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.theme.interfaces import IDefaultPloneLayer

from imio.urban.dataimport.interfaces import IUrbanDataImporter


class IBraivesUrbanDataimportLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class IArchitectsImporter(IUrbanDataImporter):
    """ marker interface for Braives Architects importer """


class IBraivesDataImporter(IUrbanDataImporter):
    """ marker interface for Braives acropole importer """
