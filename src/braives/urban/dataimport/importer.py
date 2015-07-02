# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.acropole.importer import AcropoleDataImporter
from imio.urban.dataimport.csv.importer import CSVDataImporter
from braives.urban.dataimport import objectsmapping
from braives.urban.dataimport import valuesmapping
from braives.urban.dataimport.interfaces import IArchitectsImporter
from braives.urban.dataimport.interfaces import IBraivesDataImporter
from imio.urban.dataimport.mapping import ObjectsMapping
from imio.urban.dataimport.mapping import ValuesMapping


class BraivesDataImporter(AcropoleDataImporter):
    """ """

    implements(IBraivesDataImporter)


class BraivesArchitectsImporter(CSVDataImporter):
    """ """

    implements(IArchitectsImporter)


class ArchitectsMapping(ObjectsMapping):
    """ """

    def getObjectsNesting(self):
        return objectsmapping.OBJECTS_NESTING

    def getFieldsMapping(self):
        return objectsmapping.FIELDS_MAPPINGS


class ArchitectsValuesMapping(ValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):
        return valuesmapping.VALUES_MAPS.get(mapping_name, None)
