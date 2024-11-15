import itertools
from utils import benchmark
from time import time as tim


def is_clique(graph, subset):
    return all(graph.has_edge(u, v) for u, v in itertools.combinations(subset, 2))


@benchmark
def exhaustive_clique_search(graph, clique_size):
    node_list = list(graph.nodes)
    solutions_tested = 0
    operations_count = 0

    for subset in itertools.combinations(node_list, clique_size):
        solutions_tested += 1  # Increment tested solutions
        operations_count += 1 + sum(1 for _ in itertools.combinations(subset, 2))
        if is_clique(graph, subset):
            return subset, operations_count, solutions_tested

    return None, operations_count, solutions_tested


@benchmark
def greedy_clique_search(graph, clique_size):
    operations_count = 0
    solutions_tested = 0

    sorted_nodes = sorted(graph.nodes, key=lambda x: graph.degree(x), reverse=True)
    operations_count += len(sorted_nodes)  # Conta a ordenação dos nós

    for node in sorted_nodes:
        current_clique = {node}
        for potential_node in sorted_nodes:
            operations_count += 1 + len(
                current_clique
            )  # Conta a verificação de vizinhança
            if potential_node != node and all(
                graph.has_edge(potential_node, v) for v in current_clique
            ):
                current_clique.add(potential_node)

            if len(current_clique) == clique_size:
                solutions_tested += 1
                return list(current_clique), operations_count, solutions_tested

    return None, operations_count, solutions_tested


@benchmark
def greedy_intersection_clique_search(graph, clique_size):
    operations_count = 0
    solutions_tested = 0

    sorted_nodes = sorted(graph.nodes, key=lambda x: graph.degree(x), reverse=True)
    operations_count += len(sorted_nodes)  # Conta a ordenação dos nós

    for start_node in sorted_nodes:
        current_clique = {start_node}

        # Iterativamente adiciona nós com base na interseção de vizinhos
        while len(current_clique) < clique_size:
            operations_count += 1

            candidates = [
                node
                for node in graph.nodes
                if node not in current_clique
                and all(graph.has_edge(node, v) for v in current_clique)
            ]
            operations_count += len(graph.nodes)

            if not candidates:
                break

            # Escolhe o nó que maximiza a interseção de vizinhos com o clique parcial
            next_node = max(
                candidates, key=lambda x: len(set(graph.neighbors(x)) & current_clique)
            )
            operations_count += len(candidates)

            current_clique.add(next_node)

        if len(current_clique) == clique_size:
            solutions_tested += 1
            return list(current_clique), operations_count, solutions_tested

    return None, operations_count, solutions_tested
