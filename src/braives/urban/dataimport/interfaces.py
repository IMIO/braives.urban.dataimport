# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.theme.interfaces import IDefaultPloneLayer

from imio.urban.dataimport.interfaces import IMapper, IUrbanImportSource, IUrbanDataImporter


class IBraivesUrbanDataimportLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class IbraivesDataImporter(IUrbanDataImporter):
    """ marker interface for Thuin Agorawin importer """
