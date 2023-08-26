class TinyStatistician:
    def mean(self, x):
        """
        Calcule la moyenne de la liste
        """
        if not x:
            return None
        return sum(x) / len(x)

    def median(self, x):
        """
        Calcule la mediane
        """
        if not x:
            return None
        x.sort()
        n = len(x)
        if n % 2 == 0:
            return (x[n//2 - 1] + x[n//2]) / 2
        else:
            return x[n//2]

    def quartile(self, x):
        """
        Calcule le premier et troisieme quartile
        """
        if not x:
            return None
        x.sort()
        n = len(x)
        Q1 = x[(n // 4)]
        Q3 = x[(3 * n // 4)]
        return [Q1, Q3]

    def var(self, x):
        """
        Calcule la variance.

        Moyenne de l'ecart a la moyenne au carre.
        
        La variance calcule a quel point chaque nombre est eloigne de la moyenne.
        Elle fait ensuite la moyenne de ces differences au carre.
        Une variance eleve indique que les donnees sont separes de la moyenne.
        A l'inverse une variance faible indique que les donnes sont repartis autour de la moyenne.
        """
        if not x:
            return None
        mean = self.mean(x)
        return sum((xi - mean) ** 2 for xi in x) / len(x)

    def std(self, x):
        """
        Racine carre de la variance.

        Elle calcule comme la variance l'ecart a la moyenne. Mais contrairement a la variance elle est plus simple a interpreter.
        Les ordres de grandeurs sont plus proche des donnes.
        """
        if not x:
            return None
        return (self.var(x) ** 0.5)