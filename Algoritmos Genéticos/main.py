from random import random


class Individual:
    OBJECTIVE = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    MAX_FIT = 9

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness()

    def fitness(self):
        fit = 0
        for i in range(len(self.OBJECTIVE)):
            if self.chromosome[i] == self.OBJECTIVE[i]:
                fit += 1

        self.fit = 100 * fit/self.MAX_FIT

    def set_probability(population):
        total = sum([ind.fit for ind in population])
        for ind in population:
            ind.prob = ind.fit/total

    def culling(population, threshold):
        Individual.set_probability(population)
        new_population = []
        for ind in population:
            if ind.prob > threshold:
                new_population.append(ind)

        new_population.sort(key=lambda x: x.fit, reverse=True)

        return new_population

    def get_duplicate_index(self):
        # return both indexes if there are duplicates
        for i in range(len(self.chromosome)):
            for j in range(len(self.chromosome)):
                if i != j and self.chromosome[i] == self.chromosome[j]:
                    return i, j

        return -1, -1

    def crossover(self, other):
        new_chromosome = []

        copy_first_size = int(random()*3) + 4

        new_chromosome.extend(self.chromosome[:copy_first_size])
        new_chromosome.extend(other.chromosome[copy_first_size:])

        new_individual = Individual(new_chromosome)

        while new_individual.get_duplicate_index()[0] != -1:
            index, _ = new_individual.get_duplicate_index()
            new_individual.chromosome[index] = int(random()*len(self.chromosome))

        return new_individual


    def random_mutation(self):
        changed_index = int(random()*len(self.chromosome))

        while self.chromosome[changed_index] == self.OBJECTIVE[changed_index]:
            changed_index = int(random()*len(self.chromosome))

        old_value = self.chromosome[changed_index]
        while self.chromosome[changed_index] == old_value:
            self.chromosome[changed_index] = int(random()*len(self.chromosome))


        return self




if __name__ == '__main__':

    individuals = []
    for i in range(4):
        chromosome = []
        genes = [k for k in range(9)]

        while len(genes) > 0:
            gene = genes.pop(int(random()*len(genes)))
            chromosome.append(gene)

        individuals.append(Individual(chromosome))

    print("\n----------- Individuals -----------\n")
    Individual.set_probability(individuals)
    for i in range(4):
        print("Individual {} has the chromosomes {}, fitness of {:.2f} and probability of {:.2f}".format(i, individuals[i].chromosome, individuals[i].fit, individuals[i].prob))

    individuals = Individual.culling(individuals, 0.15)
    if len(individuals) == 1:
        individuals.append(individuals[0])
    individuals.sort(key=lambda x: x.fit, reverse=True)
    new_individual = individuals[0].crossover(individuals[1])
    individuals.append(new_individual)

    while len(individuals) < 4:
        fill_individual = individuals[0].crossover(individuals[1])
        individuals.append(fill_individual)

    for i in individuals:
        i.fitness()

    print("\n----------- Individuals after Culling and Crossing Over -----------\n")
    Individual.set_probability(individuals)
    for i in individuals:
        print("Individual has the chromosomes {}, fitness of {:.2f} and probability of {:.2f}".format(i.chromosome, i.fit, i.prob))


    print("\n----------- Individuals after Mutation -----------\n")
    for i in individuals:
        i.random_mutation()
        i.fitness()

    for i in individuals:
        print("Individual has the chromosomes {}, fitness of {:.2f} and probability of {:.2f}".format(i.chromosome, i.fit, i.prob))

