import pandas

glottolog = pandas.read_csv('glottolog.csv', delimiter=',', header=0)
warnings = []

'''
get_affiliations(('Russian', 'English'))
>>> ['Indo-European, Balto-Slavic, Slavic, East Slavic', 'Indo-European, ...']
'''
def get_affiliations(languages):
    affiliations = []
    for language in languages:
        affiliation_id = tuple(glottolog[glottolog.Name == language].Classification)
        if not affiliation_id:
            affiliation = ''
            print('(get_affiliations) Warning: affiliation for {} not found'.format(language))
        else:
            affiliation = []
            affiliation_id = affiliation_id[0].split('/')
            for taxon in affiliation_id:
                affiliation.append(tuple(glottolog[glottolog.ID == taxon].Name)[0])
            affiliation = ', '.join(affiliation)
        affiliations.append(affiliation)
    return affiliations

'''
get_coordinates('Russian')
>>> (59.0, 50.0)
'''
def get_coordinates(language):
    latitude = glottolog[glottolog.Name == language].Latitude
    longitude = glottolog[glottolog.Name == language].Longitude
    if not list(latitude) or not list(longitude):
        global warnings
        warnings.append(language)
        #print('(get_coordinates) Warning: coordinates for {} not found'.format(language))
    else:
        return (float(latitude), float(longitude))


'''
get_glot_id('Russian')
>>> russ1263
'''
def get_glot_id(language):
    glot_id = tuple(glottolog[glottolog.Name == language].ID)
    if not glot_id:
        print('(get_glot_id) Warning: Glottolog ID for {} not found'.format(language))
    else:
        return glot_id[0]

'''
get_macro_area('Russian')
>>> Eurasia
'''
def get_macro_area(language):
    macro_area = tuple(glottolog[glottolog.Name == language].Macroarea)
    if not macro_area:
        print('(get_macro_area) Warning: Macro area for {} not found'.format(language))
    else:
        return macro_area[0]


'''
get_iso('Russian')
>>> rus
'''
def get_iso(language):
    iso = tuple(glottolog[glottolog.Name == language].ISO639P3code)
    if not iso:
        print('(get_iso) Warning: ISO for {} not found'.format(language))
    else:
        return iso[0]

#---------------------------------------------------------------------------------

'''
get_by_affiliation('Indo-European, Slavic, East')
>>> ('Ukrainian', 'Rusyn', 'Russian', 'Belarusian')
def get_by_affiliation(affiliation):
    languages = tuple(glottolog[glottolog.affiliation == affiliation].language)
    if not languages:
        print('(get_by_affiliation) Warning: languages by {} not found'.format(affiliation))
    else:
        return languages
'''

'''
get_by_iso('rus')
>>> Russian
'''
def get_by_iso(iso):
    language = tuple(glottolog[glottolog.ISO639P3code == iso].Name)
    if not language:
        print('(get_by_iso) Warning: language by {} not found'.format(iso))
    else:
        return language[0]

'''
get_by_glot_id('russ1263')
>>> Russian
'''
def get_by_glot_id(glot_id):
    language = tuple(glottolog[glottolog.ID == glot_id].Name)
    if not language:
        print('(get_by_glot_id) Warning: language by {} not found'.format(glot_id))
    else:
        return language[0]

#---------------------------------------------------------------------------------

'''
get_glot_id_by_iso('rus')
>>> russ1263
'''
def get_glot_id_by_iso(iso):
    glot_id = tuple(glottolog[glottolog.ISO639P3code == iso].ID)
    if not glot_id:
        print('(get_glot_id_by_iso) Warning: glot_id by {} not found'.format(iso))
    else:
        return glot_id[0]

'''
get_iso_by_glot_id('russ1263')
>>> rus
'''
def get_iso_by_glot_id(glot_id):
    iso = tuple(glottolog[glottolog.ID == glot_id].ISO639P3code)
    if not iso:
        print('(get_iso_by_glot_id) Warning: ISO by {} not found'.format(iso))
    else:
        return iso[0]
