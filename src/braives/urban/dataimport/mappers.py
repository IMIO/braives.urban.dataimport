# -*- coding: utf-8 -*-

from imio.urban.dataimport.mapper import Mapper
from imio.urban.dataimport.factory import BaseFactory

from Products.CMFPlone.utils import normalizeString

import re


# Factory
class ArchitectFactory(BaseFactory):
    def getCreationPlace(self, factory_args):
        return self.site.urban.architects

    def getPortalType(self, container, **kwargs):
        return 'Architect'


class IdMapper(Mapper):
    def mapId(self, line):
        name = '%s' % self.getData('Nom')
        name = name.replace(' ', '').replace('-', '')
        contact_id = normalizeString(self.site.portal_urban.generateUniqueId(name))
        return contact_id


class AddressMapper(Mapper):

    regex = '(\D*?)(?:(?:,?\s*)|(?:n°\s*))(\d.*)'

    def mapStreet(self, line):
        address = self.getData('Adresse')
        street = re.search(self.regex, address).group(1)
        return street

    def mapNumber(self, line):
        address = self.getData('Adresse')
        number = re.search(self.regex, address).group(2)
        return number


class PersonTitleMapper(Mapper):
    def mapPersontitle(self, line):
        title = self.getData('Civilité Doc')
        title_mapping = self.getValueMapping('titre_map')
        return title_mapping.get(title, 'notitle')


class PhoneMapper(Mapper):
    def mapPhone(self, line):
        phone = self.getData('Téléphone')
        gsm = self.getData('Gsm')

        if (phone and phone != '-') and (gsm and gsm != '-'):
            phones = '{phone}, {gsm}'.format(
                phone=phone,
                gsm=gsm,
            )
            return phones
        elif phone and phone != '-':
            return phone
        elif gsm and gsm != '-':
            return gsm

        return ''
