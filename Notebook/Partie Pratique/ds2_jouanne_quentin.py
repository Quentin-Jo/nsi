def creer_pile():
    '''Renvoie une pile vide'''
    return []

def est_vide(pile):
    '''Renvoie un booléen, True si la pile est vide et False sinon'''
    return pile == []

def empiler(pile, element):
    '''Empile element au sommet de pile'''
    pile.append(element)
    
def depiler(pile):
    '''Renvoie et enlève la valeur du sommet de pile'''
    assert not est_vide(pile), "Pile vide"
    return pile.pop()


def sommet(pile):
    ''' Renvoie la valeur au sommet de la pile mais sans la supprimer de la pile '''
    if est_vide(pile):
        raise IndexError('pile vide')
    else:
        valeur = depiler(pile)
        empiler(pile, valeur)
    return valeur




def mettre_disques(pile, n):
    for i in range(n, 0, -1):
        empiler(pile, i)

def creation_tours(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''
    p0 = creer_pile()
    p1 = creer_pile()
    p2 = creer_pile()
    mettre_disques(p0, n)
    return [p0, p1, p2]


def deplacer(tours, origine, cible):
    p0 = tours[origine]
    p1 = tours[cible]
    if not est_vide(p0):
        if est_vide(p1) or sommet(p1) > sommet(p0):
            empiler(p1, depiler(p0))

def resoudre(tours, n, origine, cible, interm):
    if n == 1:
        deplacer(tours, origine, cible)
    else:
        resoudre(tours, n-1, origine, interm, cible)
        deplacer(tours, origine, cible)
        resoudre(tours, n-1, interm, cible, origine)


def nb_etapes(n):
    if n == 1:
        return 1
    else:
        return 2*nb_etapes(n-1) + 1