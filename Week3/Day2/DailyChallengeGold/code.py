import random

class Gene:
    def __init__(self, bival=None):
        if bival is None:
            self.bival = random.randint(0,1)
        else:
            self.bival = bival
    
    def mutate(self):
        if self.bival == 1:
            self.bival = 0
        else:
            self.bival = 1

        return self
    
class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]
    
    def mutate(self):
        for gene in self.genes:
            num = random.random()
            if num > 0.5:
                gene.mutate()
        return self
    
    def __str__(self):
        return '-'.join(str(gene.bival) for gene in self.genes)
    
class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]
    
    def mutate(self):
        for chromie in self.chromosomes:
            num = random.random()
            if num > 0.5:
                chromie.mutate()
        return self
    
    def __str__(self):
        return '=='.join(str(chromie) for chromie in self.chromosomes)


class Organism:
    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment

    def mutate(self):
        num = random.random()
        if num < self.environment:
            self.dna.mutate()

        return self
    
    def fully_evolved(self):
        for chromie in self.dna.chromosomes:
            for gene in chromie.genes:
                if gene != 1:
                    return False
        return True
    
    def __str__(self):
        return str(self.dna)


    
organism = Organism(DNA(), environment=0.75)

generation = 0

while not organism.fully_evolved():
    organism.mutate()
    generation += 1
    print(generation)

print(f"Evolution complete in {generation} generations!")
print(organism.dna)
