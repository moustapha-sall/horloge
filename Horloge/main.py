import time

class Horloge:
    def __init__(self, heures, minutes, secondes):
        self.heures = heures
        self.minutes = minutes
        self.secondes = secondes
        self.mode_12_heures = False  # Par défaut, utilise le mode 24 heures

    def afficher_heure(self):
        if self.mode_12_heures:
            am_pm = "AM" if self.heures < 12 else "PM"
            heures_affichees = self.heures % 12 if self.heures % 12 != 0 else 12
            heure_str = "{:02d}:{:02d}:{:02d} {}".format(heures_affichees, self.minutes, self.secondes, am_pm)
        else:
            heure_str = "{:02d}:{:02d}:{:02d}".format(self.heures, self.minutes, self.secondes)
        print(heure_str)

    def regler_heure(self, heures, minutes, secondes):
        self.heures = heures
        self.minutes = minutes
        self.secondes = secondes

    def regler_alarme(self, heures, minutes, secondes):
        alarme = (heures, minutes, secondes)
        while True:
            heure_actuelle = (time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec)
            if heure_actuelle == alarme:
                print("Alarme! Il est maintenant {}:{}:{}".format(*heure_actuelle))
            time.sleep(1)

    def choisir_mode_affichage(self, mode_12_heures):
        self.mode_12_heures = mode_12_heures



horloge = Horloge(15, 50, 0)

while True:
    horloge.afficher_heure()
    time.sleep(1)
    horloge.regler_heure(*time.localtime()[3:6])  # Met à jour l'heure actuelle

# Utilisation de la fonction pour régler l'alarme
# horloge.regler_alarme(17, 0, 0)

# Utilisation de la fonction pour choisir le mode d'affichage
# horloge.choisir_mode_affichage(True)  # Mode 12 heures
# horloge.choisir_mode_affichage(False)  # Mode 24 heures
