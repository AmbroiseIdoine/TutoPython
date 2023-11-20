"""
Types et objets
"""

# Ceci est un commentaire: il n'est jamais pris en compte par Python et commence par '#'

### LES TYPES DE BASE ###

# les nombres

va = 45
vb = 2.65
vc = va+vb

print(vc)

# les chaines de caractères

vd = "Une Maison"
ve = "ze vaut 6,9 (€€€)"

print(ve)

# les booleens (vrai ou faux)

vf = False
vg = (vd==ve)

print(vg)

# les listes, dictionnaires et set

vh = [12,14,15]                                     # liste
vi = ["mais","ou","et","donc","or","ni","car"]      
vj = [False,"est",1,"booleen"]
vk = set("er","et","er","ui")                       # set
vl = {"chat":2,"chien":5}                           # dictionnaire
vm = {"bruit":100,
      "nom":"voiture",
      "agréable":False}

print(vm)

# les fonctions (permettent d'effectuer des opérations)

def vn(x,y):
    return x+y

def vo(name,commentaire="Eh oui!"):
    print(name)
    print(commentaire)
    return "%s %s"%(name,commentaire)

print(vn(4,7))
vo("c'est fort.")

# les classes

class vp:
    MA_CONSTANTE = "champagne"
    
    def __init__(self,nom,taille=1.87):
        self.nom = nom
        self.taille = taille
        
    def description(self):
        res = "Je m'appelle %s, mesure %f m et j'aime le %s."%(self.nom,self.taille,self.MA_CONSTANTE)
        print(res)
        return res
        
vp_instance = vp("Mc Gregor")
vp_instance.description()

