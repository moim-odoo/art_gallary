{
    'name' : 'Art Gallary',
    'application' : True,
    'depends' : ['base',],
    'data':[
            'security/ir.model.access.csv',
            'view/art_gallary_artist_view.xml',
            'view/art_gallary_artworks_view.xml',
            'view/art_gallary_user_view.xml',
            'view/art_gallary_interaction_view.xml',
            'view/art_gallary_menus.xml',
            
    ],
    'demo':[
        'demo/artwork_demo.xml',
        'demo/artist_demo.xml',
        'demo/users_demo.xml',
        'demo/interaction_demo.xml',
        
    ]

}