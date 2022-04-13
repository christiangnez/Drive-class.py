class Voiture(object):
    def __init__(self, marque, couleur):
        self.marque= marque
        self.couleur= couleur
        self.conducteur='personne'
        self.vitesse= 0
    def choisirConducteur(self, nom):
        self.conducteur= nom
    def affich_info(self):
        print(self.marque, self.couleur, self.conducteur, self.vitesse)

maVoiture= Voiture('Ford','rouge')
taVoiture= Voiture('toyota','bleue')
saVoiture= Voiture('Ford','noir')

maVoiture.choisirConducteur('hassan')
taVoiture.choisirConducteur('afid')
saVoiture.choisirConducteur('ali')
maVoiture.affich_info()

