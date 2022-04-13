class Voiture(object):
    def __init__(self, marque, couleur):
        self.marque= marque
        self.couleur= couleur
        self.conducteur='personne'
        self.vitesse= 0
    def choisirConducteur(self, nom):
        self.conducteur= nom
    def affich_info(self, marque, couleur, conducteur, vitesse):
        print(self, marque, couleur, conducteur, vitesse)

maVoiture= Voiture('Ford','rouge')
taVoiture= Voiture('toyota','bleue')
saVoiture= Voiture('Ford','noir')

maVoiture.choisirConducteur('hassan')
taVoiture.choisirConducteur('afid')
saVoiture.choisirConducteur('ali')
maVoiture.affich_info()

