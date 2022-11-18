def creer_pile():
    '''Renvoie une pile vide'''
    return []

def est_vide(pile):
    '''Renvoie un booléen, True si la pile est vide et False sinon'''
    return p == []

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
        raise IndexError('Pile Vide')
    return pile[-1]




def mettre_disques(pile, n):
    '''met des disques de taille n à 1 sur la pile'''
    for i in range(n):
        empiler(pile, n)
        n = n-1


def creation_tours(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''
    p1 = creer_pile()
    p2 = creer_pile()
    p3 = creer_pile()
    liste_tours = []
    for i in range(n):
        empiler(p1, n)
        n = n-1
    liste_tours.append(p1)
    liste_tours.append(p2)
    liste_tours.append(p3)

    return liste