# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.acropole.importer import AcropoleDataImporter
from braives.urban.dataimport.interfaces import IBraivesDataImporter


class BraivesDataImporter(AcropoleDataImporter):
    """ """

    implements(IBraivesDataImporter)
