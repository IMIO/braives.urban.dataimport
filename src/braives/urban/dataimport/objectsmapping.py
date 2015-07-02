# -*- coding: utf-8 -*-

from braives.urban.dataimport.mappers import AddressMapper
from braives.urban.dataimport.mappers import ArchitectFactory
from braives.urban.dataimport.mappers import IdMapper
from braives.urban.dataimport.mappers import PersonTitleMapper
from braives.urban.dataimport.mappers import PhoneMapper

from imio.urban.dataimport.mapper import SimpleMapper


OBJECTS_NESTING = [
    ('ARCHITECT', [],),
]

FIELDS_MAPPINGS = {
    'ARCHITECT':
    {
        'factory': [ArchitectFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'Nom',
                    'to': 'name1',
                },
                {
                    'from': 'Prénom',
                    'to': 'name2',
                },
                {
                    'from': 'Code postal',
                    'to': 'zipcode',
                },
                {
                    'from': 'Localité',
                    'to': 'city',
                },
                {
                    'from': 'Email',
                    'to': 'email',
                },
                {
                    'from': 'Fax',
                    'to': 'fax',
                },
            ),

            IdMapper: {
                'from': 'Nom',
                'to': 'id',
            },

            PersonTitleMapper: {
                'from': 'Civilité Doc',
                'to': 'personTitle',
            },

            AddressMapper: {
                'from': 'Adresse',
                'to': ('street', 'number')
            },

            PhoneMapper: {
                'from': ('Téléphone', 'Gsm'),
                'to': 'phone',
            },
        },
    },
}
