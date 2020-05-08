############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, 
                is_bestseller):
        """Initialize a melon."""
    
        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk','Muskmelon',1998,'green',True,True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas','Casaba',2003,'orange',False,False)
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    all_melon_types.append(cas)

    cren = MelonType('cren','Crenshaw',1996,'green',False,False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw','Yellow Watermelon',2013,'yellow',False,True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types

melon_types = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        pairs = ', '.join(melon.pairings)
        print(f'{melon.name} pairs with {pairs}')

print_pairing_info(melon_types)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_types:
        key = melon.code
        value = melon
        melon_dict[key] = value

    return melon_dict

melons_by_id = make_melon_type_lookup(melon_types)

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, 
                harvest_location, harvested_by):
        """Initialize a melon."""
    
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_location = harvest_location
        self.harvested_by = harvested_by

    def is_sellable(melon):
        
        if melon.shape_rating > 5 and melon.color_rating > 5 and melon.harvest_location != 'Field 3':
            return True
        else:
            return False

    is_sellable(melon)

def make_melons(melons_by_id):
    """Returns a list of Melon objects."""

    #need to define is_sellable

    all_harvested_melons = []

    melon1 = Melon(melons_by_id['yw'],8,7,'Field 2','Sheila')
    all_harvested_melons.append(melon1)

    melon2 = Melon(melons_by_id['yw'],3,4,'Field 2','Sheila')
    all_harvested_melons.append(melon2)

    melon3 = Melon(melons_by_id['yw'],9,8,'Field 3','Sheila')
    all_harvested_melons.append(melon3)

    melon4 = Melon(melons_by_id['cas'],10,6,'Field 35','Sheila')
    all_harvested_melons.append(melon4)

    melon5 = Melon(melons_by_id['cren'],8,9,'Field 35','Michael')
    all_harvested_melons.append(melon5)

    melon6 = Melon(melons_by_id['cren'],8,2,'Field 35','Michael')
    all_harvested_melons.append(melon6)

    melon7 = Melon(melons_by_id['cren'],2,3,'Field 4','Michael')
    all_harvested_melons.append(melon7)

    melon8 = Melon(melons_by_id['musk'],6,7,'Field 4','Michael')
    all_harvested_melons.append(melon8)

    melon9 = Melon(melons_by_id['yw'],7,10,'Field 3','Sheila')
    all_harvested_melons.append(melon9)

    return all_harvested_melons

harvested_melons = make_melons(melons_by_id) 


def get_sellability_report(harvested_melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in harvested_melons:
        if is_sellable(melon) == True:
            sellable = '(CAN BE SOLD)'
        else:
            sellable = '(NOT SELLABLE)'

        print(f'Harvested by {melon.harvested_by} from {harvest_location} {sellable}')

get_sellability_report(harvested_melons)


