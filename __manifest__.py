{
    'name': 'odoo1',
    'version': '16.0.1',
    'category': 'purchase',
    'summary': 'purchase custome module',
    'description': 'purchase module',
    'website': '',
    'author': 'nando',
    'depends': ['web','base'],
    'date': [
        'security/ir.model.access.csv',
        'views/nando_purchase.view.xml',
        'views/nando_purchase.menuitem.xml',
        'views/nando_purchase.action.xml'
    ],
    'installable': True,

}