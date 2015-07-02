# -*- coding: utf-8 -*-

from braives.urban.dataimport.importer import BraivesArchitectsImporter
from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm
from imio.urban.dataimport.acropole.settings import AcropoleImporterFromImportSettings
from imio.urban.dataimport.csv.settings import CSVImporterFromImportSettings


class BraivesImporterSettingsForm(ImporterSettingsForm):
    """ """


class BraivesImporterSettings(ImporterSettings):
    """ """
    form = BraivesImporterSettingsForm


class BraivesImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = BraivesImporterSettings


class LicencesImporterFromImportSettings(AcropoleImporterFromImportSettings):
    """ """

    def get_importer_settings(self):
        """
        Return the db name to read.
        """
        settings = super(LicencesImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': 'urb64015ac',
        }

        settings.update(db_settings)

        return settings


class ArchitectsImporterFromImportSettings(CSVImporterFromImportSettings):
    """ """

    def __init__(self, settings_form, importer_class=BraivesArchitectsImporter):
        """
        """
        super(CSVImporterFromImportSettings, self).__init__(settings_form, importer_class)

    def get_importer_settings(self):
        """
        Return the csv file to read.
        """
        settings = super(ArchitectsImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'csv_filename': 'Architecte.csv',
            'key_column': 'Nom',
        }

        settings.update(db_settings)

        return settings
