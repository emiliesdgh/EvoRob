import numpy as np
import os
import matplotlib.pyplot as plt

from src.utils.Filesys import get_project_root


ROOT_DIR = get_project_root()
ENV_NAME = 'Ant_custom'
results_dir = os.path.join(ROOT_DIR, 'results', ENV_NAME, 'multi')

best_individual = np.load(os.path.join(results_dir, "99", "x_best.npy"))

print("Best individual loaded from file:")
print(best_individual.shape)

f_best = np.load(os.path.join(results_dir, "99", "f_best.npy"))
print("Best fitness loaded from file:")
print(f_best)



all_fitness = np.load(os.path.join(results_dir, "full_f.npy"))
print("All fitness loaded from file:")
print(all_fitness)
print(all_fitness.shape)

all_x = np.load(os.path.join(results_dir, "full_x.npy"))
print("All individuals loaded from file:")
print(all_x.shape)


#TODO: Load the results and make a fitness curve plot.
fitnesses_full = np.load(os.path.join(results_dir, 'full_f.npy'))
fitnesses_full1 = fitnesses_full[:,:,0]
fitnesses_full2 = fitnesses_full[:,:,1]

mean_f = np.mean(fitnesses_full1, axis=1)
std_f = np.std(fitnesses_full1, axis=1)
gens = np.arange(0, 100, 1)
plt.plot(gens, mean_f, color='r')
plt.fill_between(gens, mean_f - std_f, mean_f + std_f, alpha=0.5)
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.savefig('NSGAII1_f.pdf')
plt.close()

mean_f = np.mean(fitnesses_full2, axis=1)
std_f = np.std(fitnesses_full2, axis=1)
gens = np.arange(0, 100, 1)
plt.plot(gens, mean_f, color='r')
plt.fill_between(gens, mean_f - std_f, mean_f + std_f, alpha=0.5)
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.savefig('NSGAII2_f.pdf')
plt.close()