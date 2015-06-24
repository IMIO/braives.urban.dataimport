# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm
from imio.urban.dataimport.acropole.settings import AcropoleImporterFromImportSettings


class BraivesImporterSettingsForm(ImporterSettingsForm):
    """ """


class BraivesImporterSettings(ImporterSettings):
    """ """
    form = BraivesImporterSettingsForm


class BraivesImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = BraivesImporterSettings


class BraivesImporterFromImportSettings(AcropoleImporterFromImportSettings):
    """ """

    def get_importer_settings(self):
        """
        Return the db name to read.
        """
        settings = super(BraivesImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': 'urb64015ac',
        }

        settings.update(db_settings)

        return settings
