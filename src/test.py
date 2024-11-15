from utils import generate_random_graph
from networkx import enumerate_all_cliques
from algorithms import (
    exhaustive_clique_search,
    greedy_clique_search,
    greedy_intersection_clique_search,
)

k = 5
print("Criando grafo...")
G = generate_random_graph(seed=107637, size=100, maximum_number_edges=0.75)

print("Executando algoritmo exhaustive_clique_search...")
print(exhaustive_clique_search(graph=G, clique_size=k))

print("Executando algoritmo greedy_clique_search...")
print(greedy_clique_search(graph=G, clique_size=k))

print("Executando algoritmo greedy_intersection_clique_search...")
print(greedy_intersection_clique_search(graph=G, clique_size=k))
